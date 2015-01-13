#!/usr/bin/env python

from robWI import htmlhelp
from robWI import syshelp


htmlhelp.print_header()

htmlhelp.print_back()

syshelp.exec_and_print_stdout('tail -n 500 log/roslaunch.log')

htmlhelp.print_footer()

