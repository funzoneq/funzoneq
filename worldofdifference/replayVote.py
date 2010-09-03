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
	print service.saveVote("z8f1318468949a919a8663a68dcb613b683d0b98a443ca9c910071f259b8383d0991b9c9a5fb157cdfcc08bd87fe4baba37e06f9eab6e909b4e9c0c80c94be1dbbd007369b7cbd6daaf983b61e408869c1d1d6e863aa2bc0dfe91f71d30946532c12a8db9bcc6498e493350c6e9ea9a1421a12233d89d6f25c62e798c25aa610558c7c47a1dea7841b41946c905e7")
except:
	pass
