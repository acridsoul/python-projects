#!/usr/bin/python3

import subprocess
import re

def valid_mac(mac):
    """Check if the MAC address is valid"""
    if re.fullmatch("^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", mac):
        return True
    else:
        return False
interface = input("Enter the interface: ")
mac_address = input("Enter the new MAC address: ")

if valid_mac(mac_address):
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.run(["ifconfig", interface, "up"])
    print(f"MAC address changed to {mac_address} on {interface}")
else:
    print("Invalid MAC address")

