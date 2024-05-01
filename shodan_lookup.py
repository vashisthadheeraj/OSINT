import requests

def shodan_lookup(api_key, query):
    try:
        # Shodan API base URL
        url = f"https://api.shodan.io/shodan/host/search?key={api_key}&query={query}"

        # Make the HTTP GET request
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            # Print the total number of results
            print(f"Total results found: {data['total']}")
            # Print each result
            for match in data['matches']:
                print(match)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    api_key = "QGyIxPZOK0m0vKgI7TqNFGMziQxvrE13"
    query = input("Enter your search query: ")
    shodan_lookup(api_key, query)
