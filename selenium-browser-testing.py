from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=Service('path/to/chromedriver'), options=chrome_options)

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