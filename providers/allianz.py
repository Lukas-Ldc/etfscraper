"""
This is the Allianz module.
Main website URL: https://www.allianzim.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_allianz(driver):
    """This function retrieves ETFs from the following URL: https://www.allianzim.com/product-table/

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.allianzim.com/product-table/")

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.TAG_NAME, "tbody")))

    # For each row in the table.
    for etf_row in driver.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"):
        etf_data = []

        etf_data.append(etf_row.find_element(By.TAG_NAME, "a").text)  # Ticker
        etf_data.append(f"{etf_row.find_elements(By.TAG_NAME, 'td')[1].text} {etf_row.find_elements(By.TAG_NAME, 'td')[2].text}".replace("\n", " "))  # Name
        etf_data.append(etf_row.find_element(By.TAG_NAME, "a").get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
