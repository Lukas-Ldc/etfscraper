"""
This is the Global X module.
Main website URL: https://www.globalxetfs.com
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def etf_globalx(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://www.globalxetfs.com/explore/

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.globalxetfs.com/explore/")

    # Waiting for the presence of a line in the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '[class="even"]')))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, '[aria-live="polite"] tr'):
        etf_data = []
        tag_td = etf_row.find_elements(By.TAG_NAME, "td")

        etf_data.append(tag_td[0].text)  # Ticker
        etf_data.append(tag_td[1].text)  # Name
        etf_data.append(tag_td[0].find_element(By.TAG_NAME, "a").get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
