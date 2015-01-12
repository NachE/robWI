#!/usr/bin/env python

from robWI import htmlhelp
from robWI import syshelp


htmlhelp.print_header()

htmlhelp.print_back()

print 'This command is running on background so there is no output'

syshelp.exec_and_print_stdout('export PYTHONPATH=/home/neo/catkin_ws/devel/lib/python2.7/dist-packages:/opt/ros/indigo/lib/python2.7/dist-packages; /usr/bin/python /opt/ros/indigo/bin/roslaunch qbo_arduqbo qbo_arduqbo_default.launch > /tmp/roslaunchlog 2>&1 &')

htmlhelp.print_footer()

