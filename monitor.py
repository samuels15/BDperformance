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
		return int(((commands.getoutput('pgrep -u' +username)).split('\n'))[-1]);

def getpidbycmd(cmdname):
	try:
		return int(commands.getoutput('pgrep '+cmdname));
	except:
		time.sleep(1);
		return int(commands.getoutput('pgrep ' +cmdname));

def get_memory_percent(name):
	try:
		process=psutil.Process(getpid(name));
		return (process.memory_percent());
	except:
		return 0;

def get_memory_usage(name):
	try:
		# return the memory usage in percentage like top
		process = psutil.Process(getpid(name));
		# mem = process.memory_percent()
		# return mem
		return (process.memory_info().rss)/1024
	except:
		return 0;

def get_cpu_usage(name):
	try:
		process = psutil.Process(getpid(name));
		return (process.cpu_percent(interval=0.1));
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
