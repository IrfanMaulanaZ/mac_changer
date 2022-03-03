#!/usr/bin/env python
# This code is simple and easy to use because I'm new in python :)

import subprocess

interface = input("[+] Interface EX:(wlan0) > ")
new_mac = input("[+] Enter MAC EX:(00:11:22:33:44:55) > ")

print("{+} Changging MAC address for " + interface + " to " + new_mac)

subprocess.call("sudo ifconfig " + interface + " down", shell=True)
subprocess.call("sudo ifconfig " + interface +" hw ether " + new_mac, shell=True)
subprocess.call("sudo ifconfig " + interface + " up", shell=True)
print("Succesfully changing MAC address...")
