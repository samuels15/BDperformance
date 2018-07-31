import sys
import psycopg2
from datetime import datetime
import time

def pg_insert(registers):
	try:
	    conn=psycopg2.connect(	dbname='tg1', 		\
	    						host='localhost', 	\
	    						port='5432', 		\
	    						user='postgres', 	\
	    						password='200695')
	except:
		print("Erro 0: Impossivel conectar com o Postgre.\n")
		sys.exit(0)

	cur = conn.cursor()
	try:
		query = "DROP TABLE IF EXISTS lab"
		# print query
		cur.execute(query)
		query = "CREATE TABLE public.lab (id integer NOT NULL, clientTime double precision, serverTime double precision, clientTimef timestamp without time zone, servertimef timestamp without time zone, mac character varying (40), parameters character varying (60), values double precision);"
		cur.execute(query)
		conn.commit()
		start = time.time()
		# print("Start time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(start)))
		for item in registers:
			query = "INSERT INTO public.lab (id, clientTimef, "+\
			 	"serverTimef, clientTime, serverTime, "+\
				"mac, parameters, values) " +\
				"VALUES ("+repr(item)+");";
			cur.execute(query)
			# print (query)
		conn.commit()
		end = time.time()
		# print("End time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(end)))
		# print("Total time: " + str(end-start) + " seconds.")
		cur.close()
		conn.close()
		retorno.append(end-start)
		return end-start
	except IndexError:
		print("Erro 3: Postgre acusou erro na query de insercao.\n\n")
		conn.rollback()
		cur.close()
		conn.close()
		sys.exit(1)
retorno = [];
