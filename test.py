# -*- coding: utf-8 -*-

import requests
import urllib
import urllib2
import sys
import re

shopId = []

def getInfo(url):
	content=urllib2.urlopen(url).read()
	typeEncode = sys.getfilesystemencoding()
	html = content.decode('utf-8').encode(typeEncode)
	pattern = re.compile('0}}\",\"description\":(.*?),\"icon_color\".*?'+
				'\"average_cost\":(.*?),.*?'+
				'float_minimum_order_amount.*?\"id\":(.*?),.*?'+
				':-1,\"name\":(.*?),\"next_business_time\".*?'+
				'\"order_lead_time\":(.*?),.*?'+
				'],\"tips\":(.*?)},\"promotion_info.*?'+
				'\"rating\":(.*?),.*?'+
				'\"recent_order_num\":(.*?),.*?',re.S)
	items = re.findall(pattern,html)
	# 0=优惠 1=人均消费 2=店名 3=配送时间 4=配送费 5=评分 6=月销量
	for item in items:
		# print item[0],item[1],"id："+item[2],item[3],item[4]+"分钟",item[5],"评分："+item[6],"月销售："+item[7]
		shopId.append(item[2])


print "start geting Info..."
getInfo("https://mainsite-restapi.ele.me/shopping/restaurants?extras%5B%5D=activities&geohash=wtw3qyjk6kx&latitude=31.19094&limit=24&longitude=121.59301&offset=0&terminal=web")
print shopId


# fp=open(‘login.html’,’w’)
# fp.write(content)
# fp.close()









# https://mainsite-restapi.ele.me/shopping/restaurants?extras%5B%5D=activities&geohash=wtw3qyjk6kx&latitude=31.19094&limit=24&longitude=121.59301&offset=0&terminal=web
# https://mainsite-restapi.ele.me/shopping/restaurants?extras%5B%5D=activities&geohash=wtw3qyjk6kx&latitude=31.19094&limit=24&longitude=121.59301&offset=24&terminal=web
# https://mainsite-restapi.ele.me/shopping/restaurants?extras%5B%5D=activities&geohash=wtw3qyjk6kx&latitude=31.19094&limit=24&longitude=121.59301&offset=48&terminal=web
# https://mainsite-restapi.ele.me/shopping/restaurants?extras%5B%5D=activities&geohash=wtw3qyjk6kx&latitude=31.19094&limit=24&longitude=121.59301&offset=72&terminal=web



