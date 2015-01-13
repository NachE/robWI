#!/bin/bash

stop_ros () {
    source /opt/ros/indigo/setup.sh

    #killall nodes
    for i in $( rosnode list ); do
    rosnode kill $i;
    done

    #stop roscore
    killall roscore
}


stop_ros
