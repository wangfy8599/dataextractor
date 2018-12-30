#-*- coding=utf-8 -*-

import csv
import logging
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from common import utils, log_config

logger = logging.getLogger()


def safe_find(driver, elem_id):
    """Make sure a valid element can be found."""
    try:
        elem = driver.find_element_by_id("ctl00_" + elem_id)
    except NoSuchElementException:
        elem = driver.find_element_by_id(elem_id)
    return elem


def build_options():
    """Build the option for Chrome driver"""
    opts = webdriver.ChromeOptions()
    # https://peter.sh/experiments/chromium-command-line-switches/

    # Run in headless mode, i.e., without a UI or display server dependencies.
    opts.add_argument('--headless')

    # Disables the sandbox for all process types that are normally sandboxed
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
    opts.add_argument('--disable-extensions')
    # chrome_options.add_argument('--incognito')

    opts.add_argument("--no-proxy-server")

    opts.add_argument("--disable-gpu")

    opts.add_argument(r'--user-data-dir=C:\Users\u0139119\AppData\Local\Google\Chrome\User Data')
    return opts


def apply_parameters(driver):
    """"""
    logging.debug("applying the parameters")
    #
    # print("selecting company")
    # company_select = Select(driver.find_element_by_id('ctl00_cphMain_ddlCompany'))
    # company_select.select_by_visible_text("华夏基金管理有限公司")
    # time.sleep(2)

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

    # 标准混合
    option_checkbox = safe_find(driver, "cphMain_cblCategory_7")
    option_checkbox.click()

    # print("submitting")
    option_select = Select(safe_find(driver, 'cphMain_ddlPageSite'))
    option_select.select_by_visible_text("全部")

    # time.sleep(6)
    # submit_button = safe_find(driver, "cphMain_btnGo")
    # submit_button.click()


def write_csv(driver):
    """"""
    result_dir = os.path.join(utils.script_dir(), "results")
    if not os.path.isdir(result_dir):
        os.mkdir(result_dir)
    csv_file = os.path.join(result_dir, "morning_star.csv")
    logger.info("writing fund to " + csv_file)

    content_table = safe_find(driver, "cphMain_gridResult")
    index = 0
    with open(csv_file, "w", newline='', encoding='utf-8-sig') as cf:
        # cf.write(codecs.BOM_UTF8)
        writer = csv.writer(cf)
        for row in content_table.find_elements_by_tag_name("tr"):
            tag_name = "th" if index == 0 else "td"
            cell_list = []
            for cell in row.find_elements_by_tag_name(tag_name):
                cell_value = cell.text.replace('\n', '').strip() if cell else ""
                cell_list.append(cell_value)
            logger.debug(",".join(cell_list))
            writer.writerow(cell_list)
            index += 1
            if index % 50 == 0:
                logger.info("Updated {} funds.".format(index))

    logger.info("done")


def download_data():
    """"""
    url = 'https://cn.morningstar.com/quickrank/default.aspx'
    opts = build_options()
    driver = webdriver.Chrome(executable_path=r"D:\software\drivers\chromedriver.exe", options=opts)
    logging.debug("opening the web site " + url)
    driver.get(url)

    apply_parameters(driver)

    write_csv(driver)

    # time.sleep(300)  # Let the user actually see something!
    driver.close()
    driver.quit()



if __name__ == "__main__":
    try:
        log_config.init_logger()
        download_data()
    except Exception as ex:
        logger.exception(ex)
