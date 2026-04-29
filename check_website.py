import requests

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            print(f"{url} is UP ")
        else:
            print(f"{url} is DOWN (Status Code: {response.status_code})")
    
    except requests.exceptions.RequestException as e:
        print(f"{url} is DOWN (Error: {e})")

website = "https://www.google.com"
check_website(website)