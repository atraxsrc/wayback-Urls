# Wayback-Urls

Wayback-Urls is an OSINT (Open Source Intelligence) tool leveraging the Wayback Machine for URL reconnaissance. Built with Python, it retrieves historical URLs associated with a target domain with support for keyword filtering, result limiting, screenshots, and file export.

## Prerequisites

- Python 3.7+
- [requests](https://pypi.org/project/requests/)
- [selenium](https://pypi.org/project/selenium/)
- [Firefox](https://www.mozilla.org/firefox/) + [geckodriver](https://github.com/mozilla/geckodriver/releases) *(only required for screenshot functionality)*

## Installation
```bash
git clone https://github.com/atraxsrc/wayback-Urls.git
cd wayback-Urls
pip install -r requirements.txt
```

> For screenshots, make sure `geckodriver` is installed and available in your `$PATH`.
> On Ubuntu/Debian: `sudo apt install firefox-geckodriver`
> On Arch: `sudo pacman -S geckodriver`
> Or download manually from [github.com/mozilla/geckodriver](https://github.com/mozilla/geckodriver/releases)

## Usage
```bash
python3 waybackurls.py [-h] -d target.com [-k keyword] [-l limit] [-s] [-r seconds] [-o output]
```

## Options

| Flag | Long form | Description | Default |
|------|-----------|-------------|---------|
| `-h` | `--help` | Show help message | |
| `-d` | `--domain` | Target domain (e.g., `target.com`) | *required* |
| `-k` | `--keyword` | Filter by extension or keyword (e.g., `js`, `pdf`, `admin`, `login`) | |
| `-l` | `--limit` | Maximum number of URLs to return | |
| `-s` | `--screenshot` | Take a screenshot of each URL found | |
| `-r` | `--rate-limit` | Delay in seconds between screenshots | `1` |
| `-o` | `--output` | Save results to a file at the specified path | |

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

## Screenshots

When the `-s` flag is used, screenshots are saved to the `screens/` directory inside the project folder (created automatically if it doesn't exist). Files are named `screen-<number>.png` sequentially.

## Output

By default, retrieved URLs are printed to the console with a count summary. Use `-o` to save results to a file instead.

If no URLs are found for the given domain or keyword, the tool will display a warning and exit cleanly.

## Contributing

Contributions are welcome! If you have ideas, improvements, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
