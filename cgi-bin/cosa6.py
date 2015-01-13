#!/usr/bin/env python

from robWI import htmlhelp
from robWI import syshelp
import os, sys, pickle
import cgi

htmlhelp.print_header()

pkl_file = open('../environ.pkl', 'rb')
data1 = pickle.load(pkl_file)
os.environ = data1
pkl_file.close()

for path in os.environ['PYTHONPATH'].split(":"):
	sys.path.append(path)

htmlhelp.print_back()

form = cgi.FieldStorage()
if "saytext" in form:
	print 'speaking...'
	print form["saytext"].value	
	syshelp.exec_and_print_stdout(["rosservice", "call", "/say_es1", "'"+form["saytext"].value+"'" ],environment=os.environ)
	print 'end of speak...'


print '<form action="" method="post"><input type="text" name="saytext" /><input type="submit" value="hablar" /></form>'


htmlhelp.print_footer()


