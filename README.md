# Wayback-Urls

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**Wayback-Urls** is an OSINT (Open Source Intelligence) tool that leverages the
[Internet Archive's Wayback Machine](https://web.archive.org/) for URL reconnaissance.
Written in Python, it retrieves historical URLs associated with a target domain and
supports keyword/extension filtering, result limiting, automated screenshots, and
file export.

## Features

- 🔎 Pull every archived URL the Wayback Machine knows about for a domain
- 🎯 Filter results by file extension or keyword (`js`, `pdf`, `admin`, `login`, …)
- 🔢 Cap the number of results returned
- 📸 Optionally capture a screenshot of each URL (headless Firefox via Selenium)
- 💾 Print to the console or export to a file
- 🧯 Graceful error handling for timeouts, network failures, and empty results

## Prerequisites

- Python 3.7+
- [requests](https://pypi.org/project/requests/) — always required
- [selenium](https://pypi.org/project/selenium/) — **only** for the screenshot feature
- [Firefox](https://www.mozilla.org/firefox/) + [geckodriver](https://github.com/mozilla/geckodriver/releases) — **only** for the screenshot feature

> The tool runs fine with just `requests`. If you invoke `-s/--screenshot` without
> Selenium installed, it prints a helpful message and skips screenshots rather than crashing.

## Installation

```bash
git clone https://github.com/atraxsrc/wayback-Urls.git
cd wayback-Urls
pip install -r requirements.txt
```

For screenshots, make sure `geckodriver` is installed and available on your `$PATH`:

- **Ubuntu/Debian:** `sudo apt install firefox-geckodriver`
- **Arch:** `sudo pacman -S geckodriver`
- **Manual:** download from [github.com/mozilla/geckodriver](https://github.com/mozilla/geckodriver/releases)

## Usage

```bash
python3 waybackurls.py [-h] -d target.com [-k keyword] [-l limit] [-s] [-r seconds] [-o output]
```

### Options

| Flag | Long form      | Description                                              | Default    |
|------|----------------|----------------------------------------------------------|------------|
| `-h` | `--help`       | Show the help message and exit                           |            |
| `-d` | `--domain`     | Target domain (e.g., `target.com`)                       | *required* |
| `-k` | `--keyword`    | Filter by extension or keyword (e.g., `js`, `pdf`, `admin`, `login`) |            |
| `-l` | `--limit`      | Maximum number of URLs to return                         |            |
| `-s` | `--screenshot` | Take a screenshot of each URL found                      |            |
| `-r` | `--rate-limit` | Delay in seconds between screenshots                     | `1`        |
| `-o` | `--output`     | Save results to a file at the specified path             |            |

## Examples

Retrieve all archived URLs for a domain:

```bash
python3 waybackurls.py -d example.com
```

Filter for a specific file extension:

```bash
python3 waybackurls.py -d example.com -k js
```

Filter by keyword and limit results:

```bash
python3 waybackurls.py -d example.com -k login -l 100
```

Take screenshots with a 5-second delay between each:

```bash
python3 waybackurls.py -d example.com -s -r 5
```

Retrieve URLs and save to a file:

```bash
python3 waybackurls.py -d example.com -o urls.txt
```

Retrieve URLs, take screenshots, and save output:

```bash
python3 waybackurls.py -d example.com -s -r 2 -o urls.txt
```

## How it works

The tool queries the Wayback Machine's [CDX Server API](https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md),
requesting the original URLs for the target domain. Duplicate URL keys are collapsed
server-side, and the `-k` filter is applied as a regular expression against each
archived URL.

## Screenshots

When `-s` is used, screenshots are saved to a `screens/` directory inside the project
folder (created automatically if it doesn't exist). Files are named `screen-<number>.png`
sequentially in the order URLs are processed.

## Output

By default, retrieved URLs are printed to the console with a count summary. Use `-o` to
save them to a file instead. If no URLs match the given domain or keyword, the tool
prints a warning and exits cleanly.

## Disclaimer

This tool is intended for **authorized security testing, research, and educational
purposes only**. Only use it against domains you own or have explicit permission to
assess. You are solely responsible for complying with all applicable laws and the
Internet Archive's terms of service. The authors assume no liability for misuse.

## Contributing

Contributions are welcome! If you have ideas, improvements, or bug fixes, please open
an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
