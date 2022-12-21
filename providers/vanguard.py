"""
This is the Vanguard module.
Main website URL: https://global.vanguard.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_vanguard(driver):
    """This function retrieves ETFs from the following URL: https://institutional.vanguard.com/fund-list/

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://institutional.vanguard.com/fund-list/?filters=etf%2C&sortBy=alphabetical")

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.ID, "tableData")))

    # For each row in the table.
    for etf_row in driver.find_element(By.ID, "tableData").find_elements(By.TAG_NAME, "tr"):
        etf_data = []

        etf_data.append(etf_row.find_element(By.CLASS_NAME, "symbolValueStyle").text)  # Ticker
        etf_data.append(etf_row.find_element(By.CLASS_NAME, "link-primary").text)  # Name
        etf_data.append(etf_row.find_element(By.CLASS_NAME, "link-primary").get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list
