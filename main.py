import os
import urlparse
import urllib
import requests

# If you have the token or conumer keu already, you can copy it here
# it is temporary so you will likely need to refresh
# leave blank to use the input program below
token = ''
consumer_key = ''

instance_url = raw_input('What instance are you using? (i.e. "https://something--name.cs33.my.salesforce.com"):')

print "Thanks! " + instance_url + "\n"

if token == "":
	token = raw_input('Have a token? Enter it now or leave blank to skip:')
	if token == "":
		#
		# GET TOKEN FOR CALLS
		#
		while (consumer_key == ""):
			consumer_key = raw_input('Add the consumer key? (See "Connected Apps"):')
		
		callback = instance_url + '/services/oauth2/success'
		login_url = instance_url + '/services/oauth2/authorize?response_type=token&client_id='+consumer_key+'&redirect_uri='+callback

		print "Opening login_url - return here when authed ...."
		print login_url

		os.system("open '"+login_url+"'");
		url_result = raw_input('If the page says "Remote Access Application Authorization", what is the URL?')

		result = dict(urlparse.parse_qsl(url_result.split("success#")[1]));
		token = urllib.unquote(result["access_token"])
		instance_url = urllib.unquote(result["instance_url"])

		print "**** WE RECEIVED ***\n\n"
		print result
		print "**** WITH THE TOKEN ***\n"
		print token
		print "**** FOR THE URL ***\n"
		print instance_url


print "Creating Example Search\n"
payload = {'q':'SELECT ID FROM CONTACT'}
headers = {'Authorization': 'OAuth '+token}
r = requests.get(instance_url + '/services/data/v20.0', params=payload, headers=headers)
print r.url + "\n"
print "RESPONSE:\n"
print r.json()
