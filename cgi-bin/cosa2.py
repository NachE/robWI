#!/usr/bin/env python

from robWI import htmlhelp
from robWI import syshelp
import os, sys, pickle


htmlhelp.print_header()

pkl_file = open('../environ.pkl', 'rb')
data1 = pickle.load(pkl_file)
os.environ = data1
pkl_file.close()

for path in os.environ['PYTHONPATH'].split(":"):
	sys.path.append(path)


#pythonpath = ''
#pythonpath += ':'.join(x for x in sys.path if x)
#os.environ['PYTHONPATH'] = pythonpath



htmlhelp.print_back()


#Usage: roslaunch [options] [package] <filename> [arg_name:=value...]
#       roslaunch [options] <filename> [<filename>...] [arg_name:=value...]

syshelp.exec_on_background("shell/roslaunch_shell.sh",environment=os.environ)

print ('This command is exec in background, you can see the log on <a href="/cgi-bin/log/roslaunch.log">log/roslaunch.log</a>')

htmlhelp.print_footer()


