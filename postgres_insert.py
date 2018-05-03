import sys
import psycopg2
from datetime import datetime
import time

def pg_insert(registers):
	try:
	    conn=psycopg2.connect(	dbname='pibic', 		\
	    						host='localhost', 	\
	    						port='5432', 		\
	    						user='postgres', 	\
	    						password='7323')
	except:
		print("Erro 0: Impossivel conectar com o Postgre.\n")
		sys.exit(0)

	cur = conn.cursor()
	try:
		query = "TRUNCATE TABLE walesTemperature"
		# print query
		cur.execute(query)
		conn.commit()
		start = time.time()
		print("Start time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(start)))
		for item in registers:
			query = "INSERT INTO public.walesTemperature (id, siteID, sampleDate, sampleTime, detCode,"+\
				"detResult, sourceCode, sampleID, sampleComment,sampleFlag, timeTag) " +\
				"VALUES ("+repr(item)+");";
			#print str(i) + '\t' + query + '\n'
			cur.execute(query)
		conn.commit()
		end = time.time()
		print("End time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(end)))
		print("Total time: " + str(end-start) + " seconds.")
		cur.close()
		conn.close()
		return end-start
	except IndexError:
		print("Erro 3: Postgre acusou erro na query de inserir a temperatura da agua em Wales.\n\n")
		conn.rollback()
		cur.close()
		conn.close()
		sys.exit(1)
