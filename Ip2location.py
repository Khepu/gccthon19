import urllib.request as url
import json
import pandas as pd
def ip2loc(ip):
    response = url.urlopen("http://extreme-ip-lookup.com/json/"+ip)
    geo = json.load(response)
    return geo['country']
