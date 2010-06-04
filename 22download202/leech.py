
from google.appengine.api import memcache
from google.appengine.api import urlfetch
from urllib import urlencode
from urllib import quote
from BeautifulSoup import BeautifulStoneSoup

def get22tracks():
    data = memcache.get( "22tracks" )
    if data is not None:
        return data

    values = { 'code': "pleasedontueverstealmy22tracksbecausethatwouldbe22wacks" }
    res = urlfetch.fetch("http://22tracks.com/get_thetracks.php", urlencode(values), method=urlfetch.POST, headers={'Content-Type': 'application/x-www-form-urlencoded'});

    if res.status_code != 200:
        return {'status': "http error"}

    soup = BeautifulStoneSoup(res.content)
    if not soup:
        return {'status': "soup error"}

    keys = ("title","artist","album","mp3", "itunes")

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
            info['url'] = "http://www.22tracks.com/admin/treks/"+quote(info['mp3'])
            tracks.append( info )
        genres[title.strip().lower()] = tracks

    memcache.add( "22tracks", genres, 3600 )
    return genres

# vim: expandtab shiftwidth=4 softtabstop=4 textwidth=79:
