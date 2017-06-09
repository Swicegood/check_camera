#!/usr/bin/python

#This is a Nagios plugin that checks a camera specified by the command line augument
#it works by parsing the Zoneminder server homepage to find the number of camera events
#today and reterning "CRITICAL" if there are none.

#by Jeff Swicegood (Jaga) and Bob Gailer May 1,2017

import urllib.request

PREFIX = b"<td class=\"colEvents\"><a href=\"?view=events&amp;page=1&amp;filter[terms][0][attr]=DateTime&amp;filter[terms][0][op]=%3E%3D&amp;filter[terms][0][val]=-1+day&amp;filter[terms][1][cnj]=and&amp;filter[terms][1][attr]=MonitorId&amp;filter[terms][1][op]=%3D&amp;filter[terms][1][val]=3\" onclick=\"createPopup( '?view=events&amp;page=1&amp;filter[terms][0][attr]=DateTime&amp;filter[terms][0][op]=%3E%3D&amp;filter[terms][0][val]=-1+day&amp;filter[terms][1][cnj]=and&amp;filter[terms][1][attr]=MonitorId&amp;filter[terms][1][op]=%3D&amp;filter[terms][1][val]=3\', 'zmEvents\', 'events\' ); return( false );\">"
OFFSET = len(PREFIX)

page = urllib.request.urlopen('http://192.168.0.70/zm/index.php',
                              b'action=login&view=console&username=admin&password=xxxxxx')
page2 = page.read()
i = page2.find(PREFIX) + OFFSET 
numberofevents = page2[i]
