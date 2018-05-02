import csv
import sys
import psycopg2
from influxdb import InfluxDBClient
from cassandra.cluster import Cluster

from datetime import datetime
import time
import json

class walesWater:
	id = 0
	siteID = ''
	sampleDate = ''
	sampleTime = ''
	detCode = 0
	detResult = 0
	sourceCode = ''
	sampleID = ''
	sampleComment = ''
	sampleFlag = ''
	timeTag = ''		# is going to be a timestamp

	def __init__(self, arg):
		self.id = arg[0]
		self.siteID = arg[1]
		self.sampleDate = arg[2][:-8]
		self.sampleTime = arg[3][-8:]
		self.detCode = arg[4]
		self.detResult = arg[5]
		self.sourceCode = arg[6]
		self.sampleID = arg[7]
		self.sampleComment = arg[8]
		self.sampleFlag = arg[9]
		self.timeTag = datetime.strptime(arg[2][:-8] + arg[3][-8:], '%d/%m/%Y %H:%M:%S')

	def __repr__(self): 
		return "" +\
		str(self.id) 			+",'"+ \
		str(self.siteID)			+"','"+ \
		self.sampleDate 	+"','"+ \
		self.sampleTime 	+"',"+ \
		str(self.detCode)		+","+ \
		str(self.detResult).replace(',', '.')		+",'"+ \
		self.sourceCode		+"','"+ \
		self.sampleID 		+"','"+ \
		self.sampleComment	+"','"+ \
		self.sampleFlag		+"','"+ \
		self.timeTag.strftime("%Y-%m-%d %H:%M:%S") +"'"

	def __str__(self):		# define como os dados dessa classe sao printados
		return "TimeTag: " + self.timeTag.strftime("%d/%m/%y %H:%M:%S") + "\n" +\
			"Value: " + self.detResult + "\n"

def pginsert(registers):
	try:
	    conn=psycopg2.connect(	dbname='tg1', 		\
	    						host='localhost', 	\
	    						port='5432', 		\
	    						user='postgres', 	\
	    						password='200695')
	except:
		print "Erro 0: Impossivel conectar com o Postgre.\n"
		sys.exit(0);

	cur = conn.cursor()
	try:
		query = "TRUNCATE TABLE walesTemperature";
		# print query
		cur.execute(query)
		conn.commit();
		start = time.time();
		print "Start time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(start));
		for i in range(0, len(registers)):
			query = "INSERT INTO public.walesTemperature (id, siteID, sampleDate, sampleTime, detCode,"+\
				"detResult, sourceCode, sampleID, sampleComment,sampleFlag, timeTag) " +\
				"VALUES ("+repr(registers[i])+");";
			#print str(i) + '\t' + query + '\n'
			cur.execute(query);
		conn.commit();
		end = time.time();
		print "End time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(end));
		print "Total time: " + str(end-start) + " seconds.";
		avg.append(end-start)
		cur.close();
		conn.close();
	except:
		print "Erro 3: Postgre acusou erro na query de inserir a temperatura da agua em Wales.\n\n"
		conn.rollback();
		cur.close();
		conn.close();
		sys.exit(1);

def influxinsert(registers):
	try:
		conn = InfluxDBClient(host='localhost',port=8086, username='root',password='root',database='tg1');
		conn.create_database('tg1');
	except:
		print "Erro: Impossivel conectar com o InfluxDB";
		sys.exit(0);

	try:
		conn.delete_series(database='tg1', measurement='temperature');
		start = time.time();
		print "Start time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(start));
		while len(registers)>0:
			if (len(registers)%10000==0):
				print len(registers);
			conn.write_points(mkjson_object(registers[0]));
			registers.remove(registers[0]);
		end = time.time();
		print "End time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(end));
		print "Total time: " + str(end-start) + " seconds.";
		avg.append(end-start);
	except:
		print ("Influx: Inserts nao totalmente processados");
		pass;

