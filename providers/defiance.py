"""
This is the Defiance module.
Main website URL: https://www.defianceetfs.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def etf_defiance(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://www.defianceetfs.com/the-thematic-etf-boom/

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.defianceetfs.com/the-thematic-etf-boom/")

    # Waiting for the presence of the menu.
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "etf-list-wrp")))

    # For each row in the menu.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, ".etf-list-wrp .etf-list-item"):
        etf_data = []

        etf_data.append(str(etf_row.find_element(By.CLASS_NAME, "etf-list-abr").text))  # Ticker
        etf_data.append(str(etf_row.find_element(By.CLASS_NAME, "etf-list-title").text))  # Name
        etf_data.append(etf_row.find_element(By.TAG_NAME, "a").get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
