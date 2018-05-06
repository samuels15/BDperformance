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
		#while len(registers) > 0:
		#	if (len(registers)%10000 == 0):
		#		print('Faltam %d registros.' %len(registers))
		#	conn.write_points(mkjson_object(registers[0]))
		#	registers.remove(registers[0])
		for item in registers:
			conn.write_points(mkjson_object(item));
		end = time.time()
		print("End time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(end)))
		print("Total time: " + str(end-start) + " seconds.")
		return end-start
	except:
		print("Influx: Inserts nao totalmente processados")
		pass
