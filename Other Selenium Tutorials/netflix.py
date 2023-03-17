from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.netflix.com/sg/login')

# username
driver.find_element("name", "userLoginId").send_keys("jet.pilot@rocketmail.com")
time.sleep(3)

# password
driver.find_element("name", "password").send_keys("joshua24:15")
time.sleep(3)

# login
driver.find_element("css_selector", "button[data-uia=login-submit-button]").send_keys(Keys.ENTER)
time.sleep(3)

# profile selection
driver.find_element("link_text", 'Joni').click()
time.sleep(3)

# show selection
driver.find_element("link_text", 'Breaking Bad').click()
