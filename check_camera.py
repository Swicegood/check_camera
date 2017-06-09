#!/usr/bin/python3

#This is a Nagios plugin that checks a camera specified by the command line augument
#it works by parsing the Zoneminder server homepage to find the number of camera events
#today and reterning "CRITICAL" if there are none.

#by Jeff Swicegood (Jaga) and Bob Gailer May 1,2017

import sys
import urllib.request

camera_number = sys.argv[1].encode('ascii')

prefix = b"<td class=\"colEvents\"><a href=\"?view=events&amp;page=1&amp;filter[terms][0][attr]=DateTime&amp;filter[terms][0][op]=%3E%3D&amp;filter[terms][0][val]=-1+day&amp;filter[terms][1][cnj]=and&amp;filter[terms][1][attr]=MonitorId&amp;filter[terms][1][op]=%3D&amp;filter[terms][1][val]="+ camera_number + b"\" onclick=\"createPopup( '?view=events&amp;page=1&amp;filter[terms][0][attr]=DateTime&amp;filter[terms][0][op]=%3E%3D&amp;filter[terms][0][val]=-1+day&amp;filter[terms][1][cnj]=and&amp;filter[terms][1][attr]=MonitorId&amp;filter[terms][1][op]=%3D&amp;filter[terms][1][val]="+ camera_number + b"\', 'zmEvents\', 'events\' ); return( false );\">"
offset = len(prefix)

page = urllib.request.urlopen('http://192.168.0.70/zm/index.php',
                              b'action=login&view=console&username=admin&password=xxxxxx')
page2 = page.read()
i = page2.find(prefix) + offset 
numberofevents = page2[i]
print(page2[i:i+2])
