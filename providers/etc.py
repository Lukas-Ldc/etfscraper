"""
This is the ETC module.
Main website URL: https://exchangetradedconcepts.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def etf_etc(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://exchangetradedconcepts.com/funds

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://exchangetradedconcepts.com/funds")

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, "tbody")))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, "tbody tr"):
        etf_data = []
        tag_span = etf_row.find_elements(By.TAG_NAME, "span")

        etf_data.append(tag_span[0].text)  # Ticker
        etf_data.append(tag_span[2].text)  # Name
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute("url"))  # URL

        etf_list.append(etf_data)

    return etf_list
