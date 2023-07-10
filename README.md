# LinkedIn Profile Web Scraping

This repository provides a Python script for web scraping LinkedIn profiles. The script uses the Selenium library to automate web interactions and extract information from LinkedIn user profiles.

## Disclaimer

- This script is intended for educational and research purposes only.
- Web scraping LinkedIn or any other website may violate their terms of service or legal agreements. Use this script responsibly and at your own risk.
- Respect the privacy of others and do not use the scraped data for unauthorized purposes or in violation of applicable laws.
- Be aware that LinkedIn may change its website structure or policies at any time, which may break the functionality of this script.

## Prerequisites

To use this script, you need to have the following:

- Python 3.x installed on your machine.
- Selenium library installed. You can install it using `pip install selenium`.
- WebDriver installed for the browser you intend to use (e.g., ChromeDriver for Google Chrome). Make sure the WebDriver executable is in your system's PATH.

## Rotating Proxies

This script supports the use of rotating proxies to enhance scraping capabilities and mitigate IP blocking or rate limiting. To use rotating proxies, follow these steps:

1. Create a file named `valid_proxies.txt`.
2. Add different proxies, each on a new line, to the `valid_proxies.txt` file. The format should be `<proxy_ip>:<proxy_port>`.
3. Make sure the proxies in the file are valid and in working condition.
4. Update the script to include the proxy rotation logic using libraries like `requests` or `selenium-wire`. Refer to the specific library's documentation for implementation details.

## Usage

1. Clone the repository or download the script `linkedin_scraper.py`.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set up the necessary configuration in the script, including your LinkedIn username, password, and desired browser configuration.
4. Run the script using `python linkedin_scraper.py`.
5. The script will prompt for the LinkedIn profile URL you want to scrape. Provide the URL and press Enter.
6. The script will scrape the profile page, extract the desired information, and save it to a file or perform further processing as desired.

## Limitations

- Web scraping LinkedIn is subject to legal and ethical considerations. It is essential to review and comply with LinkedIn's terms of service and respect the privacy of individuals.
- LinkedIn has anti-scraping measures in place, including CAPTCHA challenges and account restrictions. Use this script responsibly and with caution to avoid any negative consequences.

## Contributing

Contributions to improve the script and add new features are welcome! If you find any issues or have suggestions, please feel free to open an issue or submit a pull request.


