#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
import sys

def processIP(IP):
    IPNumbers = IP.split(".")
    if len(IPNumbers) != 4:
        exit(2)
    for i in range(len(IPNumbers)):
        IPNumbers[i] = dectobin(IPNumbers[i])
        if len(IPNumbers[i]) < 8:
            for j in range(8 - len(IPNumbers[i])):
                IPNumbers[i] = "0" + IPNumbers[i]

    return ".".join(IPNumbers)




def dectobin(x):
    try:
        x = int(x)
    except:
        print("ERROR: IP needs decimal characters")
        exit(1)


    bin = ""
    if not x:
        return str(x)
    while x != 0:
        bin = str(x % 2) + bin
        x = int(x / 2)

    return bin


def bintodec(x):
    counter = 0
    numxifra = len(x) - 1
    for c in x:
        if c == '0' or c == '1':
            c = int(c)
            counter = counter + c * 2 ** numxifra
            numxifra = numxifra - 1
        else:
            print("ERROR: bintodec needs binary characters")
            exit(1)
    return counter


# StdIn processing
'''
if not sys.stdin.isatty():
    y = sys.stdin.readlines()[0].split(" ")[0].rstrip("\n").lstrip("\n")
    y = bintodec(y)
    print(y)
    exit(0)
'''

# Argument processing for securing lenght of arguments for bintodec
if len(sys.argv) != 3:
    print("ERROR: bintodec needs 2 arguments")
    exit(1)

mask = sys.argv[2]
IP = sys.argv[1]


mask = processIP(mask)
IP = processIP(IP)
subnet = ""
for k in range(len(IP)):
    if IP[k] == ".":
        subnet += "."
    elif (int(IP[k]) * int(mask[k])) == 1:
        subnet += "1"
    elif (int(IP[k]) * int(mask[k])) == 0:
        subnet += "0"

decimalSubnet = ""
for i in range(4):
    decimalSubnet += "."
    decimalSubnet += str(bintodec(subnet[i * 8 + i: 8 * (i + 1) + i]))

decimalSubnet = decimalSubnet[1:]

print(decimalSubnet)


exit(0)
