import httpx

url = input("Enter the url (ex. http://www.google.com): ")
req = httpx.get(url)
headers = req.headers
print(headers)
