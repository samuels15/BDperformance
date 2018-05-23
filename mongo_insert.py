from pymongo import MongoClient
from datetime import datetime
from make_json import mkjson_object
import time
import sys
import monitor
def mongo_insert(registers):
	try:
		client = MongoClient('localhost', 27017);	 # conectando ao mongo no localhost, porta 27017
		database = client['tg1'];
		temperature = database['temperature'];
		temperature.drop();
	except:
		print "Erro na conexao com o MongoDB";
		sys.exit(0)
	mem_array=[];
	try:
		start = time.time()
		print("Start time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(start)))
		for item in registers:
			temperature.insert_one(mkjson_object(item));
			mem_array.append(monitor.get_memory_usage("mongodb"));
			# print mkjson_object(item);
		end = time.time()
		print("End time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(end)))
		print("Total time: " + str(end-start) + " seconds.")
		print("Average memory used: "+str(sum(mem_array)/len(mem_array))+"KiB.");
		return end-start
	except:
		print("MongoDB: Erro na query");
		pass
#	print mem_array;
#	return end-start
