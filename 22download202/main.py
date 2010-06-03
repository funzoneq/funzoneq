
from django.utils import simplejson
from leech import get22tracks

def main():
    tracks = get22tracks()
    json = simplejson.dumps( tracks )
    print "Content-Type: application/json"
    print "Content-Length:", len(json)
    print
    print json

if __name__ == '__main__':
    main()

# vim: expandtab shiftwidth=4 softtabstop=4 textwidth=79:

