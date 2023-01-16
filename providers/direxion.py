"""
This is the Direxion module.
Main website URL: https://www.direxion.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_direxion(driver):
    """This function retrieves ETFs from the following URL: https://www.direxion.com/etfs

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.direxion.com/etfs")

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "dx-table")))

    # For each row in the table.
    for etf_row in driver.find_element(By.CLASS_NAME, "dx-table").find_elements(By.CLASS_NAME, "dx-table__tbody-item"):
        etf_data = []

        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].text)  # Ticker
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[1].text)  # Name
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
