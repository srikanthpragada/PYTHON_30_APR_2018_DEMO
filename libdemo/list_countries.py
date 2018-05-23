
import requests

resp = requests.get(r"https://restcountries.eu/rest/v2/all")
countries = resp.json()
for c in countries:
     print("%3s %-50s  %-20s %-20s" % (c["alpha3Code"], c["name"][0:50], c["capital"], c["region"]))


