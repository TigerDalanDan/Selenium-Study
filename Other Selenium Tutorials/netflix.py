""" TigerDalanDan Selenium project, where I use Selenium to open Netflix on Chrome, and ultimately
leading to the show 'Breaking Bad.' """

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


website = 'https://www.netflix.com/sg/login'
netflix_show = 'Breaking Bad'

'''Starts Chrome maximized.'''
options = Options()
options.add_argument("start-maximized")
options.add_experimental_option('detach', True)


'''Disables Chrome extensions.'''
options.add_argument("disable-extensions")


'''Locates ChromeDriver file.'''
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

'''Gets website.'''
driver.get(website)


'''keep credentials secret'''
file_path = '/Users/jet32/Documents/netflix_credentials.txt'

'''Open the file in read mode.'''
with open(file_path, "r") as file:
    # read the contents of the file
    file_contents = file.read()


'''Inputs username.'''
username = file_contents.split()[0]
driver.find_element("name", "userLoginId").send_keys(username)


'''Inputs password.'''
password = file_contents.split()[1]
driver.find_element("name", "password").send_keys(password)


'''Signs in.'''
signin_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[data-uia='login-submit-button']")
))
# clicks the button
driver.execute_script("arguments[0].click();", signin_button)


'''Selects profile.'''
select_profile = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "a[href='/SwitchProfile?tkn=3R3VSOEK3BGCJJ7VUM63KBNLIU']")
))
# clicks the profile
driver.execute_script("arguments[0].click();", select_profile)


'''Clicks on search bar.'''
show_search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[data-uia='search-box-launcher']")
))
# clicks the button
driver.execute_script("arguments[0].click();", show_search)


'''Inputs show and searches.'''
search_bar = driver.find_element("name", "searchInput").send_keys(netflix_show)
time.sleep(3)


'''Presses show.'''
press_show = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "a[aria-label='Breaking Bad']")
))
# clicks the button
driver.execute_script("arguments[0].click();", press_show)
time.sleep(3)


'''Presses play.'''
play_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[class='color-primary hasLabel hasIcon ltr-ed00td']")
))
# clicks the button
driver.execute_script("arguments[0].click();", play_button)
time.sleep(99999)

