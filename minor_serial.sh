
#python importw.py 10000 1 > results_lab/10k/pg.txt
#python importw.py 10000 2 > results_lab/10k/influx.txt
#python importw.py 10000 3 > results_lab/10k/cassandra.txt
#python importw.py 10000 4 > results_lab/10k/mongo.txt

#python importw.py 50000 1 > results_lab/50k/pg.txt
#python importw.py 50000 2 > results_lab/50k/influx.txt
#python importw.py 50000 3 > results_lab/50k/cassandra.txt
#python importw.py 50000 4 > results_lab/50k/mongo.txt

#python importw.py 100000 1 > results_lab/100k/pg.txt
#python importw.py 100000 2 > results_lab/100k/influx.txt
#python importw.py 100000 3 > results_lab/100k/cassandra.txt
#python importw.py 100000 4 > results_lab/100k/mongo.txt

#python importw.py 500000 1 > results_lab/500k/pg.txt
#python importw.py 500000 2 > results_lab/500k/influx.txt
#python importw.py 500000 3 > results_lab/500k/cassandra.txt
#python importw.py 500000 4 > results_lab/500k/mongo.txt

echo "Iniciando script"
python importw.py 1000 1 > results_lab/pg.txt
echo "Pg terminado."
sleep 60
python importw.py 1000 2 > results_lab/influx.txt
echo "Influx terminado."
sleep 60
python importw.py 1000 3 > results_lab/cassandra.txt
echo "Cassandra terminado."
sleep 60
python importw.py 1000 4 > results_lab/mongo.txt
echo "Mongo terminado"
echo "Fim do script"
