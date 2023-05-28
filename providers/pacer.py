"""
This is the Pacer module.
Main website URL: https://www.paceretfs.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def etf_pacer(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://www.paceretfs.com/products

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.paceretfs.com/products")

    # Waiting for the presence of a line in the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.ID, "products-filter")))

    # For each row in each table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, ".theme-container tbody tr"):
        etf_data = []
        tag_a = etf_row.find_elements(By.TAG_NAME, "a")

        etf_data.append(tag_a[1].text)  # Ticker
        etf_data.append(tag_a[0].text)  # Name
        etf_data.append(tag_a[0].get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
