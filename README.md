# guitar-search-with-selenium

This project uses Selenium WebDriver with Python to automate browser actions. It specifically searches for a list of guitars on the website "https://www.musiciansfriend.com/".

**Features**

- User input for guitar names through a PyQt5 dialog box.
- Automated search for each guitar on the website.
- Automated handling of pop-up windows on the website.
- Display of search results, showing which guitars were found and which were not.

**Requirements**

- Python 3.6+
- Selenium WebDriver
- ChromeDriver
- PyQt5

**Usage**

1. Run the main.py script.
2. A dialog box will appear.
3. Enter the names of the guitars you want to search for, and click the "Import" button when you're done.
4. The script will automatically search for each guitar on the website and handle any pop-up windows that appear.
5. After the search is complete, a dialog box will appear showing which guitars were found and which were not.

**Notes**

1. This script uses the Chrome WebDriver, so you'll need to have Google Chrome installed on your machine.
2. Make sure that the version of ChromeDriver you're using is compatible with your version of Google Chrome.
