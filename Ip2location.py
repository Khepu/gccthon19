import pandas as pd

data1 = pd.read_csv("GeoLite2-Country-Blocks-IPv4.csv")

data2 = pd.read_csv("GeoLite2-Country-Locations-en.csv")

data1.drop(columns=["registered_country_geoname_id","represented_country_geoname_id","is_anonymous_proxy","is_satellite_provider"])

print(data1)
#result = pd.merge(data1, data2, how='inner', on=['geoname_id', 'geoname_id'])


#print(result["country_name"])


