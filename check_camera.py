#!/usr/bin/python

#This is a Nagios plugin that checks a camera specified by the command line augument
#it works by parsing the Zoneminder server homepage to find the number of camera events
#today and reterning "CRITICAL" if there are none.

#by Jeff Swicegood (Jaga) and Bob Gailer May 1,2017

import urllib.request
page = urllib.request.urlopen('http://192.168.0.70/zm/index.php',
                              b'action=login&view=console&username=admin&password=xxxxxx')
page2 = page.read()

