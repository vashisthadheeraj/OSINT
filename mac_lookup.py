import requests
mac = input("Enter the MAC Address to scan: ")




try:
    headers = {'Accept': 'application/json'}
    url = f"https://api.viewdns.info/maclookup/?mac={mac}&apikey=07248da53fca892b72bbf178289c86250076cedf&output=json"
    response = requests.get(url)
    output = response.json()
    print(output)
    # print("[+] Status: {}".format(output['data']['status']))
    # print("[+] Email: {}".format(output['data']['email']))
    # print("[*] Score: {}".format(output['data']['score']))
    # print("[*] Disposable: {}".format(output['data']['disposable']))
    # print("[*] Webmail: {}".format(output['data']['webmail']))
    # print("[*] MX Records: {}".format(output['data']['mx_records']))
    # print("[*] SMTP Server: {}".format(output['data']['smtp_server']))
    # print("[*] Blacklisted: {}".format(output['data']['block']))

except Exception as Error:
    print(Error)
