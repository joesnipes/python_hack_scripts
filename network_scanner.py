#!/usr/bin/python

import scapy.all as scapy
import optparse

def get_args():
    parser = optparse.OptionParser()
    parser.add_option('--t', '--target',dest='ip_range', help='IP Range to scan')
    (options, arguments)=parser.parse_args()
    if not options.ip_range:
        parser.error('[-] Please enter an IP range Ex. 192.168.1.1/24')
    return(options)

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose = False)[0]

    client_list = []
    for a in answered_list:
        client_dict = {'ip': a[1].psrc, 'mac': a[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(results_list):
    print('IP Address\t\t\tMAC Address\n*****************************************************')
    for client in results_list:
        print(client["ip"] + '\t\t\t' + client["mac"])

options = get_args()
scan_results = scan(options.ip_range)
print_result(scan_results)