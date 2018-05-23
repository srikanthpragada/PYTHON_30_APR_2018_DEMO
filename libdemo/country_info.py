
import requests

code = input("Enter country code :")

resp = requests.get(r"https://restcountries.eu/rest/v2/alpha/" + code)
if resp.status_code == 404:
    print("Sorry! Country code not found!")
elif resp.status_code != 200:
    print("Sorry! Could not get details of country!")
else:
    details = resp.json()
    print("Country Information");
    print("Name         : " + details["name"])
    print("Captial      : " + details["capital"])
    print("Population   : " + str(details["population"]))
    print("Sharing borders with :")
    for  c in  details["borders"]:
        print(c)



