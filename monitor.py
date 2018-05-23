# -*- coding: utf-8 -*-
import commands
import psutil
from datetime import datetime
import time

def getpid(username):
	try:
		return int(commands.getoutput('pgrep -u' +username));
	except:
		time.sleep(1);
		return int(commands.getoutput('pgrep -u' +username));

#def getpidbycmd(cmdname):
#	try:
#		return int(commands.getoutput('pgrep '+cmdname));
#	except:
#		time.sleep(1);
#		return int(commands.getoutput('pgrep ' +cmdname));

def get_memory_percent(name):
	process=psutil.Process(getpid(name));
	return (process.memory_percent());

def get_memory_usage(name):
	# return the memory usage in percentage like top
	process = psutil.Process(getpid(name));
	# mem = process.memory_percent()
	# return mem
	return (process.memory_info().rss)/1024

def get_cpu_usage(name):
	process = psutil.Process(getpid(name));
	return (process.cpu_percent());

# consume_memory = range(20*1000*1000)
# mem_array=[]
# cpu_array=[]
# start = time.time();
# now = time.time();
# print("Start time = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(start)))
# while (now - start <= 10):
# 	mem_array.append(get_memory_usage('quicklookd'));
# 	cpu_array.append(get_cpu_usage('quicklookd'));
# 	now = time.time();
# 	#mem_array.append(memory_usage_psutil())
# print("Now = " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(now)));
# print ("Uso médio da memória: ");
# print sum(mem_array)/len(mem_array);

# print ("Uso médio da CPU: ")
# print sum(cpu_array)/len(cpu_array);

