"""
This is the ETC module.
Main website URL: https://exchangetradedconcepts.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_etc(driver):
    """This function retrieves ETFs from the following URL: https://exchangetradedconcepts.com/funds

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://exchangetradedconcepts.com/funds")

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.TAG_NAME, "tbody")))

    # For each row in the table.
    for etf_row in driver.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"):
        etf_data = []

        etf_data.append(etf_row.find_elements(By.TAG_NAME, "span")[0].text)  # Ticker
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "span")[2].text)  # Name
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute("url"))  # URL

        etf_list.append(etf_data)

    return etf_list
