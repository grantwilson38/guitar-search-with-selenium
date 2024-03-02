from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Ask the user for a list of guitars
guitars = []
while True:
    guitar = input("Enter a guitar you are looking for, or 'done' to finish: ")
    if guitar.lower() == 'done':
        break
    guitars.append(guitar)

# Now, the list 'guitars' contains the guitars the user is looking for

# Setup Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Create a new instance of the Chrome driver
s=Service('./chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrome_options)

# Open the website
driver.get("https://www.musiciansfriend.com/")
driver.maximize_window()
# Wait for the search bar element to be visible and then interact with it
wait = WebDriverWait(driver, 10)  # wait for up to 10 seconds
search_bar = wait.until(EC.visibility_of_element_located((By.ID, "searchTerm")))

# Click on the search bar
search_bar.click()

# Enter "yamaha guitar" in the search bar and press Enter
search_bar.send_keys("yamaha guitar")
search_bar.send_keys(Keys.RETURN)

# Wait for the pop-up window to appear
try:
    decline_offer_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Decline Offer; close the dialog']"))
    )
    # Click on the decline offer button
    decline_offer_button.click()
except TimeoutException:
    # If the pop-up window does not appear within 10 seconds, ignore it
    pass

# Wait for the search results to load
# Look for any Yamaha guitars with F335 in their name
try:
    f335_guitar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/guitars/yamaha-f335-acoustic-guitar')]"))
    )
    print("Found Yamaha F335 guitar")
except TimeoutException:
    print("Yamaha F335 guitar not found")