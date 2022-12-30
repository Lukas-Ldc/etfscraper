"""
This is the DWS module.
Main website URL: https://etf.dws.com/en-gb/audience-selection/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_dws(driver):
    """This function retrieves ETFs from the following URL: https://etf.dws.com/en-gb/product-finder/

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://etf.dws.com/en-gb/product-finder/?PageSize=10000")

    # Interaction with cookies.
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.ID, "consent_prompt_reject")))
    driver.find_element(By.ID, "consent_prompt_reject").click()

    # Interaction with type of investor.
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[data-title="Professional Clients"]')))
    driver.find_element(By.CSS_SELECTOR, '[data-title="Professional Clients"]').click()
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.ID, "en-gb")))
    driver.find_element(By.ID, "en-gb").click()

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "partial-update-content-container")))

    # For each row in the table.
    for etf_row in driver.find_element(By.CLASS_NAME, "partial-update-content-container").find_elements(By.TAG_NAME, "tr"):
        etf_data = []

        etf_data.append("")  # Ticker
        etf_data.append(str(etf_row.find_element(By.TAG_NAME, "a").text).split("\n")[1])  # Name
        etf_data.append(etf_row.find_element(By.TAG_NAME, "a").get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
