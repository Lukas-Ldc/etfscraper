"""
This is the HANetf module.
Main website URL: https://www.hanetf.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def etf_hanetf(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://www.hanetf.com/product-list

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.hanetf.com/product-list")

    # Interaction with legal disclaimer.
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "ctl00_rptCountries_ctl03_lnkCountry"))).click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[data-type="individual"]'))).click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "ctl00_btnInvestorType"))).click()

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, "tbody")))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, "tbody tr"):
        etf_data = []
        tag_a = etf_row.find_elements(By.TAG_NAME, "a")

        etf_data.append(tag_a[1].text)  # Ticker
        etf_data.append(tag_a[0].text)  # Name
        etf_data.append(tag_a[0].get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
