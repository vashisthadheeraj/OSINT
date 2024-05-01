import requests

def find_subdomains(domain):
    subdomains = set()

    # Censys API
    censys_api_url = f"https://censys.io/api/v1/search/ipv4"
    censys_params = {"query": f"parsed.names: *.{domain}"}
    censys_headers = {"Content-Type": "application/json"}
    censys_response = requests.post(censys_api_url, json=censys_params, headers=censys_headers)
    if censys_response.status_code == 200:
        censys_data = censys_response.json()
        for result in censys_data['results']:
            subdomains.add(result['parsed.names'][0])

    # VirusTotal API
    virustotal_api_url = f"https://www.virustotal.com/api/v3/domains/{domain}/subdomains"
    virustotal_headers = {"x-apikey": "7fcced260497a1a234a9a838d691017103713d770f3a40218cc34a522fb2c149"}
    virustotal_response = requests.get(virustotal_api_url, headers=virustotal_headers)
    if virustotal_response.status_code == 200:
        virustotal_data = virustotal_response.json()
        for subdomain_data in virustotal_data['data']:
            subdomains.add(subdomain_data['id'])

    # Shodan API
    shodan_api_key = "QGyIxPZOK0m0vKgI7TqNFGMziQxvrE13"
    shodan_api_url = f"https://api.shodan.io/shodan/domain/{domain}?key={shodan_api_key}"
    shodan_response = requests.get(shodan_api_url)
    if shodan_response.status_code == 200:
        shodan_data = shodan_response.json()
        for subdomain in shodan_data:
            subdomains.add(subdomain)

    return subdomains

if __name__ == "__main__":
    domain = input("Enter the domain name to find subdomains: ")
    subdomains = find_subdomains(domain)
    print(f"Subdomains for {domain}:")
    for subdomain in subdomains:
        print(subdomain)
