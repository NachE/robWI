#!/bin/bash

PIDNUM=`cat var/run/lighttpd.pid`

kill -9 $PIDNUM
