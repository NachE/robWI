#!/usr/bin/env python

from robWI import htmlhelp
from robWI import syshelp


htmlhelp.print_header()

htmlhelp.print_back()

print 'hi, this is a module :D'

syshelp.exec_and_print_stdout('roslaunch qbo_arduqbo qbo_arduqbo_default.launch')

htmlhelp.print_footer()

