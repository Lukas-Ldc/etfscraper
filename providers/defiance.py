"""
This is the Defiance module.
Main website URL: https://www.defianceetfs.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_defiance(driver):
    """This function retrieves ETFs from the following URL: https://www.defianceetfs.com/the-thematic-etf-boom/

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.defianceetfs.com/the-thematic-etf-boom/")

    # Waiting for the presence of the menu.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.ID, "list-etf")))

    # For each row in the menu.
    for etf_row in driver.find_element(By.ID, "list-etf").find_elements(By.TAG_NAME, "a"):
        etf_data = []

        etf_data.append(str(etf_row.get_attribute('textContent')).split("\n")[0])  # Ticker
        etf_data.append(str(etf_row.find_element(By.TAG_NAME, "div").get_attribute('textContent')).split("\n")[1].strip())  # Name
        etf_data.append(etf_row.get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
