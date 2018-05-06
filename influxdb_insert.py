from influxdb import InfluxDBClient
from datetime import datetime
from make_json import mkjson_object
import time
import sys

def influx_insert(registers):
	try:
		conn = InfluxDBClient(host='localhost',port=8086, username='root',password='root',database='tg1')
		conn.create_database('tg1')
	except:
		print("Erro: Impossivel conectar com o InfluxDB")
		sys.exit(0)

	try:
		conn.delete_series(database='tg1', measurement='temperature')
		start = time.time()
		print("Start time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(start)))
		#i=0;
		for item in registers:
			conn.write_points([mkjson_object(item)]);
			#i+=1
			#if (i%100==0):
			#	print ("Processados %d registros" %i);
		end = time.time()
		print("End time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(end)))
		print("Total time: " + str(end-start) + " seconds.")
		return end-start
	except:
		print("Influx: Inserts nao totalmente processados")
		pass
