import json
import socket
import whois
import re
import requests
from bs4 import BeautifulSoup

def get_ip(domain):
    
    #IP adresini bulur.

    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return "IP address is not found"

def get_whois_info(domain):
    
    #WHOIS bilgisini getirir.
    
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return f"Whois query failed: {e}"

def scan_ports(ip):
    
    #Önemli portları tarar.
    
    open_ports = []
    ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 143, 443, 8080, 3389] 

    for port in ports_to_scan:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def rdp_info(ip):
    # RDP servisini kontrol eder ve bilgi döndürür.
    port = 3389
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    if result == 0:
        return f"RDP service is running on {ip}:{port}"
    else:
        return f"RDP service is not running on {ip}:{port}"

def google_search(domain):
   
    #Excel linkleri için google araması
    
    query = f"site:{domain} filetype:xls OR filetype:xlsx"
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url)
    links = re.findall(r'<a href="\/url\?q=(.*?)&amp;', response.text)
    return links

def get_site_links(domain):
    
    #Verilen domain ile ilgili linkleri getirir.
    
    links = []
    try:
        response = requests.get(f'http://{domain}')
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            if domain in href or href.startswith('/'):
                links.append(href)
    except Exception as e:
        links.append(f"Failed to retrieve site links: {e}")
    return links

def main(domain):
    ip = get_ip(domain)
    whois_info = get_whois_info(domain)
    open_ports = scan_ports(ip)
    rdp_info_result = rdp_info(ip)
    excel_links = google_search(domain)
    site_links = get_site_links(domain)

    with open('output.txt', 'w') as f:
        f.write(f"Domain: {domain}\n")
        f.write(f"IP Address: {ip}\n\n")
        f.write("Whois Info:\n")
        f.write(json.dumps(whois_info, default=str, indent=4) + "\n\n")
        f.write("Open Ports:\n")
        f.write(", ".join(map(str, open_ports)) + "\n\n")
        f.write("RDP Info:\n")
        f.write(rdp_info_result + "\n\n")
        f.write("Google Excel Links:\n")
        for link in excel_links:
            f.write(link + "\n")
        f.write("\nSite Links:\n")
        for link in site_links:
            f.write(link + "\n")

if __name__ == "__main__":
    domain = input("Please enter a domain: ")
    main(domain)