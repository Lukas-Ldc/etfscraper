"""
This is the Fidelity module.
Main website URL: https://www.fidelity.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def etf_fidelity(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://www.fidelity.com/etfs/different-types-of-etfs

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.fidelity.com/etfs/different-types-of-etfs")

    # Waiting for the presence of a line in the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "cp-filters-card-wrapper")))

    # For each element in the first type of table.
    for etf_row in driver.find_element(By.ID, "ETFsdetailsallcardsFLEX").find_elements(By.CLASS_NAME, "scl-flex-card--desc-container"):
        etf_data = []
        tag_a = etf_row.find_element(By.TAG_NAME, "a")

        etf_data.append(tag_a.get_attribute('textContent'))  # Ticker
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "h3")[1].get_attribute('textContent').split("\n")[2])  # Name
        etf_data.append(tag_a.get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list
