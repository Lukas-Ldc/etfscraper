"""
This is the Allianz module.
Main website URL: https://www.allianzim.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def etf_allianz(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://www.allianzim.com/product-table/

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.allianzim.com/product-table/")

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, "tbody")))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, "tbody tr"):
        etf_data = []
        tag_a = etf_row.find_element(By.TAG_NAME, "a")
        tag_td_list = etf_row.find_elements(By.TAG_NAME, 'td')

        etf_data.append(tag_a.text)  # Ticker
        etf_data.append(f"{tag_td_list[1].text} {tag_td_list[2].text}".replace("\n", " "))  # Name
        etf_data.append(tag_a.get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
