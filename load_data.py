import csv
from wales_water import WalesWater

def load_wales():
	i=0
	waterWales=[]
	with open("data/WalesWater.csv", "r") as csvfile:
		file = csv.reader(csvfile, delimiter=';',quotechar='"')
		# next (file)	# skip header
		for row in file:
			waterWales.append(WalesWater(row))
			# print i
			# print waterWales[i];
			if i >= 500000:
				break
			i+=1
		csvfile.close();
	print("Numero de registros: " + str(i))
	return waterWales
