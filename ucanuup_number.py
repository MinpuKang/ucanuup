#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#import re
import urllib2

number = 0
#regular = "^[u,U][c,C,a,A,n,N,u,U]{5}[p,P]$"

#read the content from web
url = "http://106.75.28.160/UCloud.txt"
uscok = urllib2.urlopen(url)
input_content = uscok.read()

#count the number
for is_ucanuup in input_content.strip().split(" "):
    if is_ucanuup == "UCanUup":
        number +=1

#printout the total number
print "The number of UCanUup: %s" %number