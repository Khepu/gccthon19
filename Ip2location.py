import urllib.request as url
import json
def ip2loc(ip):
    response = url.urlopen("http://extreme-ip-lookup.com/json/"+ip)
    geo = json.load(response)
    return geo['country']
