from postgres_select import pg_select, retorno as avg_pstg
from cassandra_select import cassandra_select, retorno as avg_cass
from influxdb_select import influx_select, retorno as avg_iflx
from couchbase_support import couchbase_select, retorno as avg_couch
from monitor import monitor, mem, cpu
import sys, time, threading

def main():
	if(len(sys.argv)==2):
		opt = sys.argv[1]
	else:
		opt = input('Which database do you want to test?' \
						+'\n1. PostgreSQL'\
						+'\n2. InfluxDB'  \
						+'\n3. Cassandra' \
						#+'\n4. MongoDB'  \
						+'\n0. Cancelar e sair.\n');
	if (str(opt)=='1'):
		query = "SELECT parameters, COUNT(*) FROM lab GROUP BY parameters;"
		# query = "SELECT EXTRACT(MONTH FROM clienttimef), parameters, AVG(values) FROM lab group by 1, 2;"
		print ("Testando PostgreSQL...");
		print query;
		for i in range(5):
			print ("\n" + "Teste no. "+str(i+1));
			try:
				t1=threading.Thread(target=pg_select, args=([query]));
				t2=threading.Thread(target=monitor, args=(["postgres"]))
				try:
					t1.start();
				except:
					print ("Erro ao iniciar pg_select")
				try:
					t2.start();
				except:
					print ("Erro ao iniciar monitor")
				while t1.isAlive():
					pass;
				t2.do_run = False;
				while t2.isAlive():
					pass;
			except:
				print ("Erro no threading");

			if (avg_pstg):
				print ("Tempo da consulta: %.4f segundos" % avg_pstg[-1]);
			if (mem):
				mem_avg.append(sum(mem)/len(mem))
				print ("Media de memoria: %.0f KiB" % (sum(mem)/len(mem)));
				del mem[:];	# limpando as aquisicoes dessa repeticao
			if (cpu):
				cpu_avg.append(sum(cpu)/len(cpu))
				print ("Uso medio da CPU: %.4f%%" % (sum(cpu)/len(cpu)));
				del cpu[:];	# limpando as aquisicoes dessa repeticao
			time.sleep(60)		# Pausa de um minuto antes da proxima bateria de testes
		print ('\n');
		if(avg_pstg):
			print ("Media global do tempo: %.4f segundos" % (sum(avg_pstg)/len(avg_pstg)));
		if mem_avg:
			print ("Media global do uso de memoria: %.0f" % (sum(mem_avg)/len(mem_avg)));
		if cpu_avg:
			print ("Media global do uso de CPU: %.4f%%"   % (sum(cpu_avg)/len(cpu_avg)));

	if (str(opt)=='2'):
		print ("Testando InfluxDB...");
		query="SELECT COUNT(clientTime) FROM lab GROUP BY parameters;"
		print query;
		for i in range(5):
			print ("\n" + "Teste no. "+str(i+1));
			try:
				t1=threading.Thread(target=influx_select, args=([query]));
				t2=threading.Thread(target=monitor, args=(["influxdb"]))
				try:
					t1.start();
				except:
					print ("Erro ao iniciar influxdb_select")
				try:
					t2.start();
				except:
					print ("Erro ao iniciar monitor")
				while t1.isAlive():
					pass;
				t2.do_run = False;
				while t2.isAlive():
					pass;
			except:
				print ("Erro no threading");

			if (avg_iflx):
				print ("Tempo da consulta: %.4f segundos" % avg_iflx[-1]);
			if (mem):
				mem_avg.append(sum(mem)/len(mem))
				print ("Media de memoria: %.0f KiB" % (sum(mem)/len(mem)));
				del mem[:];	# limpando as aquisicoes dessa repeticao
			if (cpu):
				cpu_avg.append(sum(cpu)/len(cpu))
				print ("Uso medio da CPU: %.4f%%" % (sum(cpu)/len(cpu)));
				del cpu[:];	# limpando as aquisicoes dessa repeticao
			time.sleep(60)		# Pausa de um minuto antes da proxima bateria de testes
		print ('\n');
		if(avg_iflx):
			print ("Media global do tempo: %.4f segundos" % (sum(avg_iflx)/len(avg_iflx)));
		if mem_avg:
			print ("Media global do uso de memoria: %.0f" % (sum(mem_avg)/len(mem_avg)));
		if cpu_avg:
			print ("Media global do uso de CPU: %.4f%%"   % (sum(cpu_avg)/len(cpu_avg)));


	if (str(opt)=='3'):
		query = "SELECT parameters, COUNT(*) FROM lab GROUP BY parameters;";
		print ("Testando Cassandra...");
		print query
		for i in range(5):
			print ("\n" + "Teste no. "+str(i+1));
			try:
				t1=threading.Thread(target=cassandra_select, args=([query]));
				t2=threading.Thread(target=monitor, args=(["cassandra"]))
				try:
					t1.start();
				except:
					print ("Erro ao iniciar cassandra_select")
				try:
					t2.start();
				except:
					print ("Erro ao iniciar monitor")
				while t1.isAlive():
					pass;
				t2.do_run = False;
				while t2.isAlive():
					pass;
			except:
				print ("Erro no threading");

			if (avg_cass):
				print ("Tempo da consulta: %.4f segundos" % avg_cass[-1]);
			if (mem):
				mem_avg.append(sum(mem)/len(mem))
				print ("Media de memoria: %.0f KiB" % (sum(mem)/len(mem)));
				del mem[:];	# limpando as aquisicoes dessa repeticao
			if (cpu):
				cpu_avg.append(sum(cpu)/len(cpu))
				print ("Uso medio da CPU: %.4f%%" % (sum(cpu)/len(cpu)));
				del cpu[:];	# limpando as aquisicoes dessa repeticao
			time.sleep(60)		# Pausa de um minuto antes da proxima bateria de testes
		print ('\n');
		if(avg_cass):
			print ("Media global do tempo: %.4f segundos" % (sum(avg_cass)/len(avg_cass)));
		if mem_avg:
			print ("Media global do uso de memoria: %.0f" % (sum(mem_avg)/len(mem_avg)));
		if cpu_avg:
			print ("Media global do uso de CPU: %.4f%%"   % (sum(cpu_avg)/len(cpu_avg)));


	if (str(opt)=='5'):
		query = "SELECT parameters, COUNT(*) FROM tg1 GROUP BY parameters";
		print ("Testando Couchbase...");
		print query
		for i in range(5):
			print ("\n" + "Teste no. "+str(i+1));
			try:
				t1=threading.Thread(target=couchbase_select, args=([query]));
				t2=threading.Thread(target=monitor, args=(["couchbase"]))
				try:
					t1.start();
				except:
					print ("Erro ao iniciar couchbase_select")
				try:
					t2.start();
				except:
					print ("Erro ao iniciar monitor")
				while t1.isAlive():
					pass;
				t2.do_run = False;
				while t2.isAlive():
					pass;
			except:
				print ("Erro no threading");

			if (avg_couch):
				print ("Tempo da consulta: %.4f segundos" % avg_couch[-1]);
			if (mem):
				mem_avg.append(sum(mem)/len(mem))
				print ("Media de memoria: %.0f KiB" % (sum(mem)/len(mem)));
				del mem[:];	# limpando as aquisicoes dessa repeticao
			if (cpu):
				cpu_avg.append(sum(cpu)/len(cpu))
				print ("Uso medio da CPU: %.4f%%" % (sum(cpu)/len(cpu)));
				del cpu[:];	# limpando as aquisicoes dessa repeticao
			time.sleep(60)		# Pausa de um minuto antes da proxima bateria de testes
		print ('\n');
		if(avg_couch):
			print ("Media global do tempo: %.4f segundos" % (sum(avg_couch)/len(avg_couch)));
		if mem_avg:
			print ("Media global do uso de memoria: %.0f" % (sum(mem_avg)/len(mem_avg)));
		if cpu_avg:
			print ("Media global do uso de CPU: %.4f%%"   % (sum(cpu_avg)/len(cpu_avg)));




mem_avg = []
cpu_avg = []
main()
