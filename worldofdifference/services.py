#!/usr/bin/env python

import logging, binascii, rc4, random, hashlib, names, time
from pyamf.remoting.client import RemotingService

key = 'wodrocks'

def doVote(data):
	appReferer = 'http://vodafone.egotribe.nl/WOD2010_Loader01.swf?random='+str(random.randint(10000, 99999))

	logging.basicConfig(
	    level=logging.DEBUG,
	    format='%(asctime)s %(levelname)-5.5s [%(name)s] %(message)s'
	)

	gw = RemotingService('http://flashservices.egotribe.nl/gateway.php', referer=appReferer, logger=logging)
	service = gw.getService('vodafoneGadget')

	print service.saveVote(data)

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
	UIDs = [ 'b3cdf321c6c019d3', 'efbbf92b7dab2f3e', 'f4953a7d462d4bd8', 'c9bed70e4525ef9a', 'a7a35424b016e22a', '272bf47d9ceeb3d4' ]
	data =  UIDs[random.randint(0, len(UIDs))-1]+';'
	data += randUserID()+';'
	data += names.MName(3, "voor").New()+";"
	data += names.MName(3, "achter").New()+";"
	data += genHyvesURL()+";"

	return data

def hex0rcrypt(data, key):
	crypt = rc4.rc4crypt(data, key)
	return "z"+binascii.hexlify(crypt)

# Hier je proxies inlezen van een bestand, zorg er voor dat het allemaal http
# proxies zijn. Je kan ze uit Nils zijn code halen van pollbuster.
#
# code:
#  proxies = open("proxies.txt").readlines()

# Loop door de proxies:
#
# code:
#  for proxy in proxies:
for i in range(0, 2000):
	data = generateUserInfo()
	hex = hex0rcrypt(data, key)
    # Set hier eerst de proxy, er vanuit gaande dat elke regel van het bestand
    # dit bevat: "http://host:port/"
    #
    # code:
    #  proxy_handler = urllib2.ProxyHandler({'http': proxy})
    #  opener = urllib2.build_opener(proxy_handler)
    #  urllib2.install_opener(opener)
    #
	doVote(hex)
	time.sleep(0.5)

# vim: expandtab shiftwidth=4 softtabstop=4 textwidth=79:

