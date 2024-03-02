import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton
from input_dialog import InputDialog

def main():

    # Create a QApplication instance
    app = QApplication([])

    # Ask the user for a list of guitars
    guitars = []
    dialog = InputDialog()
    dialog.add_another.connect(guitars.append)
    dialog.add_many.connect(lambda g: (guitars.extend(g), dialog.close(), start_search(guitars)))  # close dialog and start search when add_many is emitted
    dialog.exec_()

def start_search(guitars):
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # Create a new instance of the Chrome driver
    s=Service('./chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=chrome_options)

    # Open the website
    driver.get("https://www.musiciansfriend.com/")
    driver.maximize_window()

    # Lists to keep track of which guitars were found and which were not
    found_guitars = []
    not_found_guitars = []

    # Search for each guitar
    for guitar in guitars:
        # Wait for the search bar element to be visible and then interact with it
        wait = WebDriverWait(driver, 10)  # wait for up to 10 seconds
        search_bar = wait.until(EC.visibility_of_element_located((By.ID, "searchTerm")))

        # Clear the search bar
        search_bar.clear()

        # Click on the search bar
        search_bar.click()

        # Enter the guitar name in the search bar and press Enter
        search_bar.send_keys(guitar)
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
        time.sleep(5)

        # Look for the guitar in the search results
        try:
            search_result = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, f"//a[contains(translate(@href, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{guitar.replace(' ', '-').lower()}') and contains(text(), '{guitar}')]"))
            )
            found_guitars.append(guitar)
        except TimeoutException:
            not_found_guitars.append(guitar)

    # Print the lists of found and not found guitars
    print("Found guitars:")
    for guitar in found_guitars:
        print(guitar)

    print("\nNot found guitars:")
    for guitar in not_found_guitars:
        print(guitar)

    # selenium-browser-testing.py
    from result_dialog import ResultDialog

    # After the search is done
    result_dialog = ResultDialog(found_guitars, not_found_guitars)
    result_dialog.exec_()

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()