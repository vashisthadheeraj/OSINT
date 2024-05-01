import requests
domain = input("Enter your Domain Name: ")

try:
    headers = {'Accept': 'application/json'}
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key=d3ddf041687d499b05a2c6cbd15b3be6e9236b9b"
    response = requests.get(url)
    output = response.json()
    print("[+] Domain: {}".format(output['data']['domain']))
    print("[+] Organization: {}".format(output['data']['organization']))
    print("[*] Industry: {}".format(output['data']['industry']))
    print("[*] Disposable: {}".format(output['data']['disposable']))
    print("[*] Webmail: {}".format(output['data']['webmail']))
    # print("[*] Social Media: {}".format(output['data']['twitter', 'facebook', 'linkedin', 'instagram', 'youtube']))
    print("[*] Technologies: {}".format(output['data']['technologies']))
    print("[*] Country: {}".format(output['data']['country']))
    print("[*] State: {}".format(output['data']['state']))
    print("[*] City: {}".format(output['data']['city']))
    print("[*] PIN Code: {}".format(output['data']['postal_code']))
    print("[*] Emails: {}".format(output['data']['emails']))

except Exception as Error:
    print(Error)
    
