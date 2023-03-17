from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach', True)
chrome_driver = webdriver.Chrome()

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.netflix.com/sg/login')

# username
driver.find_element("name", "userLoginId").send_keys("jet.pilot@rocketmail.com")

# password
driver.find_element("name", "password").send_keys("joshua24:15")

# sign in
driver.find_element("data-uia", "button[login-submit-button]").send_keys(Keys.ENTER) # FIXME
time.sleep(3)

# profile selection
driver.find_element("profile_name", 'Joni').click() # FIXME
time.sleep(3)

# show selection
driver.find_element("link_text", 'Breaking Bad').click() # FIXME
