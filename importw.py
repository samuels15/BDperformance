import sys
from load_data import load_wales
from postgres_insert import pg_insert, retorno as avg_pstg
from influxdb_insert import influx_insert, retorno as avg_iflx
from cassandra_insert import cassandra_insert, retorno as avg_cass
from mongo_insert import mongo_insert, retorno as avg_mong
from monitor import monitor_memory, mem
import threading

def main():
	dataSetSize = 100000;
	if (len(sys.argv)==2):
		opt = sys.argv[1]
	elif(len(sys.argv)==3):
		opt = sys.argv[1];
		dataSetSize = int(sys.argv[2]);
	else:
		opt = input('Which database do you want to test?'
						+'\n1. PostgreSQL'
						+'\n2. InfluxDB'
						+'\n3. Cassandra'
						+'\n4. MongoDB'
						+'\n0. Cancelar e sair.\n')
	waterWales = load_wales(dataSetSize);
	if (str(opt)=='1'):
		print ("Testando PostgreSQL...");
		for i in range(1): #Com threads, nao pode ter esse loop aqui, ele tera que ser repensado.
			print ("\n" + "Teste no. "+str(i+1));
			try:
				t1=threading.Thread(target=pg_insert, args=([waterWales]));
				t2=threading.Thread(target=monitor_memory, args=(["postgres"]))
				t1.start();
				t2.start();
				while t1.isAlive():
					pass;

				t2.do_run = False;

				while t2.isAlive():
					pass;
				print ('Thread executed');
				if (mem):
					print ("Media de memoria:" + str(sum(mem)/len(mem))+"KiB.")
					print ("Maximo de memoria:"+ max(mem)+"KiB.");
			except:
				pg_insert(waterWales);
			avg=avg_pstg;
			# avg.append(pg_insert(waterWales));
	elif (str(opt)=='2'):
		print ("Testando InfluxDB...");
		for i in range(2):
			print ("\n"+"Teste no. "+str(i+1));
			influx_insert(waterWales);
			avg=avg_iflx;
			# avg.append(influx_insert(waterWales));
	elif (str(opt)=='3'):
		print ("Testando Cassandra...");
		for i in range(2):
			print ("\n"+"Teste no. "+str(i+1));
			cassandra_insert(waterWales);
			avg=avg_cass;
	elif (str(opt)=='4'):
		print ("Testando MongoDB...");
		for i in range(2):
			print ("\n"+"Teste no. "+str(i+1));
			mongo_insert(waterWales);
			avg = avg_mong;
			#avg.append(mongo_insert(waterWales));
	elif (str(opt)=='0'):
		pass
	else:
		print ("Opcao "+str(opt)+" invalida.")

avg = []
main()
if avg:
	print ("Media do tempo: " + str(sum(avg)/len(avg)) + " segundos.");
	print("Media postgres_insert: "+ str(sum(avg_pg)/len(avg_pg))+" segundos.");
