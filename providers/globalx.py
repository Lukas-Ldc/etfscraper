"""
This is the Global X module.
Main website URL: https://www.globalxetfs.com
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_globalx(driver):
    """This function retrieves ETFs from the following URL: https://www.globalxetfs.com/explore/

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.globalxetfs.com/explore/")

    # Waiting for the presence of a line in the table.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '[class="even"]')))

    # For each row in the table.
    for etf_row in driver.find_element(By.CSS_SELECTOR, '[aria-live="polite"]').find_elements(By.TAG_NAME, "tr"):
        etf_data = []
        etf_col = etf_row.find_elements(By.TAG_NAME, "td")

        etf_data.append(etf_col[0].text)  # Ticker
        etf_data.append(etf_col[1].text)  # Name
        etf_data.append(etf_col[0].find_element(By.TAG_NAME, "a").get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
