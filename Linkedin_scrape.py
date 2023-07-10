from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import csv
import time
import unicodedata

# Path to chrome driver
PATH = "PATH TO CHROME DRIVER.exe"
username = 'your_email@email.com'
password = 'PASSWORD'
# Define the number of pages to scrape
num_pages = 1

def login(driver, username, password):
    # Load the LinkedIn login page
    driver.get('https://www.linkedin.com/login')

    # Enter your login credentials
    email_input = driver.find_element(By.ID, 'username')
    email_input.send_keys(username)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)

    # Submit the login form
    password_input.send_keys(Keys.ENTER)

    # Wait for the search bar element to be clickable
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@class, 'search-global-typeahead__input')]")))

def scrape_profiles(driver, num_pages):
    # Scrape data from each page
    scrape_info = []
    for page in range(num_pages):
        # Scroll to the end of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for the profile elements to load
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'entity-result__item')))

        # Extract the HTML content of the search results page
        html_content = driver.page_source

        # Create a BeautifulSoup object from the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the CEO profile elements
        profile_elements = soup.find_all('div', class_='entity-result__item')

        # Iterate over the profile elements and extract the desired information
        for profile_element in profile_elements:
            # Extract the name, headline, and location using appropriate locators
            name_element = profile_element.find('span', class_='entity-result__title-text t-16').find('span', attrs={'aria-hidden': 'true'})
            headline_element = profile_element.find('div', class_='entity-result__primary-subtitle t-14 t-black t-normal')
            location_element = profile_element.find('div', class_='entity-result__secondary-subtitle t-14 t-normal')

            # Extract the text from the elements and normalize the encoding
            name = name_element.get_text(strip=True) if name_element and name_element.get_text(strip=True) != "LinkedIn Member" else "Limited Visibility"
            headline = unicodedata.normalize('NFKD', headline_element.get_text(strip=True)) if headline_element else ""
            location = unicodedata.normalize('NFKD', location_element.get_text(strip=True)) if location_element else ""

            # Append the data to the list
            scrape_info.append({'Name': name, 'Headline': headline, 'Location': location})

        # Go to the next page if it is not the last page
        if page < num_pages - 1:
            next_button = driver.find_element(By.XPATH, "//button[@aria-label='Next']")
            next_button.click()
            time.sleep(5)  # Adjust sleep duration to allow the next page to load

    return scrape_info

def save_to_csv(data, csv_file):
    fieldnames = ['Name', 'Headline', 'Location']

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

        print(f"Scraped data saved to '{csv_file}'.")


# Rotating proxies
with open("valid_proxies.txt", "r") as f:
    proxies = f.read().split("\n")

counter = 0

for i in range(len(proxies)):
    try:
        print(f"Using the proxy: {proxies[counter]}")
        res = requests.get(i, proxies={"http": proxies[counter], "https": proxies[counter]})
        print(res.status_code)

    except:
        print("Failed")

    finally:
        counter += 1

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(PATH)

# Login to LinkedIn
login(driver, username, password)

# Wait for the search bar element to be clickable
wait = WebDriverWait(driver, 20)
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@class, 'search-global-typeahead__input')]")))

# Find the search bar and enter the search query
search_bar = driver.find_element(By.XPATH, "//input[contains(@class, 'search-global-typeahead__input')]")


# ---->SEARCH CRITERIA<---- 
search_bar.send_keys("---->SEARCH CRITERIA<----")
search_bar.send_keys(Keys.ENTER)

# Set the wait time in seconds
wait_time = 10

# Wait for the People button to be clickable
people_button = WebDriverWait(driver, wait_time).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='People']"))
)

# Click the People button
people_button.click()

time.sleep(5)

# Scrape profiles
scrape_info = scrape_profiles(driver, num_pages)

# Save the data in a CSV file
csv_file = 'scrape_info.csv'
save_to_csv(scrape_info, csv_file)

# Quit the WebDriver
driver.quit()

print(f"Scraped data saved to '{csv_file}'.")
