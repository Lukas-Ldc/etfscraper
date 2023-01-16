"""
This is the HANetf module.
Main website URL: https://www.hanetf.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_hanetf(driver):
    """This function retrieves ETFs from the following URL: https://www.hanetf.com/product-list

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.hanetf.com/product-list")

    # Interaction with type of investor.
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.ID, "ctl00_rptCountries_ctl03_lnkCountry")))
    driver.find_element(By.ID, "ctl00_rptCountries_ctl03_lnkCountry").click()
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[data-type="individual"]')))
    driver.find_element(By.CSS_SELECTOR, '[data-type="individual"]').click()
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.ID, "ctl00_btnInvestorType")))
    driver.find_element(By.ID, "ctl00_btnInvestorType").click()

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.TAG_NAME, "tbody")))

    # For each row in the table.
    for etf_row in driver.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"):
        etf_data = []

        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[1].text)  # Ticker
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].text)  # Name
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
