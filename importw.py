import sys
from load_data import load_wales
from postgres_insert import pg_insert
from influxdb_insert import influx_insert
from cassandra_insert import cassandra_insert
from mongo_insert import mongo_insert

def main():
	waterWales = load_wales()
	if (len(sys.argv)>1):
		opt = sys.argv[1]
	else:
		opt = input('Which database do you want to test?'
						+'\n1. PostgreSQL'
						+'\n2. InfluxDB'
						+'\n3. Cassandra'
						+'\n4. MongoDB'
						+'\nq. Cancelar e sair.\n')
	if (str(opt)=='1'):
		print ("Testando PostgreSQL...")
		for i in range(10):
			print ("\n" + "Teste no. "+str(i+1))
			avg.append(pg_insert(waterWales))
	elif (str(opt)=='2'):
		print ("Testando InfluxDB...")
		#for register in waterWales:
		#	print register
		#	print '\n'
		avg.append(influx_insert(waterWales))
	elif (str(opt)=='3'):
		print ("Testando Cassandra...");
		cassandra_insert(waterWales);
	elif (str(opt)=='4'):
		print ("Testando MongoDB...");
		mongo_insert(waterWales);
	elif (opt=='') or (opt=='q'):
		pass
	else:
		print ("Opcao "+str(opt)+" invalida.")

avg = []
main()
#if avg:
#	print ("Media do tempo: " + str(sum(avg)/len(avg)) + " segundos.")
