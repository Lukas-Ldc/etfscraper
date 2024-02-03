"""
This is the DWS module.
Main website URL: https://etf.dws.com/en-gb/audience-selection/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def etf_dws(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://etf.dws.com/en-gb/product-finder/

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://etf.dws.com/en-gb/product-finder/?PageSize=10000")

    # Interaction with cookies.
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "consent_prompt_reject"))).click()

    # Interaction with legal disclaimerr.
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "pv_id_4_1"))).click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[name="continue"]'))).click()

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "partial-update-content-container")))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, ".partial-update-content-container tr"):
        etf_data = []
        tag_a = etf_row.find_element(By.TAG_NAME, "a")

        etf_data.append("-")  # Ticker
        etf_data.append(str(tag_a.text).split("\n")[1])  # Name
        etf_data.append(tag_a.get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
