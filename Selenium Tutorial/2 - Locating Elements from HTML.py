"""Selenium Tutorial #1
https://sites.google.com/a/chromium.org/chromedriver/downloads"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

website = "https://www.techwithtim.net"


'''Starts Chrome maximized.'''
options = Options()
options.add_argument("start-maximized")


'''Disables Chrome extensions.'''
options.add_argument("disable-extensions")


'''Locates ChromeDriver file.'''
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

'''Gets website.'''
driver.get(website)


'''Prints website title.'''
title = driver.title
print(driver.title)


'''Prints the first word of the title.'''
print(title.split()[0])


'''Presents search results for test.'''
search = driver.find_element("name", "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)


# '''prints page source'''
# print(driver.page_source)


'''Locates for element presence but quits after 10 seconds.'''
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    print(main.text)

    articles = main.find_elements(By.TAG_NAME, "article")
    for article in articles:
        header = article.find_elements(By.XPATH, "//class[@id='entry-summary']")
    # print(header.text)

# except:
#     driver.quit()
#     print(f"Website {website} took too long to load.")

finally:
    '''Exits Chrome tab.'''
    time.sleep(2)
    driver.quit()

