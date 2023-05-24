import requests
import json

url = "http://127.0.0.1:8000/hotels/anambra/4999?skip=0&limit=100"

def formatted_print(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get(f"{url}")
if response.status_code == 200:
    print("sucessfully fetched the data")
    formatted_print(response.json())
else:
    print(f"Hello person, there's a {response.status_code} error with your request")


