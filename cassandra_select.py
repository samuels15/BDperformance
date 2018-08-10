from cassandra.cluster import Cluster
from datetime import datetime
# from make_json import mkjson_object
import time
import sys

def cassandra_select(tablename):
	try:
		cluster = Cluster(['192.168.15.93','192.168.15.92','192.168.15.94']);	 # conectando ao cassandra no localhost 127.0.0.1
		session = cluster.connect('tg1');
	except:
		print "Erro na conexao com o Cassandra";
		sys.exit(0)

	try:
		query = "SELECT id FROM " + tablename;
		print query
		start = time.time();
		print ("Start time = "+ time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(start)))
		results = session.execute(query);
		end = time.time();
		print ("End time = "+ time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(end)));
		print ("Total time: "+ str(end-start) + " seconds.");
		count = 0
		# for item in results:
			# count+=1
			# print (count)
			# print (item.id)
		print (count)
		cluster.shutdown();
		retorno.append(end-start)
		return (end-start)
	except:
		print("Cassandra: Select falhou.");
		pass

retorno=[];
