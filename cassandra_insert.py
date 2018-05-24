from cassandra.cluster import Cluster
from datetime import datetime
# from make_json import mkjson_object
import time
import sys

def cassandra_insert(registers):
	try:
		cluster = Cluster();	 # conectando ao cassandra no localhost 127.0.0.1
		session = cluster.connect('tg1');
		session.execute ('TRUNCATE tg1.temperature'); # talvez passar isso pra proxima sessao.
	except:
		print "Erro na conexao com o Cassandra";
		sys.exit(0)

	try:
		start = time.time();
		print ("Start time = "+ time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(start))) 
		for item in registers:
			query = "INSERT INTO temperature (id, siteID, sampleDate, sampleTime, detCode,"+\
				"detResult, sourceCode, sampleID, sampleComment, sampleFlag, timeTag) "+\
				"VALUES ("+repr(item)+");";
			#print query;
			session.execute(query);
		end = time.time();
		print ("End time = "+ time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(end)));
		print ("Total time: "+ str(end-start) + " seconds.");
		cluster.shutdown()
		retorno.append(end-start)
		return (end-start)
	except:
		print("Cassandra: Erro na query");
		pass

retorno=[];
