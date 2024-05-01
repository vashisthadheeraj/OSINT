import requests
IP = input("Enter your Target IP Address: ")
print("Getting Geo Location info...")
try:
    headers = {'Accept': 'application/json'}
    geo_response = requests.request('GET', "http://ip-api.com/json/"+ IP,headers=headers)
    response = (geo_response.json())
    print("[+] Status: {}".format(response['status']))
    print("[+] Country Code: {}".format(response['countryCode']))
    print("[*] Country: {}".format(response['country']))
    print("[*] Latitude: {}".format(response['lat']))
    print("[*] Longitude: {}".format(response['lon']))
    print("[*] City: {}".format(response['city']))
    print("[*] Timezone: {}".format(response['timezone']))
    print("[*] ZIP Code: {}".format(response['zip']))

except Exception as Error:
    print(Error)