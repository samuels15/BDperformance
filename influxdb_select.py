from influxdb import InfluxDBClient
from datetime import datetime
#from make_json import mkjson_object
import time
import sys

def influx_select(tablename):
	try:
		conn = InfluxDBClient(host='localhost',port=8086, username='root',password='root',database='tg1');
	except:
		print("Erro: Impossivel conectar com o InfluxDB")
		sys.exit(0)

	try:
		start = time.time();
		# print("Start time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(start)))
		result = conn.query("SELECT COUNT(id) FROM "+tablename);
		end = time.time()
		# print("End time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(end)))
		print("Total time: " + str(end-start) + " seconds.")
		print ("Result:")
		print (result)
		retorno.append(end-start)
		return end-start
	except:
		print("InfluxDB: Select falhou");
		pass

retorno = []
influx_select();
