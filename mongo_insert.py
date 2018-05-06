from pymongo import MongoClient
from datetime import datetime
from make_json import mkjson_object
import time
import sys

def mongo_insert(registers):
	try:
		client = MongoClient('localhost', 27017);	 # conectando ao mongo no localhost, porta 27017
		database = client['tg1'];
		temperature = database['temperature'];
		temperature.drop();
	except:
		print "Erro na conexao com o MongoDB";
		sys.exit(0)

	#try:
	# conn.delete_series(database='tg1', measurement='temperature')
	start = time.time()
	print("Start time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(start)))
	# temperature.insert_one(mkjson_object(register));
	for item in registers:
		temperature.insert_one(mkjson_object(item));
		# print mkjson_object(item);
	end = time.time()
	print("End time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(end)))
	print("Total time: " + str(end-start) + " seconds.")
	return end-start
	#except:
	#	print("MongoDB: Erro na query");
	#	pass
