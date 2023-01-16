"""
This is the Horizons module.
Main website URL: https://horizonsetfs.com/
"""
from re import search
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_horizons(driver):
    """This function retrieves ETFs from the following URL: https://horizonsetfs.com/products/

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://horizonsetfs.com/products/")

    # Waiting for the presence the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.ID, "product-listing-table-all")))

    # Scrolling to the page buttons.
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center', inline: 'center'});", driver.find_element(By.CLASS_NAME, "disclaimer-text-column"))
    sleep(3)

    # For each page.
    breakk = False
    while not breakk:

        # For each row in the table.
        for etf_row in driver.find_element(By.ID, "product-listing-table-all").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"):
            etf_data = []

            etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].text)  # Ticker
            etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[1].text)  # Name
            etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute("href"))  # URL

            etf_list.append(etf_data)

        if search(r'disabled', driver.find_element(By.ID, "product-listing-table-all_next").get_attribute('class')):
            breakk = True
        else:
            driver.find_element(By.ID, "product-listing-table-all_next").click()

    return etf_list
