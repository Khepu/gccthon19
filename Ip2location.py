import urllib.request as url

import json
import pandas as pd

data = pd.read_csv("datasets/website-access.data",sep=" ",header=None)

ip = data[0][1]




response = url.urlopen("http://extreme-ip-lookup.com/json/"+ip)
geo = json.load(response)
print(data)
print(ip)
print(geo['country'])
