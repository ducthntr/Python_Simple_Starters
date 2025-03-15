import socket
import sys

def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()

if len(sys.argv) != 4:
    print("Usage: python3 portscanner.py [ip_address] [lowest_port] [highest_port]")
    print("Example: python3 portscanner.py 127.0.0.1 22 443")
    sys.exit(1)

target = sys.argv[1]
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])
scan_ports(target, start_port, end_port)                  
