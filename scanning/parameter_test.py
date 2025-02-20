import httpx

def read_list_from_file(file_path):
    """Reads a file and returns its content as a list, 
    splitting each line into a separate element.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # Remove newline characters from each line
            my_list = [line.strip() for line in lines]
        return my_list
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

# Example usage:
file_path = 'parameters.list'  # Replace with the actual path to your file
my_list = read_list_from_file(file_path)

if my_list:
    for item in my_list:
        url = f"https://0ad300df04bf81b08065dab500c100e1.web-security-academy.net/api/{item}/"
        headers = {'Cookie': 'session=XGJt4O7xenf5fKl0zVPm6ltR031SzWp8'}
        req = httpx.get(url, headers=headers)
        req_text = req.status_code
        print(url)
        print(req_text)
