from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time


def safe_find(driver, id):
    try:
        elem = driver.find_element_by_id("ctl00_" + id)
    except NoSuchElementException:
        elem = driver.find_element_by_id(id)
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
driver.get('https://cn.morningstar.com/quickrank/default.aspx')
#
# print("selecting company")
# company_select = Select(driver.find_element_by_id('ctl00_cphMain_ddlCompany'))
# company_select.select_by_visible_text("华夏基金管理有限公司")
# time.sleep(2)

print("setting the options")



# 三年评级
for i in range(5):
    rating_checkbox = safe_find(driver, "cphMain_cblStarRating_{}".format(i))
    rating_checkbox.click()

# 主动管理
option_checkbox = safe_find(driver, "cphMain_cblGroup_3")
option_checkbox.click()

# 股票型
option_checkbox = safe_find(driver, "cphMain_cblCategory_0")
option_checkbox.click()

# 激进配置
option_checkbox = safe_find(driver, "cphMain_cblCategory_5")
option_checkbox.click()

# 灵活配置
option_checkbox = safe_find(driver, "cphMain_cblCategory_6")
option_checkbox.click()

print("submitting")
option_select = Select(safe_find(driver, 'cphMain_ddlPageSite'))
option_select.select_by_visible_text("全部")

driver.page_source

# time.sleep(6)
# submit_button = safe_find(driver, "cphMain_btnGo")
# submit_button.click()

print("result")
time.sleep(5) # Let the user actually see something!
driver.close()
driver.quit()
