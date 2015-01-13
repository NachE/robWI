#!/usr/bin/env python

from robWI import htmlhelp

htmlhelp.print_header()
print '<h2>Run commands</h2>'
print '<ul>'
print '<li><a href="/cgi-bin/cosa1.py">cat /proc/cpuinfo</a></li>'
print '<li><a href="/cgi-bin/cosa2.py">roslaunch qbo_arduqbo qbo_arduqbo_default.launch</a></li>'
print '<li><a href="/cgi-bin/cosa3.py">Stop ros core</a></li>'
print '<li><a href="/cgi-bin/cosa4.py">tail -n 500 log/roslaunch.log</a></li>'
print '<li><a href="/cgi-bin/cosa5.py">rosrun neotalk</a></li>'
print '<li><a href="/cgi-bin/cosa6.py">say text</a></li>'




print '<li><a href="/cgi-bin/log/roslaunch.log">log/roslaunch.log</a></li>'

print '</ul>'


htmlhelp.print_footer()
