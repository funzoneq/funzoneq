from leech import get22tracks
import re

def main():
    try:
        fp = open( "22download202.tpl" )
        tpl = fp.read()
    except (IOError, OSError):
        tpl = "{content}"

    content = "<h1>Ok klaar. Het is weer leuk geweest. Punt gemaakt. Alles kan kapot. Technology is a double-edged sword. Luisteren kan gratis op de site. Kopen kan via iTunes. 22tracks heerscht. Wij <a href=\"http://22tracks.com/#/house/2/\">stuiteren</a> nog even door.</h1>"
    
    output = tpl.replace( "{content}", content.encode( "utf-8" ) )
    print "Content-Type: text/html"
    print "Content-Length:", len(output)
    print
    print output

if __name__ == "__main__":
    main()

# vim: expandtab shiftwidth=4 softtabstop=4 textwidth=79:

