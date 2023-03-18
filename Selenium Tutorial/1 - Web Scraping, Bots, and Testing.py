# Selenium Tutorial #1
# https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.add_argument("start-maximized")
options.add_argument("disable-extensions")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# get website
driver.get("https://www.facebook.com")

# print website's title
title = driver.title
print(driver.title)

# print the first word of the title
print(title.split()[0])

driver.quit()
