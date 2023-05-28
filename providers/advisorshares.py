"""
This is the AdvisorShares module.
Main website URL: https://advisorshares.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def etf_advisorshares(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://advisorshares.com/etfs/

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://advisorshares.com/etfs/")

    # Waiting for the presence of all the tables.
    wdwait.until(expected_conditions.presence_of_all_elements_located((By.TAG_NAME, "tbody")))

    # For each row in each table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, "tbody tr"):
        etf_data = []
        tag_a_list = etf_row.find_elements(By.TAG_NAME, "a")

        etf_data.append(tag_a_list[0].text)  # Ticker
        etf_data.append(str(tag_a_list[1].text).replace("\n", " "))  # Name
        etf_data.append(tag_a_list[0].get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
