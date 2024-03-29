"""
This is the ETFMG module.
Main website URL: https://etfmg.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def etf_etfmg(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://etfmg.com/our-funds/

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://etfmg.com/our-funds/")

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.ID, "list")))

    # For each row in the menu.
    for etf_row in driver.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"):
        etf_data = []
        tag_a = etf_row.find_elements(By.TAG_NAME, "a")

        etf_data.append(tag_a[0].text)  # Ticker
        etf_data.append(tag_a[1].text)  # Name
        etf_data.append(tag_a[0].get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
