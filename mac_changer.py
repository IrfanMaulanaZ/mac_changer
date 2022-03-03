#!/usr/bin/env python
import subprocess

interface = input("[+] Interface EX:(wlan0) > ")
new_mac = input("[+] Enter MAC EX:(00:11:22:33:44:55) > ")

print("{+} Changging MAC address for " + interface + " to " + new_mac)

subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["sudo", "ifconfig", interface, "up"])
print()
subprocess.call("ifconfig " + interface, shell=True)
