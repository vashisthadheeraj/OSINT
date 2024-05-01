import requests

def open_shortlink(shortlink):
    response = requests.get(shortlink, allow_redirects=True)
    
    if response.status_code == 200:
        print("Shortlink opened successfully!")
        print("Redirected URL:", response.url)
    else:
        print(f"Error: {response.status_code}")

# Replace 'YOUR_SHORTLINK_URL' with the actual shortlink URL you want to open
shortlink = input("Enter your Short URL: ")

open_shortlink(shortlink)
