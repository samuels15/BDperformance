import couchbase
# from couchbase.admin import Admin
from couchbase.bucket import Bucket
import time

def couchbase_insert(registers):
	try:
		cb = Bucket('couchbase://127.0.0.1/tg1',username='samuel', password='samuel');	 # conectando ao couchbase no localhost 127.0.0.1
		cb.flush();
		# Testar: cb = Bucket('couchbase://10.0.2.9,10.0.2.10,10.0.2.11/tg1');
	except:
		print "Couchbase: Erro de conexao ao Bucket.";
		sys.exit(0)

	try:
		# comecar a contar o tempo e inserir os dados no couchbase
		start = time.time();
		#print("Start time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(start)))
		for item in registers:
			try:
				cb.upsert(str(item.id), {'mac': item.mac, 'clientTime': item.clientTime,	'values':item.values,	'parameters':item.parameters,	'serverTime':item.serverTime,	'serverTimef':item.serverTimef.strftime("%Y-%m-%dT%H:%M:%SZ"),	'clientTimef':item.clientTimef.strftime("%Y-%m-%dT%H:%M:%SZ")}, format=couchbase.FMT_JSON);
			except:
				print ("Erro inserindo registro no Couchbase.");
		end = time.time();
		#print("End time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(end)))
		#print("Total time: " + str(end-start) + " seconds.")
		retorno.append(end-start)
		return (end-start);
	except:
		print "Erro no Couchbase.";

def couchbase_select(query):
	try:
		cb = Bucket('couchbase://127.0.0.1/tg1',username='samuel', password='samuel');	 # conectando ao couchbase no localhost 127.0.0.1
	except:
		print "Couchbase: Erro de conexao ao Bucket.";
		sys.exit(0)
	try:
		print query
		start = time.time();
		for row in cb.n1ql_query(query):
			#print row
			pass

		end = time.time();
		retorno.append(end-start)
		return end-start
	except:
		print "Couchbase: Select falhou."

retorno=[];
