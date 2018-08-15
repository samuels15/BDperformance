import sys
import psycopg2
from datetime import datetime
import time

def pg_select(query):
	try:
	    conn=psycopg2.connect(	dbname='tg1', 		\
  						host='localhost', 	\
    						port='5432', 		\
    						user='postgres', 	\
    						password='200695')
	except:
		print("Erro: Impossivel conectar com o PostgreSQL.\n")
		sys.exit(0)

	cur = conn.cursor()
	try:
		print (query);
		start = time.time()
		# print("Start time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(start)))
		cur.execute(query)
		end = time.time()
		# print("End time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(end)))
		rows = cur.fetchall();
		# for item in rows:
		# 	print (item[0]);
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
