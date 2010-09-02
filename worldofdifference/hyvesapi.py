from pprint import pprint
import simplejson as json
import oauth2 as oauth
import urllib

# Create your consumer with the proper key/secret.
consumer = oauth.Consumer(key="NzEwNV-Mx6aKn-h9ZVpfCmhxamd2", secret="NzEwNV_I3Y7lXMajgw9WjJB_mrGU")

# Request token URL for Twitter.
authorize_url = "http://www.hyves.nl/api/authorize/"
request_token_url = "http://data.hyves-api.nl/?ha_fancylayout=false&ha_format=json&ha_method=auth.requesttoken&ha_version=1.2&methods=users.get%2Cfriends.get%2Cusers.search"
access_token_url = "http://data.hyves-api.nl/?ha_fancylayout=false&ha_format=json&ha_method=auth.accesstoken&ha_version=1.2"
search_users_url = "http://data.hyves-api.nl/?searchterms=%s&ha_method=users.search&ha_resultsperpage=50&ha_version=2.0&ha_format=json&ha_fancylayout=false"

# Create our client.
client = oauth.Client(consumer)

# The OAuth Client request works just like httplib2 for the most part.
resp, content = client.request(request_token_url, "GET")
request_token = json.loads(content)

print "Request Token:"
print "    - oauth_token        = %s" % request_token['oauth_token']
print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']
print 

# Step 2: Redirect to the provider. Since this is a CLI script we do not 
# redirect. In a web application you would redirect the user to the URL
# below.

print "Go to the following link in your browser:"
print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
print 

# After the user has granted access to you, the consumer, the provider will
# redirect you to whatever URL you have told them to redirect to. You can 
# usually define this in the oauth_callback argument as well.
accepted = 'n'
while accepted.lower() == 'n':
    accepted = raw_input('Have you authorized me? (y/n) ')


# Step 3: Once the consumer has redirected the user back to the oauth_callback
# URL you can request the access token the user has approved. You use the 
# request token to sign this request. After this is done you throw away the
# request token and use the access token returned. You should store this 
# access token somewhere safe, like a database, for future use.
token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
client = oauth.Client(consumer, token)

resp, content = client.request(access_token_url, "POST")
access_token = json.loads(content)

print "Access Token:"
print "    - oauth_token        = %s" % access_token['oauth_token']
print "    - oauth_token_secret = %s" % access_token['oauth_token_secret']
print
print "You may now access protected resources using the access tokens above." 
print

# Step 4: Now we search
token = oauth.Token(access_token['oauth_token'], access_token['oauth_token_secret'])
client = oauth.Client(consumer, token)

resp, content = client.request((search_users_url) % urllib.quote("Henk-Jan Klaassen"), "POST")

pprint(resp)
pprint(content)

results = json.loads(content)
pprint(results)
