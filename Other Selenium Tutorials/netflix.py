""" TigerDalanDan Selenium project, where I use Selenium to open Netflix on Chrome, and ultimately
leading to the show 'Breaking Bad.' """


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

# keep credentials secret # FIXME# FIXME# FIXME# FIXME
file_path = '/Users/user/Documents/pswrds'

# open the file in read mode # FIXME# FIXME# FIXME# FIXME
with open(file_path, "r") as file:
    # read the contents of the file
    file_contents = file.read()


# username # FIXME# FIXME# FIXME# FIXME# FIXME# FIXME
driver.find_element("name", "userLoginId").send_keys(file_contents[0])


# password # FIXME# FIXME# FIXME# FIXME# FIXME# FIXME
driver.find_element("name", "password").send_keys(file_contents[1])


# sign in
driver.find_element("data-uia", "button[login-submit-button]").send_keys(Keys.ENTER) # FIXME
time.sleep(3)


# profile selection
driver.find_element("profile_name", 'Joni').click() # FIXME
time.sleep(3)


# show selection
driver.find_element("link_text", 'Breaking Bad').click() # FIXME
