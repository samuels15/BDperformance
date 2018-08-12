# Novas tentativas para InfluxDB e Cassandra
# TG 2 - Rodar InfluxDB novamente para 500k e para 10k
# TG2 - Rodar Cassandra novamente para 10k e 500k

python importw.py 10000 2 > results_lab/10k/influx2.txt
sleep 60
python importw.py 10000 3 > results_lab/10k/cassandra2.txt
sleep 60
python importw.py 500000 2 > results_lab/500k/influx2.txt
sleep 60
python importw.py 500000 3 > results_lab/500k/cassandra2.txt
