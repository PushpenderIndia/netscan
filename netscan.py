#!/usr/bin/env python

import pyfiglet
import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description='NetScan v1.0')
    parser._optionals.title = "Optional Arguments"

    required_arguments = parser.add_argument_group('Required Arguments')
    required_arguments.add_argument("-t", "--target", dest="target", help="Target's IP Address/IP Range.", required=True)
    return parser.parse_args()

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    clients_list = []
    for element in answered_list:
        clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list
    
def print_result(results_list):
    print(33*"_")
    print("IP Address\tMAC Address\n" + 33*"-")
    for client in results_list:
        print(client["ip"] + "\t" + client["mac"])
    print()    
    print(33*"-")    
    print(f"[*] Total Target Found: {len(results_list)}")
    print(33*"-") 

ascii_banner = pyfiglet.figlet_format("NetScan")
print(ascii_banner)
print(" is a Network Reconnaissance tool!\n")
print(50*"-")
print("  Author: Pushpender | Website: technowlogy.tk")
print(50*"-","\n")

arguments = get_arguments()
scan_result = scan(arguments.target) 
print_result(scan_result)       