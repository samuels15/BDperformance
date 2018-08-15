def mkjson_string(registers):
	jsonStr = '['
	for item in registers:
		jsonStr = jsonStr + "{\n" + \
		'\t"measurement": "temperature",\n' + \
		'\t"tags": {\n'+	\
		'\t"siteID":"' + item.siteID + '",\n' + \
		'\t"sampleID":"' + item.sampleID + '",\n' + \
		'\t},\n' + \
		'\t"time":"' + item.timeTag.strftime("%Y-%m-%dT%H:%M:%SZ") + '",\n' + \
		'\t"fields": {\n' + \
		'\t"id":"' + item.id + '",\n' + \
		'\t"sampleDate":"' + item.sampleDate + '",\n' + \
		'\t"sampleTime":"' + item.sampleTime + '",\n' + \
		'\t"detCode":"' + item.detCode + '",\n' + \
		'\t"sourceCode":"' + item.sourceCode + '",\n' + \
		'\t"sampleComment":"' + item.sampleComment + '",\n' + \
		'\t"sampleFlag":"' + item.sampleFlag + '",\n' + \
		'\t"value":"' + str(item.detResult).replace(',', '.') + '"\n\t}\n},'
	jsonStr = jsonStr[:-1] + '\n]'

def mkjson_object(register):
	return {
		"measurement": "lab",
		"tags": {
			"id": register.id,
			"mac": register.mac,
			"parameters":register.parameters,
		},
		"time": register.clientTimef.strftime("%Y-%m-%dT%H:%M:%SZ"),
		"fields": {
			"clientTime":register.clientTime,
			"serverTime":register.serverTime,
			"serverTimef":register.serverTimef.strftime("%Y-%m-%dT%H:%M:%SZ"),
			"value":register.values
		}
	}
