"""
This is the Direxion module.
Main website URL: https://www.direxion.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


def etf_direxion(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://www.direxion.com/etfs

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.direxion.com/etfs")

    # Removing the alerts subscription overlay.
    try:
        wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "fancybox-close"))).click()
    except TimeoutException:
        pass

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, "react-tabs")))

    # For each row in the table.
    for etf_row in driver.find_element(By.CLASS_NAME, "react-tabs").find_elements(By.CSS_SELECTOR, "tbody tr"):
        etf_data = []
        tag_a = etf_row.find_elements(By.TAG_NAME, "a")

        if len(tag_a) == 0 or len(tag_a[0].text) == 0:
            continue

        etf_data.append(tag_a[0].text)  # Ticker
        etf_data.append(tag_a[1].text)  # Name
        etf_data.append(tag_a[0].get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
