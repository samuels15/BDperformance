# -*- coding: utf-8 -*-
import commands
import psutil
from datetime import datetime
import time
import threading

def getpid(username):
	try:
		return int(commands.getoutput('pgrep -u' +username));
	except:
		# time.sleep(1);
		return map(int, (commands.getoutput('pgrep -u' +username)).split('\n'));

def getpidbycmd(cmdname):
	try:
		return int(commands.getoutput('pgrep '+cmdname));
	except:
		#time.sleep(1);
		return map(int, (commands.getoutput('pgrep -u' +username)).split('\n'));

def get_memory_percent(name):
	try:
		sum_mem = 0;
		for item in getpid(name):
			process=psutil.Process(item);
			sum_mem += process.memory_percent();
		return (sum_mem);
	except:
		return 0;

def get_memory_usage(name):
	# return the memory usage in percentage like top
	try:
		sum_mem = 0;
		for item in (getpid(name)):
			process = psutil.Process(item);
			sum_mem += (process.memory_info().rss)/1024
		return (sum_mem)
	except:
		return 0;

def get_cpu_usage(name):
	try:
		sum_cpu = 0;
		for item in (getpid(name)):
			process = psutil.Process(item);
			sum_cpu += (process.cpu_percent(interval=0.1));
		return (sum_cpu);
	except:
		return 0;

def monitor(name):
	t = threading.currentThread();
	while getattr(t, "do_run", True):
		mem.append(get_memory_usage(name));
		cpu.append(get_cpu_usage(name))
		# now = time.time();
	# print (i);

cpu=[]
mem=[]
