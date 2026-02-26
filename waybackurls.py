#!/usr/bin/env python3

import requests
import argparse
import os
import sys
from time import sleep

ASCII_ART = '''
             |
       Atrax |
             |
         /   |   \\
         \\   |   /
       .  --\\|/--  ,
        '--|___|--'
        ,--|___|--,
       '  /\\o o/\\  `
         +   +   +
          `     ' 
'''

class TerminalColors:
    OK      = '\033[92m'
    WARNING = '\033[93m'
    FAIL    = '\033[91m'
    RESET   = '\033[0m'
    INFO    = '\033[94m'

WAYBACK_API_URL = (
    "https://web.archive.org/cdx/search/cdx"
    "?matchType=domain&collapse=urlkey&output=text&fl=original"
)
SCREENSHOT_FOLDER = "screens"


def setup_arg_parser():
    parser = argparse.ArgumentParser(
        description="Fetch archived URLs for a domain from the Wayback Machine."
    )
    parser.add_argument("-d", "--domain",      help="Target domain (e.g., target.com)", type=str, required=True)
    parser.add_argument("-k", "--keyword",     help="Filter by extension or keyword (e.g., js, pdf, admin)", type=str)
    parser.add_argument("-l", "--limit",       help="Max number of URLs to return", type=int)
    parser.add_argument("-s", "--screenshot",  help="Take a screenshot of each URL", action="store_true")
    parser.add_argument("-r", "--rate-limit",  help="Delay between screenshots in seconds (default: 1)", type=float, default=1)
    parser.add_argument("-o", "--output",      help="Save results to this file", type=str)
    return parser


def take_screenshots(url_list, rate_limit):
    """Take screenshots of the provided URLs using Selenium + Firefox headless."""
    try:
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options
    except ImportError:
        print(TerminalColors.FAIL + "[!] Selenium not installed. Run: pip install selenium" + TerminalColors.RESET)
        return

    os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)

    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout(30)

    print(TerminalColors.OK + f"[+] Taking screenshots of {len(url_list)} URLs..." + TerminalColors.RESET)

    for i, url in enumerate(url_list, start=1):
        try:
            driver.get(url)
            sleep(rate_limit)
            screenshot_path = os.path.join(SCREENSHOT_FOLDER, f"screen-{i}.png")
            driver.save_screenshot(screenshot_path)
            print(f"  [{i}] Saved: {screenshot_path}")
        except Exception as e:
            print(TerminalColors.WARNING + f"  [{i}] Failed ({url}): {e}" + TerminalColors.RESET)

    driver.quit()
    print(TerminalColors.OK + "[+] Screenshots complete." + TerminalColors.RESET)


def fetch_urls(domain, keyword=None, limit=None):
    """Fetch archived URLs from the Wayback Machine CDX API."""
    url = f"{WAYBACK_API_URL}&url={domain}/*"

    if keyword:
        # Filter URLs containing the keyword/extension in the original URL
        url += f"&filter=original:.*\\.{keyword}(\\?.*)?$"

    if limit:
        url += f"&limit={limit}"

    print(TerminalColors.INFO + f"[*] Querying: {url}" + TerminalColors.RESET)

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print(TerminalColors.FAIL + "[!] Request timed out. The Wayback Machine may be slow — try again." + TerminalColors.RESET)
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(TerminalColors.FAIL + f"[!] HTTP error: {e}" + TerminalColors.RESET)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(TerminalColors.FAIL + f"[!] Network error: {e}" + TerminalColors.RESET)
        sys.exit(1)

    text = response.text.strip()

    if not text:
        print(TerminalColors.WARNING + "[!] No URLs found. Try a different domain or keyword." + TerminalColors.RESET)
        return []

    return text.splitlines()


def main():
    print(ASCII_ART)
    parser = setup_arg_parser()
    args = parser.parse_args()

    urls = fetch_urls(args.domain, args.keyword, args.limit)

    if not urls:
        sys.exit(0)

    print(TerminalColors.OK + f"[+] Found {len(urls)} URL(s)." + TerminalColors.RESET)

    if args.screenshot:
        take_screenshots(urls, args.rate_limit)

    output_text = "\n".join(urls)

    if args.output:
        try:
            with open(args.output, "w") as f:
                f.write(output_text + "\n")
            print(TerminalColors.OK + f"[+] Results saved to: {args.output}" + TerminalColors.RESET)
        except IOError as e:
            print(TerminalColors.FAIL + f"[!] Could not write to file: {e}" + TerminalColors.RESET)
            sys.exit(1)
    else:
        print(output_text)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + TerminalColors.FAIL + "[!] Cancelled by user." + TerminalColors.RESET)
        sys.exit(0)
