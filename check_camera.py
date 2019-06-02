#!/usr/bin/python2

# This is a Nagios plugin that checks a camera specified by the command line argument
# it works by parsing the Zoneminder server homepage to find the number of camera events
# today and returning "CRITICAL" if there are none.

# by Jeff Swicegood (Jaga) and Bob Gailer May 1,2017


import urllib2
import cookielib
import json


number_of_monitors_defined = 10


req = urllib2.Request('http://192.168.0.70/zm/index.php',
                      b'action=login&view=console&username=admin&password=xxxxx')

page = urllib2.urlopen(req)

c = cookielib.CookieJar()

cookielib.CookieJar.extract_cookies(c, page, req)

req2 = urllib2.Request('http://192.168.0.70/zm/api/events/consoleEvents/24%20hour.json')

cookielib.CookieJar.add_cookie_header(c, req2)

page2 = urllib2.urlopen(req2)

page2 = page2.read()

oneday_data = json.loads(page2)

req3 = urllib2.Request('http://192.168.0.70/zm/api/monitors.json')

page3 = urllib2.urlopen(req3)

monitors_data = json.loads(page3.read())

def get_monitor_name(mon_number):
    for monitor in monitors_data['monitors']:
        if (monitor['Monitor_Status']['Status'] == 'Connected') and (monitor['Monitor_Status']['MonitorId'] == mon_number):
            return monitor['Monitor']['Name']
    return "Not Found"

count = 0

message=''

for results, monitor in oneday_data.iteritems():
    for i in monitor.iteritems():
        if not int(i[1]):
            monitor_name = get_monitor_name(i[0])
            message = (message + 'CRITICAL - CAMERA ' + monitor_name.encode('UTF8') + ' has 0 events today!')
    if message != '':
        print (message)
        exit(2)
    else:
        for results, monitor in oneday_data.iteritems():
            for i in monitor.iteritems():
                message = (message + ' ' + (str(i[0].encode('UTF8')) + ':' +str(i[1].encode('UTF8'))))
        message = "OK - " + message
        print (message)
        exit(0)
