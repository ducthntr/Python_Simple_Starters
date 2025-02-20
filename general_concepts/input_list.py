import sys

if len(sys.argv) < 2:
    print("Usage: python3 file.py list.list")
    exit()

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
file_path = f'{sys.argv[1]}'
my_list = read_list_from_file(file_path)
num = 1
if my_list:
    for item in my_list:        
        print(str(num) + " " + item)
        num += 1


