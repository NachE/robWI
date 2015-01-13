#!/bin/bash


python -c "import pickle, os; output = open('environ.pkl', 'wb'); pickle.dump(os.environ, output); output.close()"
/usr/sbin/lighttpd -f conf/lighttpd.conf
