#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

nohup rosrun qbo_talk neo_talk.py >$DIR/../log/rosrun_neo_talk.log 2>&1 & 
