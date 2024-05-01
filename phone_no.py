import requests

def validate_phone_number(api_key, phone_number):
    url = f"https://api.apilayer.com/number_verification/validate?number={phone_number}"
    headers = {'apikey': "yaYOLPNdTgxoAG0qWoGdHhnpwholWvbr"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'YOUR_API_KEY'
phone_number = input("Enter Target Mobile Number: ")

result = validate_phone_number(api_key, phone_number)
if result:
    print("Validation Result:", result)
