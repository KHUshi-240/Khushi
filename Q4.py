import requests

url = "http://api.open-notify.org/iss-now.json"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

# Send a GET request to the API endpoint with headers
response = requests.get(url, headers=headers)

# Print the response object and the text content of the response
print(response)
print(response.text)

# Parse the JSON response
json_data = response.json()
