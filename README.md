# Wayback-Urls
WaybackMachine's OSINT tool for url recon using Python

## Prerequisites:
- requests
- selenium

## Install:
```git
git clone https://github.com/atraxsrc/wayback-Urls.git
cd wayback-Urls 
python3 waybackurls.py

```
## Usage:
```python
python3 waybackurls.py [-h] -d target.xyz [-k keyword] [-l limit] [-s] [-r] [-o output]
```
## options:
```
  -h          show this help message and exit
  -d          target domain (exp: target.com)
  -k          search a specific extension or keyword (js, xml, json, pdf, css... or admin, login...)
  -l          limit (number of links)
  -s          screenshot of each url found
  -r          delay between screenshots
  -o          output file to your choosen path
```
