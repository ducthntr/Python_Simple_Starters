import httpx

url = input("Enter the url (ex. http://www.google.com): ")
req = httpx.get(url)
req_text = req.text
print(req_text)
