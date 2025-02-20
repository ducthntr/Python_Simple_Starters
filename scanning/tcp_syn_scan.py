from scapy.all import *

def syn_scan(target_ip, port_range):
    for port in port_range:
        packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
        response = sr1(packet, timeout=1, verbose=0)
        if response is None:
            print(f"Port {port} is filtered")
        elif response.haslayer(TCP):
            if response[TCP].flags == "SA":
                print(f"Port {port} is open")
            elif response[TCP].flags == "RA":
                print(f"Port {port} is closed")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    ports_low = input("Enter the lowest port you wish to scan (default: 1): ") or 1
    ports_high = input("Enter the highest port you wish to scan (default: 65535): ") or 65535
    port_range = range(int(ports_low), int(ports_high))
    syn_scan(target_ip, port_range)
