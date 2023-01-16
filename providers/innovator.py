"""
This is the Innovator module.
Main website URL: https://www.innovatoretfs.com/
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


def etf_innovator(driver):
    """This function retrieves ETFs from the following URL: https://www.innovatoretfs.com/define/etfs/

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.innovatoretfs.com/define/etfs/#allproducts")

    # Waiting for the presence of a line in the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.XPATH, "//tbody[.//a]")))

    # Openning the menu.
    sleep(2)
    driver.execute_script("window.scrollTo(0, 0);")
    sleep(1)
    driver.find_element(By.ID, "siteNav").find_elements(By.TAG_NAME, "a")[1].click()
    sleep(1)
    for submenu in driver.find_element(By.ID, "siteNav").find_elements(By.CLASS_NAME, "collapsed"):
        submenu.click()

    # For each element in the menu.
    for etf_row in driver.find_element(By.ID, "dropdown_nav_submenu").find_elements(By.TAG_NAME, "li"):
        etf_data = []

        try:
            etf_data.append(etf_row.find_element(By.TAG_NAME, "span").text)  # Ticker
            etf_data.append(etf_row.find_element(By.TAG_NAME, "a").text)  # Name
            etf_data.append(etf_row.find_element(By.TAG_NAME, "a").get_attribute("href"))  # URL

            etf_list.append(etf_data)

        except NoSuchElementException:
            pass

    # For each row in the table.
    for etf_row in driver.find_element(By.ID, "allproducts").find_elements(By.TAG_NAME, "tr")[1:]:
        etf_data = []

        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].text)  # Ticker
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[4].text)  # Name
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
