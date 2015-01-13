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


htmlhelp.print_back()

syshelp.exec_on_background("shell/rosrun_neotalk.sh",environment=os.environ)

print ('<p>This command is exec in background, you can see the log on <a href="/cgi-bin/log/rosrun_neo_talk.log">log/rosrun_neo_talk.log</a></p>')

htmlhelp.print_footer()


