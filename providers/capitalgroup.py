"""
This is the Capital Group module.
Main website URL: https://www.capitalgroup.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_capitalgroup(driver):
    """This function retrieves ETFs from the following URL: https://www.capitalgroup.com/individual/what-we-offer/exchange-traded-funds/returns

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.capitalgroup.com/individual/what-we-offer/exchange-traded-funds/returns")

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.TAG_NAME, "tbody")))

    # For each row in the table.
    for etf_row in driver.find_element(By.TAG_NAME, "tbody").find_elements(By.CLASS_NAME, "tabFund"):
        etf_data = []

        etf_data.append(etf_row.find_element(By.CLASS_NAME, "ticker-blue").text)  # Ticker
        etf_data.append(etf_row.find_element(By.CLASS_NAME, "ticker-black").text)  # Name
        etf_data.append(etf_row.find_element(By.TAG_NAME, "a").get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
