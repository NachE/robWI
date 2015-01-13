#!/usr/bin/env python

from robWI import htmlhelp
from robWI import syshelp


htmlhelp.print_header()

htmlhelp.print_back()

print '<p>Stopping ros core</p>'

syshelp.exec_and_print_stdout('shell/rosstop_shell.sh')

htmlhelp.print_footer()

