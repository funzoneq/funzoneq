import json
from cgi import escape

def main():
    with open( "22tracks.json" ) as fp:
        genres = json.load( fp )
    with open( "22tracks.tpl" ) as fp:
        tpl = fp.read()
    content = u""
    for key in sorted(genres.keys()):
        g = u"<div id='%s' class='genre'>\n<div class='name'>%s</div>\n"%(key, key.title())
        g += u"<div class='info'>\n"
        for track in genres[key]:
            for k in ("title","artist","album"):
                g += u"<span class='%s'>%s</span>\n" % (k,track[k])
            g += u"<a class='url' href='%s'>download</a>\n" % escape(track['url'])
        g += u"</div>\n</div>\n\n"
        content += g
    print tpl.replace( "{content}", content.encode( "utf-8" ) )
