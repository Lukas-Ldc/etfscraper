"""
This is the Dimensional module.
Main website URL: https://www.dimensional.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


def etf_dimensional(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://www.dimensional.com/us-en/funds

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.dimensional.com/us-en/funds?ft=etf")

    # Interaction with cookies.
    try:
        wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))).click()
    except TimeoutException:
        pass

    # Interaction with legal disclaimer.
    wdwait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[data-a-lbl="an Individual Investor"]'))).click()

    # Reloading page with ETF selector.
    wdwait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "sticky-header-container")))
    driver.get("https://www.dimensional.com/us-en/funds?ft=etf")

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "tools-fund-listing-table-scrollable-container")))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, '.tools-fund-listing-table-scrollable-container [role="rowgroup"]'):
        etf_data = []
        tag_a = etf_row.find_element(By.TAG_NAME, "a")

        etf_data.append(etf_row.find_element(By.CLASS_NAME, "tools-fund-listing-table-col-identifier").text)  # Ticker
        etf_data.append(tag_a.text)  # Name
        etf_data.append(tag_a.get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list
