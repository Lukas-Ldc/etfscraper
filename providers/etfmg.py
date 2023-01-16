"""
This is the ETFMG module.
Main website URL: https://etfmg.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_etfmg(driver):
    """This function retrieves ETFs from the following URL: https://etfmg.com/our-funds/

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://etfmg.com/our-funds/")

    # Interaction with the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.ID, "fundsList")))
    driver.find_element(By.ID, "fundsList").click()

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.ID, "funds")))

    # For each row in the menu.
    for etf_row in driver.find_elements(By.ID, "funds")[0].find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"):
        etf_data = []

        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].text)  # Ticker
        etf_data.append(etf_row.find_element(By.CLASS_NAME, "fn").text)  # Name
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
