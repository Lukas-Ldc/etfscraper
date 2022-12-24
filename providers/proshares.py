"""
This is the ProShares module.
Main website URL: https://www.proshares.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_proshares(driver):
    """This function retrieves ETFs from the following URLs: https://www.proshares.com/our-etfs/find-strategic-etfs and https://www.proshares.com/our-etfs/find-leveraged-and-inverse-etfs

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.proshares.com/our-etfs/find-strategic-etfs")

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=10).until(expected_conditions.visibility_of_element_located((By.ID, "overviewBody")))

    # For each row in the table.
    for etf_row in driver.find_element(By.ID, "overviewBody").find_elements(By.TAG_NAME, "tr"):
        etf_data = []

        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].text)  # Ticker
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "td")[1].text)  # Name
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute('href'))  # URL

        etf_list.append(etf_data)

    driver.get("https://www.proshares.com/our-etfs/find-leveraged-and-inverse-etfs")

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=10).until(expected_conditions.visibility_of_element_located((By.ID, "overviewBody")))

    # For each row in the table.
    for etf_row in driver.find_element(By.ID, "overviewBody").find_elements(By.TAG_NAME, "tr"):
        etf_data = []

        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].text)  # Ticker
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "td")[1].text)  # Name
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list
