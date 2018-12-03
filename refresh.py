#!/usr/local/bin/python

import os
import urlparse
import urllib
import requests

import json
import urllib
import urllib2

# The values below are pulled from the results in the `main.py` file
params = urllib.urlencode({
    'grant_type'    : 'refresh_token',
    'client_id'     : '',
    'client_secret' : '',
    'refresh_token': '',
    'format': 'json'
})

sandbox = "[YOUR SANDBOX NAME HERE]"
# may be different based on your instance location. 
instance_url = 'https://' + sandbox+ '.cs33.my.salesforce.com'

# Make a POST request
response = urllib.urlopen(instance_url + '/services/oauth2/token', params)
response_str = response.read()
obj = json.loads(response_str)
print "access_token", obj["access_token"]
token = obj["access_token"]


print "\n\nCreating Example SOQL Search for Accounts:"
payload = {'q':'SELECT Owner.Name, Id, OwnerId, Name FROM Account'}
headers = {'Authorization': 'OAuth '+token}
r = requests.get(instance_url + '/services/data/v44.0/query/', params=payload, headers=headers)
print r.url
print "\nRESPONSE:"
print r.json()

