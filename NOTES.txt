						Python notes:
File management:
	Open:
		with open(file_path, 'r') as file:
	Read lines of file:
		lines = file.readlines()
	Make list from lines: #strip newline characters
		my_list = [line.strip() for line in lines]
	Make tabel [line # : line string}:
		for line_number, line in enumerate(file, 1):
	
Keyword Search:
	if keyword.lower() in line.lower():
	
Command line input:
	import sys
	var1 = sys.argv[1]
	var2 = sys.argv[2]

Error Handling:
	if len(sys.argv) != 3:
    		print("Usage: python3 xxx.py [var1] [var2]")
    		sys.exit(1)
    	try:
    	except FileNotFoundError:
    	except httpx.RequestError as e:
  		print(f"Error fetching URL: {str(e)}")
	except Exception as e:
    		print(f"Error: {str(e)}")
	except httpx.HTTPError as e:
		print(f"Error fetching URL: {str(e)}")
Port Scan:
	import socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)
	result = sock.connect_ex((target, port)) #0 = open
	sock.close()

Cipher:
	ciph_map = {'A': 'cipher_key_for_a', 'B': 'cipher_key_for_b'}
	rev_ciph_map = {v: k for k, v in ciph_map.items()}
	Encrypt:
		''.join(ciph_map.get(c.upper(), c) for c in text)
	Decrypt:
		''.join(rev_ciph_map.get(c, c) for c in text)
		
Web Request
	import httpx (or import requests)
	url = 'https://www.website.com"
	headers = {'Content-Type': 'application/json'}
	data = {'a':0}
	req = httpx.post(url=url, headers=headers, json=data) #post, get, put, patch, head, options, delete
	print(req.text) #req.status_code
