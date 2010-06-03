from leech import get22tracks
import re

def main():
    genres = get22tracks()
    try:
        fp = open( "22download202.tpl" )
        tpl = fp.read()
    except (IOError, OSError):
        tpl = "{content}"
    content = u""
    rx_key2id = re.compile( r"[^a-zA-Z0-9]+" )
    for key in sorted(genres.keys()):
        id = rx_key2id.sub( "-", key )
        g = u"<div id='%s' class='genre'>\n<div class='name'>%s</div>\n"%(id, key.title())
        g += u"<div class='info'>\n"
        for track in genres[key]:
            g += "<div class='track'>\n"
            for k in ("title","artist","album"):
                data = track[k]
                if not data or len(data.strip()) < 1:
                    data = "&nbsp;"
                g += u"<span class='%s'>%s</span>\n" % (k,data)
            g += u"<a class='url' href='%s'>download</a>\n" % track['url']
            g += "</div>\n\n"
        g += u"</div>\n</div>\n\n\n"
        content += g
    print tpl.replace( "{content}", content.encode( "utf-8" ) )

if __name__ == "__main__":
    main()

# vim: expandtab shiftwidth=4 softtabstop=4 textwidth=79:

