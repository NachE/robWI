#!/usr/bin/env python

from robWI import htmlhelp

htmlhelp.print_header()
print '<h2>Run commands</h2>'
print '<ul>'
print '<li><a href="/cgi-bin/cosa1.py">cat /proc/cpuinfo</a></li>'
print '<li><a href="/cgi-bin/cosa2.py">/opt/ros/indigo/bin/roslaunch qbo_arduqbo qbo_arduqbo_default.launch</a></li>'
print '<li><a href="/cgi-bin/cosa3.py">Cosa3</a></li>'
print '<li><a href="/cgi-bin/cosa4.py">Cosa4</a></li>'

print '</ul>'


htmlhelp.print_footer()
