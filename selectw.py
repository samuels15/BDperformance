from postgres_select import pg_select
from cassandra_select import cassandra_select
from influxdb_select import influx_select
import sys

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
		print ("Testando PostgreSQL...");
		pg_select("lab")
	if (str(opt)=='2'):
		print ("Testando InfluxDB...");
		influx_select("lab")
	if (str(opt)=='3'):
		print ("Testando Cassandra...");
		cassandra_select("lab")

main()