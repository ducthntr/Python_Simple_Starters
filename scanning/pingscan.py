from scapy.all import srp, Ether, ARP

def arp_ping_scan(subnet):
    # Create ARP packet
    arp = ARP(pdst=subnet)

    # Create Ethernet frame
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC address

    # Combine Ethernet frame and ARP packet
    packet = ether/arp

    # Send and receive ARP requests using srp function
    result = srp(packet, timeout=3, verbose=False)[0]

    # Parse results
    devices = []
    for sent, received in result:
        # For each response, append IP and MAC address to the devices list
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

if __name__ == "__main__":
    subnet = "10.230.216.0/21"  # Example subnet, change it according to your needs
    devices = arp_ping_scan(subnet)
    print("Devices found in subnet:")
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}")
