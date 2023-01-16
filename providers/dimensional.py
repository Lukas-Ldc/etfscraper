"""
This is the Dimensional module.
Main website URL: https://www.dimensional.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_dimensional(driver):
    """This function retrieves ETFs from the following URL: https://www.dimensional.com/us-en/funds

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.dimensional.com/us-en/funds?ft=etf")

    # Interaction with cookies.
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-reject-all-handler")))
    driver.find_element(By.ID, "onetrust-reject-all-handler").click()

    # Interaction with the type of investor.
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[data-a-lbl="an Individual Investor"]')))
    driver.find_element(By.CSS_SELECTOR, '[data-a-lbl="an Individual Investor"]').click()

    # Reloading page with ETF selector.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "tools-fund-listing-table-scrollable-container")))
    driver.get("https://www.dimensional.com/us-en/funds?ft=etf")

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "tools-fund-listing-table-scrollable-container")))

    # For each row in the table.
    for etf_row in driver.find_element(By.CLASS_NAME, "tools-fund-listing-table-scrollable-container").find_elements(By.CSS_SELECTOR, '[role="rowgroup"]'):
        etf_data = []

        etf_data.append(etf_row.find_element(By.CLASS_NAME, "tools-fund-listing-table-col-identifier").text)  # Ticker
        etf_data.append(etf_row.find_element(By.TAG_NAME, "a").text)  # Name
        etf_data.append(etf_row.find_element(By.TAG_NAME, "a").get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list
