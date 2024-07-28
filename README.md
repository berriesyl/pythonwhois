README

Domain Analysis Script

This repository contains a Python script designed to perform a comprehensive analysis of a given domain. The script retrieves various information including the domain's IP address, WHOIS data, open ports, RDP service status, and finds Excel files linked to the domain on Google. Additionally, it scrapes and lists all links found on the domain's homepage.

Features

- IP Address Retrieval: Fetches the IP address associated with the domain.
- WHOIS Information: Retrieves WHOIS data for the domain, including registration details.
- Port Scanning: Scans common ports to check if they are open.
- RDP Service Check: Checks if the Remote Desktop Protocol (RDP) service is running.
- Google Search for Excel Files: Searches for Excel files linked to the domain using Google.
- Site Link Extraction: Scrapes the homepage of the domain to list all internal and relevant links.

Prerequisites

Ensure you have the following Python libraries installed:

```bash
pip install socket
pip install python-whois
pip install requests
pip install beautifulsoup4
```

Usage

1. Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/domain-analysis-script.git
   cd domain-analysis-script
   ```

2. Run the script**:

   ```bash
   python domain_analysis.py
   ```

3. Input the domain** when prompted.

4. View the results** in the `output.txt` file generated in the same directory.

Example Outputs

google.com

```
Domain: google.com
IP Address: 142.251.140.14

Whois Info:
{
    "domain_name": ["GOOGLE.COM", "google.com"],
    "registrar": "MarkMonitor, Inc.",
    ...
}

Open Ports:
21, 80, 443

RDP Info:
RDP service is not running on 142.251.140.14:3389

Google Excel Links:
https://maps.google.com/maps%3Fq%3Dsite:google.com%2Bfiletype:xls%2BOR%2Bfiletype:xlsx%26um%3D1%26ie%3DUTF-8%26ved%3D1t:200713%26ictx%3D111
https://www.google.com/help/hc/downloads/richmedia/rich_media_spec_collection_template.xls

Site Links:
https://www.google.com/imghp?hl=tr&tab=wi
http://maps.google.com.tr/maps?hl=tr&tab=wl
...
```

Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue to discuss improvements or bug fixes.

License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Acknowledgements

- [python-whois](https://pypi.org/project/python-whois/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests](https://docs.python-requests.org/en/master/)
- [Socket](https://docs.python.org/3/library/socket.html)
