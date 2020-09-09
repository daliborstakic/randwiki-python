from selenium import webdriver
""" Simulating keyboard shortcuts """
from selenium.webdriver.common.keys import Keys

# Webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe" # Path
driver = webdriver.Chrome(PATH)

# Loading the page
driver.get("https://en.wikipedia.org/wiki/Main_Page")
html_page = driver.find_element_by_xpath('html')

def gen_rand():
    """ Generates a random Wiki page """
    html_page = driver.find_element_by_xpath('html')
    html_page.send_keys(Keys.ALT, Keys.SHIFT, 'x')
