import csv
from wales_water import WalesWater

def load_wales():
	i=0
	waterWales=[]
	with open("data/WalesWater.csv", "r") as csvfile:
		file = csv.reader(csvfile, delimiter=';',quotechar='"')
		# next (file)	# skip header
		for row in file:
			# print i
			# print waterWales[i];
			if i >= 5000:
				break
			waterWales.append(WalesWater(row))
			i+=1
		csvfile.close();
	print("Numero de registros: " + str(i))
	return waterWales
