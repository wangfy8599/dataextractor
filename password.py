from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time


def safe_find(driver, id):
    try:
        elem = driver.find_element_by_id(id)
    except NoSuchElementException:
        elem = None
    return elem


chrome_options = webdriver.ChromeOptions()
# https://peter.sh/experiments/chromium-command-line-switches/

# Run in headless mode, i.e., without a UI or display server dependencies.
# chrome_options.add_argument('--headless')

# Disables the sandbox for all process types that are normally sandboxed
chrome_options.add_argument('--no-sandbox')

chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--incognito')

chrome_options.add_argument(r'--user-data-dir=C:\Users\u0139119\AppData\Local\Google\Chrome\User Data')
driver = webdriver.Chrome(executable_path=r"D:\software\drivers\chromedriver.exe", options=chrome_options)
print("opening the web site")
driver.get('https://passwordmanager.thomsonreuters.com/hipm_tr/psf.exe#2')

print("opening the web site")
input_user = driver.find_element_by_name("USER_IDENT")
input_user.send_keys("U0139119")

print("opening the web site")
button_continue = driver.find_element_by_name("SUBMIT-TOKENS.x")
button_continue.click()

print("opening the web site")
input_usepwd = driver.find_element_by_name("SUBMIT-chn:$INTERNAL_password.pss")
input_usepwd.click()

# time.sleep(6)
# submit_button = safe_find(driver, "cphMain_btnGo")
# submit_button.click()

print("result")
time.sleep(5) # Let the user actually see something!
driver.close()
driver.quit()
