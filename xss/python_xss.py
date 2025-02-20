import requests

# Take input from the user for the search term
search_term = input("Enter the search term: ")

#Construct URL with the search term
url = f"https://0a9600b004f6f6bc80e4f30f0020000e.web-security-academy.net/?search={search_term}"

# Make the GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request was successful!")
    # You can print the content of the response if needed
    print("Response content:")
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")
