from cassandra.cluster import Cluster
from datetime import datetime
# from make_json import mkjson_object
import time
import sys

def cassandra_insert(register):
	try:
		cluster = Cluster();	 # conectando ao cassandra no localhost 127.0.0.1
		session = cluster.connect('tg1');
		session.execute ('USE tg1');
	except:
		print "Erro: Impossivel conectar com o Cassandra";
		sys.exit(0)

	try:
		query = "INSERT INTO temperature (id, siteID, sampleDate, sampleTime, detCode,"+\
                                "detResult, sourceCode, sampleID, sampleComment, sampleFlag, timeTag) "+\
                                "VALUES ("+repr(register)+");";
		print query;
		session.execute(query);
	except:
		print("Cassandra: Erro na query");
		pass
