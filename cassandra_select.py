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
	# try:
	# 	session.execute('TRUNCATE lab');
	# except:
	# 	pass;
	# #	print ("Cassandra: Erro no truncate");
	# #	print ("Prosseguindo com a insercao...");

	try:
		start = time.time();
		# print ("Start time = "+ time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(start)))
		result = conn.query("SELECT COUNT(id) FROM "+tablename);
		end = time.time();
		# print ("End time = "+ time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(end)));
		print ("Total time: "+ str(end-start) + " seconds.");
		cluster.shutdown()
		retorno.append(end-start)
		return (end-start)
	except:
		print("Cassandra: Select falhou.");
		pass

retorno=[];
