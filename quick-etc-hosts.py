#!/usr/bin/env python
# Tired of adding hosts over and over in CTF games or doing other things?
# Run this (as sudo) for a more convenient /etc/hosts experience

import re

# for validating an Ip-address & subdomain name
# hostRegex supports infinite subdomains
IPregex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
hostRegex = "^(((?!\-))(xn\-\-)?[a-z0-9\-_]{0,61}[a-z0-9]{1,1}\.)*(xn\-\-)?([a-z0-9\-]{1,61}|[a-z0-9\-]{1,30})\.[a-z]{2,}$"

# loop until IP provided is valid
try:
    while True:
        Ip = str(input("Enter the IP address of the host you want to add: "))

        if re.search(IPregex, Ip):
            while True: # loop until Domain name provided is valid
                hst = input("Enter the hostname: ")
                if re.search(hostRegex, hst):            
                    with open("/etc/hosts", "a") as file:
                        file.write("\n" + Ip)
                        file.write("    " + hst)
                        print(f"{hst} was added with IP {Ip}.")
                    break
                else:
                    print(f"The host name '{hst}' is not valid, please enter a correct one")                
            break
        else:
            print(f"The IP address {Ip} is not valid, please enter a correct one")
except PermissionError:
    print("Permission error, are you authorized to run this?")
except KeyboardInterrupt:
    exit