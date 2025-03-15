import sys

def keyword_search(filename, keyword):
    print(f"\n***Beginning search for {keyword}.***")
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, 1):
                if keyword.lower() in line.lower():
                    print(f"Line {line_number}: {line.strip()}")
        print("***Search complete.***")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if len(sys.argv) != 3:
    print("Usage: python3 keyword_search.py [filename] [keyword]")
    sys.exit(1)

filename = sys.argv[1]
keyword = sys.argv[2]

keyword_search(filename, keyword)
