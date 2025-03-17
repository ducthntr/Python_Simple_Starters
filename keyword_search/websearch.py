import sys
import httpx

def keyword_search(content, keyword):
    print(f"\n***Beginning search for {keyword}.***")
    try:
        lines = content.splitlines()
        found = False
        for line_number, line in enumerate(lines, 1):
            if keyword.lower() in line.lower():
                print(f"Line {line_number}: {line.strip()}")
                found = True

        if not found:
            print(f"Keyword '{keyword}' not found")
        print("***Search complete.***")

    except Exception as e:
        print(f"Error during search: {str(e)}")

if len(sys.argv) != 3:
    print("Usage: python3 keyword_search.py [url] [keyword]")
    print("Example: python3 keyword_search.py http://www.google.com google")
    sys.exit(1)

try:
    url = sys.argv[1]
    keyword = sys.argv[2]

    print(f"Fetching {url}...")
    req = httpx.get(url)
    content = req.text
    print(req.status_code)
    keyword_search(content, keyword)

except httpx.RequestError as e:
    print(f"Error fetching URL: {str(e)}")
except Exception as e:
    print(f"Error: {str(e)}")
