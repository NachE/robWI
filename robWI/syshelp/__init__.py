#!/usr/bin/env python

import subprocess

def exec_and_print_stdout(command):
	s='<p>running ' + command + '...</p>'
	print (s)
	command = command.split()
	p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	print ('<plaintext>')
	for line in p.stdout:
		print (line),
		#print(line, end="") <-this for python3
	print ('</plaintext>')

	print ('<plaintext>')
	for line in p.stderr:
		print (line),
	print ('</plaintext>')

	print ('<p>Done</p>')
