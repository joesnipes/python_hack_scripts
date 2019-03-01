#!usr/bin/env python

import scapy.all as scapy
from scapy_http import http


def sniff(interface):
    scapy.sniff(iface= interface, store= False, prn= process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(str(packet, 'utf8'))

sniff("en0")