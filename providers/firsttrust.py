"""
This is the First Trust module.
Main website URL: https://www.ftportfolios.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


def etf_firsttrust(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://www.ftportfolios.com/Retail/etf/etflist.aspx

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.ftportfolios.com/Retail/etf/etflist.aspx")

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "searchResults")))

    # For each row in each table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, ".searchResults tr"):
        try:
            etf_row.find_element(By.TAG_NAME, "th")
        except NoSuchElementException:
            etf_data = []
            tag_a = etf_row.find_elements(By.TAG_NAME, "a")

            etf_data.append(etf_row.find_elements(By.TAG_NAME, "td")[1].text)  # Ticker
            etf_data.append(tag_a[0].text)  # Name
            etf_data.append(tag_a[0].get_attribute('href'))  # URL

            etf_list.append(etf_data)

    return etf_list
