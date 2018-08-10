import sys
import psycopg2
from datetime import datetime
import time

def pg_insert(tablename):
	try:
	    conn=psycopg2.connect(	dbname='tg1', 		\
	    						host='localhost', 	\
	    						port='5432', 		\
	    						user='postgres', 	\
	    						password='200695')
	except:
		print("Erro: Impossivel conectar com o Postgre.\n")
		sys.exit(0)

	cur = conn.cursor()
	try:
		start = time.time()
		# print("Start time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(start)))
		result= cur.execute("SELECT COUNT(id) FROM "+tablename)
		end = time.time()
		# print("End time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(end)))
		print("Total time: " + str(end-start) + " seconds.")
		cur.close()
		conn.close()
		retorno.append(end-start)
		return end-start
	except:
		print ("PostgreSQL: select falhou")
		conn.rollback()
		cur.close()
		conn.close()
		sys.exit(1)
retorno = [];