def cassinsert(register):
	try:
		cluster = Cluster();		# conectando ao cassandra no localhost 127.0.0.1
		session = cluster.connect('tg1');
	except:
		print "Erro: Impossivel se comunicar com o Cassandra";
		sys.exit(0);
	try:
		query = "INSERT INTO temperature (id, siteID, sampleDate, sampleTime, detCode,"+\
                                "detResult, sourceCode, sampleID, sampleComment, sampleFlag, timeTag) "+\
                                "VALUES ("+repr(register)+");";
		print query;
		session.execute(query);
	except:
		print "Erro: Cassandra acusou erro na query";
		sys.exit(1);

def loadWales():
	i=0;
	waterWales=[];
	with open("WalesWater.csv", "rb") as csvfile:
		file = csv.reader(csvfile, delimiter=';',quotechar='"')
		# next (file)	# skip header

		for row in file:
			waterWales.append(walesWater(row))
			# print i
			# print waterWales[i];
			if i >= 50000:
				break;
			i+=1;
		csvfile.close();
	print "Numero de registros: " + str(i);
	return waterWales;

def mkjson_string(registers):
	jsonStr = '[';
	for i in range(0, len(registers)):
		jsonStr = jsonStr + "{\n" + \
		'\t"measurement": "temperature",\n' + \
		'\t"tags": {\n'+	\
		'\t"siteID":"' + registers[i].siteID + '",\n' + \
		'\t"sampleID":"' + registers[i].sampleID + '",\n' + \
		'\t},\n' + \
		'\t"time":"' + registers[i].timeTag.strftime("%Y-%m-%dT%H:%M:%SZ") + '",\n' + \
		'\t"fields": {\n' + \
		'\t"id":"' + registers[i].id + '",\n' + \
		'\t"sampleDate":"' + registers[i].sampleDate + '",\n' + \
		'\t"sampleTime":"' + registers[i].sampleTime + '",\n' + \
		'\t"detCode":"' + registers[i].detCode + '",\n' + \
		'\t"sourceCode":"' + registers[i].sourceCode + '",\n' + \
		'\t"sampleComment":"' + registers[i].sampleComment + '",\n' + \
		'\t"sampleFlag":"' + registers[i].sampleFlag + '",\n' + \
		'\t"value":"' + str(registers[i].detResult).replace(',', '.') + '"\n\t}\n},'
	jsonStr = jsonStr[:-1] + '\n]'

def mkjson_object(register):
	return [
		{
			"measurement": "temperature",
			"tags": {
				"siteID": register.siteID,
				"sampleID":register.sampleID
			},
			"time": register.timeTag.strftime("%Y-%m-%dT%H:%M:%SZ"),
			"fields": {
				"id": register.id,
				"sampleDate":register.sampleDate,
				"sampleTime":register.sampleTime,
				"detCode":register.detCode,
				"sourceCode":register.sourceCode,
				"sampleComment": register.sampleComment,
				"sampleFlag":register.sampleFlag,
				"value": register.detResult
			}
		}
	];

def main():
	opt=''
	if (len(sys.argv)>1):
		opt = sys.argv[1]
	else:
		print ("Which database do you want to test?");
		print ("1. PostgreSQL;");
		print ("2. InfluxDB;");
		print ("3. Cassandra;");
		print ("q. Cancelar e sair.")
		opt = raw_input();
	if (opt=='1'):
		print ("Testando PostgreSQL...");
		waterWales = loadWales();
		for i in range (0,1):
			print "\n" + "Teste no. "+str(i+1);
			pginsert(waterWales);
	elif (opt=='2'):
		print ("Testando InfluxDB...");
		waterWales=loadWales();
		#for register in waterWales:
		#	print register
		#	print '\n'
		influxinsert(waterWales);
	elif (opt=='3'):
		print ("Testando Cassandra...");
		waterWales=loadWales();
		cassinsert(waterWales[0]);
	elif (opt=='') or (opt=='q'):
		pass;
	else:
		print ("Opcao invalida.");

avg = []
main()
if (len(avg)!=0):
	print "Media do tempo: " + str(sum(avg)/len(avg)) + " segundos.";

