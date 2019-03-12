# couchbasedb

#from couchbase.bucket import Bucket

# def couchbase_insert(registers):
# 	try:
# 		cb = Bucket ('couchbase://127.0.0.1/tg1', username="samuel", password="samuel");
# 	except:
# 		print ("Erro: Impossivel conectar com o Couchbase")
# 		sys.exit(0)

# 	try: 
# 		range(1000000):

# 			print "We're on time %d" % (x)

# cb.upsert('foo', {'bar': 'baz'}, format=couchbase.FMT_JSON)

# from datetime import datetime
# from make_json import mkjson_object
# import time
# import sys

# cb.upsert('foo', {'bar': 'baz'}, format=couchbase.FMT_JSON)



from couchbase.admin import Admin
from couchbase.bucket import Bucket
# from datetime import datetime
# from make_json import mkjson_object
# import time
# import sys


def couchbase_insert(registers):

	# Conectando ao banco
	try:
		adm = Admin('samuel', 'samuel', host='127.0.0.1', port=8091);
	except:
		print "Erro na conexao com o Couchbase";
		sys.exit(0)

	# recriando o bucket
	try:
		adm.bucket_remove('tg1');
		adm.bucket_create('tg1',
				  bucket_type='couchbase',
				  bucket_password='samuel',
				  flush_enabled='true');

		cb = bucket('couchbase://127.0.0.1/tg1',username='samuel', password='samuel');	 # conectando ao couchbase no localhost 127.0.0.1
		# Testar: cb = Bucket('couchbase://10.0.2.9,10.0.2.10,10.0.2.11/tg1');
	except:
		print "Couchbase: Erro resetando o bucket";
		sys.exit(0)

	try:
		# comecar a contar o tempo e inserir os dados no couchbase
		start = time.time();
		for item in registers:
			try:
				cb.upsert(item.id, {'mac': item.mac, 'clientTime': item.clientTime,	'values':item.values,	'parameters':item.parameters,	'serverTime':item.serverTime,	'serverTimef':item.serverTimef.strftime("%Y-%m-%dT%H:%M:%SZ"),	'clientTimef':item.clientTimef.strftime("%Y-%m-%dT%H:%M:%SZ")}, format=couchbase.FMT_JSON);
			except:
				print ("Erro inserindo registro no Couchbase.");
		end = time.time();
		return (end-start);
	except:
		print "Erro no Couchbase.";

retorno=[];


