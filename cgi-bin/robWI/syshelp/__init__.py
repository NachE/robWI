#!/usr/bin/env python

import subprocess, os

def exec_and_print_stdout(command,environment=os.environ):
	s='<p>running ' + command + '...</p>'
	print (s)
	command = command.split()
	p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=environment)
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


def exec_on_background(command,environment=os.environ):
	s='<p>running ' + command + '...</p>'
	print (s)
	command = command.split()
	pid = os.spawnvpe(os.P_NOWAIT, command[0], command, env=environment)
	return pid	
