import sys
from load_data import load_wales, load_uiot
from postgres_insert import pg_insert, retorno as avg_pstg
from influxdb_insert import influx_insert, retorno as avg_iflx
from cassandra_insert import cassandra_insert, retorno as avg_cass
from mongo_insert import mongo_insert, retorno as avg_mong
from monitor import monitor, mem, cpu
import threading

def main():
	dataSetSize = 100000;	# tamanho de dados padrao para inserir
	# checando argumentos que foram fornecidos

	if (len(sys.argv)==2):
		opt = sys.argv[1]
	elif(len(sys.argv)==3):
		opt = sys.argv[2];
		dataSetSize = int(sys.argv[1]);
	else:
		opt = input('Which database do you want to test?'
						+'\n1. PostgreSQL'
						+'\n2. InfluxDB'
						+'\n3. Cassandra'
						+'\n4. MongoDB'
						+'\n0. Cancelar e sair.\n')
	uiot = load_uiot(100)
	# uiot = load_uiot(dataSetSize)
	# for item in uiot:
	# 	print repr(item)

	if (str(opt)=='1'):
		print ("Testando PostgreSQL...");
		for i in range(5):
			print ("\n" + "Teste no. "+str(i+1));
			try:
				t1=threading.Thread(target=pg_insert, args=([uiot]));
				t2=threading.Thread(target=monitor, args=(["postgres"]))
				t1.start();
				t2.start();
				while t1.isAlive():
					pass;
				t2.do_run = False;
				while t2.isAlive():
					pass;
				# print ('Thread executed');
				if (avg_pstg):
					print ("Tempo da insercao: %.4f segundos" % avg_pstg[-1]);
				if (mem):
					mem_avg.append(sum(mem)/len(mem))
					print ("Media de memoria: %.0f KiB" % (sum(mem)/len(mem)));
					del mem[:];	# limpando as aquisicoes dessa repeticao
				if (cpu):
					cpu_avg.append(sum(cpu)/len(cpu))
					print ("Uso medio da CPU: %.4f%%" % (sum(cpu)/len(cpu)));
					del cpu[:];	# limpando as aquisicoes dessa repeticao
			except:
				print ("Erro no threading");
		print ('\n');
		if(avg_pstg):
			print ("Media global do tempo: %.4f segundos" % (sum(avg_pstg)/len(avg_pstg)));
		if mem_avg:
			print ("Media global do uso de memoria: %.0f" % (sum(mem_avg)/len(mem_avg)));
		if cpu_avg:
			print ("Media global do uso de CPU: %.4f%%"   % (sum(cpu_avg)/len(cpu_avg)));
	elif (str(opt)=='2'):
		print ("Testando InfluxDB...");
		for i in range(5):
			print ("\n"+"Teste no. "+str(i+1));
			try:
				t1=threading.Thread(target=influx_insert, args=([uiot]));
				t2=threading.Thread(target=monitor, args=(["influxdb"]))
				t1.start();
				t2.start();
				while t1.isAlive():
					pass;
				t2.do_run = False;
				while t2.isAlive():
					pass;
				# print ('Thread executed');
				if (avg_iflx):
					print ("Tempo da insercao: %.4f segundos" % avg_iflx[-1]);
				if (mem):
					mem_avg.append(sum(mem)/len(mem))
					print ("Media de memoria: %.0f KiB" % (sum(mem)/len(mem)));
					del mem[:];	# limpando as aquisicoes dessa repeticao
				if (cpu):
					cpu_avg.append(sum(cpu)/len(cpu))
					print ("Uso medio da CPU: %.4f%%" % (sum(cpu)/len(cpu)));
					del cpu[:];	# limpando as aquisicoes dessa repeticao
			except:
				print("Erro no threading");
		print ('\n');
		if(avg_iflx):
			print ("Media global do tempo: %.4f segundos" % (sum(avg_iflx)/len(avg_iflx)));
		if mem_avg:
			print ("Media global do uso de memoria: %.0f" % (sum(mem_avg)/len(mem_avg)));
		if cpu_avg:
			print ("Media global do uso de CPU: %.4f%%"   % (sum(cpu_avg)/len(cpu_avg)));
	elif (str(opt)=='3'):
		print ("Testando Cassandra...");
		for i in range(5):
			print ("\n"+"Teste no. "+str(i+1));
			try:
				t1=threading.Thread(target=cassandra_insert, args=([uiot]));
				t2=threading.Thread(target=monitor, args=(["cassandra"]))
				t1.start();
				t2.start();
				while t1.isAlive():
					pass;
				t2.do_run = False;
				while t2.isAlive():
					pass;
				#print ('Thread executed');
				if (avg_cass):
					print ("Tempo da insercao: %.4f segundos" % avg_cass[-1]);
				if (mem):
					mem_avg.append(sum(mem)/len(mem))
					print ("Media de memoria: %.0f KiB" % (sum(mem)/len(mem)));
					del mem[:];	# limpando as aquisicoes dessa repeticao
				if (cpu):
					cpu_avg.append(sum(cpu)/len(cpu))
					print ("Uso medio da CPU: %.4f%%" % (sum(cpu)/len(cpu)));
					del cpu[:];	# limpando as aquisicoes dessa repeticao
			except:
				print("Erro no threading");
		print ('\n');
		if(avg_cass):
			print ("Media global do tempo: %.4f segundos" % (sum(avg_cass)/len(avg_cass)));
		if mem_avg:
			print ("Media global do uso de memoria: %.0f" % (sum(mem_avg)/len(mem_avg)));
		if cpu_avg:
			print ("Media global do uso de CPU: %.4f%%"   % (sum(cpu_avg)/len(cpu_avg)));
	elif (str(opt)=='4'):
		print ("Testando MongoDB...");
		for i in range(5):
			print ("\n"+"Teste no. "+str(i+1));
			try:
				t1=threading.Thread(target=mongo_insert, args=([uiot]));
				t2=threading.Thread(target=monitor, args=(["mongodb"]))
				t1.start();
				t2.start();
				while t1.isAlive():
					pass;
				t2.do_run = False;
				while t2.isAlive():
					pass;
				#print ('Thread executed');
				if (avg_mong):
					print ("Tempo da insercao: %.4f segundos" % avg_mong[-1]);
				if (mem):
					mem_avg.append(sum(mem)/len(mem))
					print ("Media de memoria: %.0f KiB" % (sum(mem)/len(mem)));
					del mem[:];	# limpando as aquisicoes dessa repeticao
				if (cpu):
					cpu_avg.append(sum(cpu)/len(cpu))
					print ("Uso medio da CPU: %.4f%%" % (sum(cpu)/len(cpu)));
					del cpu[:];	# limpando as aquisicoes dessa repeticao
			except:
				print ("Erro no threading")
		print ('\n');
		if(avg_mong):
			print ("Media global do tempo: %.4f segundos" % (sum(avg_mong)/len(avg_mong)));
		if mem_avg:
			print ("Media global do uso de memoria: %.0f" % (sum(mem_avg)/len(mem_avg)));
		if cpu_avg:
			print ("Media global do uso de CPU: %.4f%%"   % (sum(cpu_avg)/len(cpu_avg)));
	elif (str(opt)=='0'):
		pass
	else:
		print ("Opcao "+str(opt)+" invalida ou indisponivel.")

mem_avg = []
cpu_avg = []
main()
