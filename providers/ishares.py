"""
This is the iShares module.
Main website URL: https://www.ishares.com/us
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_ishares(driver):
    """This function retrieves ETFs from the following URL: https://www.ishares.com/us/products/etf-investments

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.ishares.com/us/products/etf-investments#/?productView=etf&sortColumn=localExchangeTicker&sortDirection=asc&dataView=keyFacts&showAll=true")

    # Interaction with cookies.
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-reject-all-handler")))
    driver.find_element(By.ID, "onetrust-reject-all-handler").click()

    # Waiting for the presence of a line in the table.
    WebDriverWait(driver, timeout=5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "fund-cell-container")))

    # For each row in the table.
    for etf_row in driver.find_element(By.CSS_SELECTOR, '[role="grid"]').find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"):
        etf_data = []

        etf_data.append(etf_row.find_element(By.CLASS_NAME, "fund-cell").find_element(By.CLASS_NAME, "ticker").text)  # Ticker
        etf_data.append(etf_row.find_element(By.CLASS_NAME, "fund-cell").find_element(By.CLASS_NAME, "fund-name").text)  # Name
        etf_data.append(etf_row.find_element(By.CLASS_NAME, 'fund-cell').find_element(By.CLASS_NAME, 'link-to-product-page').get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list
