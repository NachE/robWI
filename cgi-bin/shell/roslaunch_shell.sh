#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

nohup roslaunch qbo_arduqbo qbo_arduqbo_default.launch >$DIR/../log/roslaunch.log 2>&1 & 
