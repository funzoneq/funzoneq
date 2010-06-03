from google.appengine.api import memcache

def main():
    memcache.delete( "22tracks" )
    print "cache empty"

if __name__ == "__main__":
    main()
