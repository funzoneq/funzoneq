#!/usr/bin/env python

import logging, binascii, rc4, random, hashlib, names, time, urllib2
from pprint import pprint
from pyamf.remoting.client import RemotingService

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
	print service.getUserMD("z3f4b828d5679d5f817dc76f46d3076f8")
except:
	pass
