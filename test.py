# -*- coding: utf-8 -*-

import requests
import urllib
import urllib2
import sys
import re

content=urllib2.urlopen('https://mainsite-restapi.ele.me/shopping/restaurants?extras%5B%5D=activities&geohash=wtw3qyjk6kx&latitude=31.19094&limit=24&longitude=121.59301&offset=0&terminal=web').read()
typeEncode = sys.getfilesystemencoding()
html = content.decode('utf-8').encode(typeEncode)

# print html

pattern = re.compile('0}}\",\"description\":(.*?),\"icon_color\".*?'+
				''+
				':-1,\"name\":(.*?),\"next_business_time\".*?'+
				'],\"tips\":(.*?)},\"promotion_info.*?',re.S)
items = re.findall(pattern,html)

# 0=优惠 1=名称 2=配送费


for item in items:
	print item[0],item[1],item[2]

# fp=open(‘login.html’,’w’)
# fp.write(content)
# fp.close()









# https://mainsite-restapi.ele.me/shopping/restaurants?extras%5B%5D=activities&geohash=wtw3qyjk6kx&latitude=31.19094&limit=24&longitude=121.59301&offset=0&terminal=web
# https://mainsite-restapi.ele.me/shopping/restaurants?extras%5B%5D=activities&geohash=wtw3qyjk6kx&latitude=31.19094&limit=24&longitude=121.59301&offset=24&terminal=web
# https://mainsite-restapi.ele.me/shopping/restaurants?extras%5B%5D=activities&geohash=wtw3qyjk6kx&latitude=31.19094&limit=24&longitude=121.59301&offset=48&terminal=web
# https://mainsite-restapi.ele.me/shopping/restaurants?extras%5B%5D=activities&geohash=wtw3qyjk6kx&latitude=31.19094&limit=24&longitude=121.59301&offset=72&terminal=web



