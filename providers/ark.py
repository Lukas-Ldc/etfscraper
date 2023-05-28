"""
This is the Ark module.
Main website URL: https://ark-funds.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def etf_ark(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://ark-funds.com/our-etfs/

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://ark-funds.com/our-etfs/")

    # Waiting for the presence the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.ID, "dtBasicExample")))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, "#tt-overview #dtBasicExample tbody tr"):
        etf_data = []
        class_fund = etf_row.find_element(By.CLASS_NAME, "b-funds-item__text")

        etf_data.append(class_fund.find_element(By.TAG_NAME, "b").text)  # Ticker
        etf_data.append(class_fund.find_element(By.TAG_NAME, "span").text)  # Name
        etf_data.append(str(etf_row.get_attribute("onclick")).split("'")[1][:-1])  # URL

        etf_list.append(etf_data)

    return etf_list
