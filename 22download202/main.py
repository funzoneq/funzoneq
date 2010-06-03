#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import urlfetch
from urllib import urlencode
from BeautifulSoup import BeautifulStoneSoup
from django.utils import simplejson

class MainHandler(webapp.RequestHandler):
    def get(self):
        values = { 'code': "dontueverstealmy22tracksbecausethatwouldbe22wacks" }
        res = urlfetch.fetch("http://22tracks.com/get_alltracks.php", urlencode(values), method=urlfetch.POST, headers={'Content-Type': 'application/x-www-form-urlencoded'});
       
        if res.status_code != 200:
            print "request failed:", res.status_code
            sys.exit()
            
        soup = BeautifulStoneSoup(res.content)
        if not soup:
            print "xml failed"
            sys.exit()

        keys = ("title","artist","album","mp3")

        genres = {}
        for genre in soup.findAll( "genre" ):
            title = genre['genre']
            tracks = []
            for track in genre.findAll( "track" ):
                info = {}
                for k in keys:
                    try:
                        e = getattr(track,k)
                        info[k] = e.string.strip()
                    except AttributeError:
                        info[k] = None
                info['url'] = "http://22tracks.com/admin/mp3/"+info['mp3']
                tracks.append( info )
            genres[title.strip().lower()] = tracks
        
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(simplejson.dumps( genres ))

def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()