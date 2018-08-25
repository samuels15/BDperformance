from datetime import datetime
import time

class WalesWater:
	def __init__(self, arg):
		self.id = arg[0]
		self.siteID = arg[1]
		self.sampleDate = arg[2][:-8]
		self.sampleTime = arg[3][-8:]
		self.detCode = arg[4]
		self.detResult = arg[5]
		self.sourceCode = arg[6]
		self.sampleID = arg[7]
		self.sampleComment = arg[8]
		self.sampleFlag = arg[9]
		self.timeTag = datetime.strptime(arg[2][:-8] + arg[3][-8:], '%d/%m/%Y %H:%M:%S')

	def __repr__(self):
		return "" +\
		str(self.id) 			+",'"+ \
		str(self.siteID)			+"','"+ \
		self.sampleDate 	+"','"+ \
		self.sampleTime 	+"',"+ \
		str(self.detCode)		+","+ \
		str(self.detResult).replace(',', '.')		+",'"+ \
		self.sourceCode		+"','"+ \
		self.sampleID 		+"','"+ \
		self.sampleComment	+"','"+ \
		self.sampleFlag		+"','"+ \
		self.timeTag.strftime("%Y-%m-%dT%H:%M:%SZ") +"'"

	def __str__(self):		# define como os dados dessa classe sao printados
		return "TimeTag: " + self.timeTag.strftime("%d/%m/%y %H:%M:%S") + "\n" +\
			"Value: " + self.detResult + "\n"

class UIoT:
	def __init__(self, id, arg):
		self.id = id
		self.clientTimef = datetime.strptime(arg[0], "%Y-%m-%d %H:%M:%S")
		self.parameters = arg[1]
		self.serverTime = arg[2]
		self.clientTime = arg[3]
		self.mac = arg[4]
		self.values = arg[5]
		self.serverTimef = datetime.strptime(arg[6], "%Y-%m-%d %H:%M:%S")

	def __repr__(self):
		return "" +\
		str(self.id) 			+",'"+ \
		self.clientTimef.strftime("%Y-%m-%dT%H:%M:%SZ")	+"','"+ \
		self.serverTimef.strftime("%Y-%m-%dT%H:%M:%SZ")	+"',"+ \
		str(self.clientTime).replace(',', '.') 	+","+ \
		str(self.serverTime).replace(',', '.') 	+",'"+ \
		self.mac				+"','"	+ \
		self.parameters				+"',"+ \
		str(self.values).replace(',', '.')

	def __str__(self):		# define como os dados dessa classe sao printados
		return "clientTimef: " + self.clientTimef.strftime("%Y-%m-%d %H:%M:%S") + "\n" +\
			"Parameter: "+self.parameters+"\n"+"Value: " + self.values + "\n"
