"""
This is the AdvisorShares module.
Main website URL: https://advisorshares.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_advisorshares(driver):
    """This function retrieves ETFs from the following URL: https://advisorshares.com/etfs/

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://advisorshares.com/etfs/")

    # Waiting for the presence of all the tables.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_all_elements_located((By.TAG_NAME, "tbody")))

    # For each table.
    for etf_table in driver.find_elements(By.TAG_NAME, "tbody"):

        # For each row in the table.
        for etf_row in etf_table.find_elements(By.TAG_NAME, "tr"):
            etf_data = []

            etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].text)  # Ticker
            etf_data.append(str(etf_row.find_elements(By.TAG_NAME, "a")[1].text).replace("\n", " "))  # Name
            etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute("href"))  # URL

            etf_list.append(etf_data)

    return etf_list
