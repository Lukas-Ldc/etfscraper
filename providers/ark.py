"""
This is the Ark module.
Main website URL: https://ark-funds.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_ark(driver):
    """This function retrieves ETFs from the following URL: https://ark-funds.com/our-etfs/

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://ark-funds.com/our-etfs/")

    # Waiting for the presence the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.ID, "dtBasicExample")))

    # For each row in the table.
    for etf_row in driver.find_element(By.ID, "dtBasicExample").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"):
        etf_data = []

        etf_data.append(etf_row.find_element(By.CLASS_NAME, "b-funds-item__text").find_element(By.TAG_NAME, "b").text)  # Ticker
        etf_data.append(etf_row.find_element(By.CLASS_NAME, "b-funds-item__text").find_element(By.TAG_NAME, "span").text)  # Name
        etf_data.append(str(etf_row.get_attribute("onclick")).split("'")[1][:-1])  # URL

        etf_list.append(etf_data)

    return etf_list
