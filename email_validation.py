import requests
email = input("Enter your Email: ")

try:
    headers = {'Accept': 'application/json'}
    url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key=d3ddf041687d499b05a2c6cbd15b3be6e9236b9b"
    response = requests.get(url)
    output = response.json()
    print("[+] Status: {}".format(output['data']['status']))
    print("[+] Email: {}".format(output['data']['email']))
    print("[*] Score: {}".format(output['data']['score']))
    print("[*] Disposable: {}".format(output['data']['disposable']))
    print("[*] Webmail: {}".format(output['data']['webmail']))
    print("[*] MX Records: {}".format(output['data']['mx_records']))
    print("[*] SMTP Server: {}".format(output['data']['smtp_server']))
    print("[*] Blacklisted: {}".format(output['data']['block']))

except Exception as Error:
    print(Error)
    
