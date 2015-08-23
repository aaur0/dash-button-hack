from scapy.all import *
import requests
import time


#import logging
#logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scanner import record

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      if pkt[ARP].hwsrc == '74:c2:46:e0:9f:1f': # Huggies Button
        print "fish feeding done"
        event_time = time.strftime("%Y-%m-%d %H:%M:%S")
        event_name = "fed the fish."
        event_record = [event_time, event_name]
        record(event_record)
      else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

if __name__ == '__main__':
    while(True):
        try:
            print sniff(prn=arp_display, filter="arp", store=0, count=10)
        except Exception , e:
            print str(e)

