from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

class Gokul:
    url = 'http://www.google.com'
    
    def __init__(self):
        # Set Firefox options to run in headless mode
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        
        # Initialize the Firefox driver with the headless option
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

    def browse(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def get_title(self):
        return self.driver.title

    def close_browser(self):
        self.driver.quit()

s = Gokul()
s.browse()
print(s.get_title())

# Make sure to close the browser when you are done
s.close_browser()
