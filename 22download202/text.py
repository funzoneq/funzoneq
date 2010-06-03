
from leech import get22tracks

def main():
    genres = get22tracks()
    text = ""
    for genre in genres:
        for track in genres[genre]:
            text += "%s\n" % str(track['url'])
    print "Content-Type: text/plain"
    print "Content-Length:", len(text)
    print
    print text

if __name__ == '__main__':
    main()

# vim: expandtab shiftwidth=4 softtabstop=4 textwidth=79:

