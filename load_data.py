import csv
from wales_water import WalesWater

def load_wales(dataSetSize):
	i=0
	waterWales=[]
	with open("data/WalesWater.csv", "r") as csvfile:
		file = csv.reader(csvfile, delimiter=';',quotechar='"')
		# next (file)	# skip header
		for row in file:
			# print i
			# print waterWales[i];
			if i >= dataSetSize:
				break
			waterWales.append(WalesWater(row))
			i+=1
		csvfile.close();
	print("Numero de registros: " + str(i))
	return waterWales
