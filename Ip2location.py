import urllib.request as url
import json
from functools import lru_cache
@lru_cache(maxsize=None)
def ip2loc(ip):
    response = url.urlopen("http://extreme-ip-lookup.com/json/"+ip)
    geo = json.load(response)
    return geo['country']
