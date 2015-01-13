#!/usr/bin/env python

from robWI import htmlhelp
from robWI import syshelp
import os, sys
import subprocess
import pickle

pkl_file = open('../environ.pkl', 'rb')
data1 = pickle.load(pkl_file)
os.environ = data1
pkl_file.close()



htmlhelp.print_header()



htmlhelp.print_back()


#Usage: roslaunch [options] [package] <filename> [arg_name:=value...]
#       roslaunch [options] <filename> [<filename>...] [arg_name:=value...]

print 'test'

output = subprocess.check_output("echo $PYTHONPATH", shell=True)
print output


print os.environ
print 'test2'
htmlhelp.print_footer()

