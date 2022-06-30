# Wayback-Urls
WaybackMachine's OSINT tool for url recon using Python

## Prerequisites:

- requests
- selenium

## Install:
```bash
$ git clone https://github.com/atraxsrc/waybackurls

$ cd waybackurls

$ python3 waybackurls.py
```
## Usage:
```bash
./waybackurls.py [-h] -d target.xyz [-k keyword] [-l limit] [-s] [-r] [-o output]
```
Can be use with other tools for more efficient results


## options:
```bash
  -h, --help  show this help message and exit
  
  -d          target domain (exp: target.com)
  
  -k          search for a specific extension or keyword (js, xml, json, pdf... or admin, login, dashboard...)
  
  -l          limit (number of links you want)
  
  -s          take screenshot of each url found
  
  -r          delay between two screenshots
  
  -o          Output file name
```
  

