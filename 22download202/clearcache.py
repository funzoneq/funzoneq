from google.appengine.api import memcache

def main():
    memcache.delete( "22tracks" )

if __name__ == "__main__":
    main()
