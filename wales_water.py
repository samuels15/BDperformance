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
