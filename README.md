# Wayback-Urls

Wayback-Urls is an OSINT (Open Source Intelligence) tool leveraging the Wayback Machine for URL reconnaissance. It's built using Python and allows users to retrieve historical URLs associated with a specific domain. The tool also offers functionalities such as keyword filtering, limiting the number of results, taking screenshots of retrieved URLs, and exporting results.

## Prerequisites
- Python 3
- requests
- selenium
- Firefox WebDriver (for screenshot functionality)

## Installation

```bash
git clone https://github.com/atraxsrc/wayback-Urls.git
cd wayback-Urls
pip install -r requirements.txt

```
## Usage:
```python
python3 waybackurls.py [-h] -d target.xyz [-k keyword] [-l limit] [-s] [-r] [-o output]
```
## options:
```
  -h          show this help message
  -d          target domain (exp: target.com)
  -k          search a specific extension or keyword (js, xml, json, pdf, css... or admin, login...)
  -l          limit (number of links)
  -s          screenshot of each url found
  -r          delay between screenshots
  -o          output file to your choosen path
```
## Examples

- Retrieve URLs for a specific domain:
```python
python3 waybackurls.py -d example.com
```
- Retrieve URLs and take screenshots with a 5-second delay:
```python
python3 waybackurls.py -d example.com -s -r 5
```
- Filter results for a specific keyword and limit the output:
```python
python3 waybackurls.py -d example.com -k login -l 100
```
