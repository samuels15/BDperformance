from cassandra.cluster import Cluster
from datetime import datetime
# from make_json import mkjson_object
import time
import sys

def cassandra_insert(registers):
	try:
		cluster = Cluster(['192.168.15.93','192.168.15.92','192.168.15.94']);	 # conectando ao cassandra no localhost 127.0.0.1
		session = cluster.connect('tg1');
		session.execute ("CREATE KEYSPACE IF NOT EXISTS tg1 WITH REPLICATION= {'class' : 'SimpleStrategy', 'replication_factor' : 3};");
		session.execute ('CREATE TABLE IF NOT EXISTS lab(id int, clientTime float, serverTime float, clientTimef timestamp, serverTimef timestamp, mac text, parameters text, values float, PRIMARY KEY (parameters, id));');
		# session.execute ('TRUNCATE TABLE lab');	# talvez passar isso pra proxima sessao.
	except:
		print "Erro na conexao com o Cassandra";
		sys.exit(0)
	try:
		session.execute('TRUNCATE lab');
	except:
		pass;
	#	print ("Cassandra: Erro no truncate");
	#	print ("Prosseguindo com a insercao...");

	try:
		start = time.time();
		# print ("Start time = "+ time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(start)))
		error_count=0;
		for item in registers:
			query = "INSERT INTO lab (id, clientTimef, serverTimef, "+\
			 	"clientTime, serverTime, mac, parameters, values) "+\
				" VALUES ("+repr(item)+");";
			try:
				session.execute(query);
			except:
				try:
					session.execute(query);
				except:
					try:
						session.execute(query);
					except:
						error_count+=1;
						# print ("Erro na execucao da query.");
						with open("erros/cass.txt", "a") as outfile:
							outfile.write(query)
		print ("Error count: "+ str(error_count));
		end = time.time();
		# print ("End time = "+ time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(end)));
		# print ("Total time: "+ str(end-start) + " seconds.");
		cluster.shutdown()
		retorno.append(end-start)
		return (end-start)
	except:
		print("Cassandra: Erro na query");
		pass

retorno=[];
