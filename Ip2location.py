import pandas as pd

data1 = pd.read_csv("GeoLite2-Country-Blocks-IPv4.csv")

data2 = pd.read_csv("GeoLite2-Country-Locations-en.csv")


data1.drop(columns=["registered_country_geoname_id","represented_country_geoname_id","is_anonymous_proxy","is_satellite_provider"],axis=1,inplace=True)
data2.drop(columns=["locale_code","continent_code","continent_name","country_iso_code","is_in_european_union"],axis=1,inplace=True)


result = pd.merge(data1, data2, how='inner', on=['geoname_id', 'geoname_id'])

result.drop(columns=["geoname_id"],axis=1,inplace=True)

print(result)
