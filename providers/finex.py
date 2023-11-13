"""
This is the Finex module.
Main website URL: https://www.finexetf.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException


def etf_finex(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://www.finexetf.com/product/

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.set_window_size(800, 1000)
    driver.get("https://www.finexetf.com/product/")

    # Interaction with legal disclaimer.
    try:
        wdwait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "select")))
        Select(driver.find_element(By.TAG_NAME, "select")).select_by_value("Ireland")
        wdwait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Institutional investor')]"))).click()
    except TimeoutException:
        pass

    # Waiting for the presence of the table.
    driver.set_window_size(1920, 1080)
    driver.get("https://www.finexetf.com/product/")
    wdwait.until(expected_conditions.visibility_of_all_elements_located((By.TAG_NAME, "tbody")))

    # For each row in the menu.
    for etf_row in driver.find_elements(By.TAG_NAME, "tbody")[0].find_elements(By.TAG_NAME, "tr"):
        etf_data = []
        tag_a = etf_row.find_element(By.TAG_NAME, "a")

        etf_data.append(etf_row.find_elements(By.TAG_NAME, "td")[3].text)  # Ticker
        etf_data.append(tag_a.text)  # Name
        etf_data.append(tag_a.get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
