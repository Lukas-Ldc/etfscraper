"""
This is the iShares module.
Main website URL: https://www.ishares.com/us/ishares-global
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


def etf_ishares_gbr(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://www.ishares.com/uk/individual/en/products/etf-investments

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.ishares.com/uk/individual/en/products/etf-investments")

    # Interaction with cookies.
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))).click()

    # Interaction with legal disclaimer.
    wdwait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[data-link-event="Accept t&c: individual"]'))).click()

    driver.get("https://www.ishares.com/uk/individual/en/products/etf-investments#/?productView=etf&sortColumn=localExchangeTicker&sortDirection=asc&dataView=keyFacts&showAll=true")

    # Waiting for the presence of a line in the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "fund-cell-container")))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, '[role="grid"] tbody tr .fund-cell'):
        etf_data = []

        etf_data.append(etf_row.find_element(By.CLASS_NAME, "ticker").text)  # Ticker
        etf_data.append(etf_row.find_element(By.CLASS_NAME, "fund-name").text)  # Name
        etf_data.append(etf_row.find_element(By.CLASS_NAME, 'link-to-product-page').get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list


def etf_ishares_usa(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://www.ishares.com/us/products/etf-investments

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.ishares.com/us/products/etf-investments#/?productView=etf&sortColumn=localExchangeTicker&sortDirection=asc&dataView=keyFacts&showAll=true")

    # Interaction with cookies.
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))).click()

    # Waiting for the presence of a line in the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "fund-cell-container")))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, '[role="grid"] tbody tr .fund-cell'):
        etf_data = []

        etf_data.append(etf_row.find_element(By.CLASS_NAME, "ticker").text)  # Ticker
        etf_data.append(etf_row.find_element(By.CLASS_NAME, "fund-name").text)  # Name
        etf_data.append(etf_row.find_element(By.CLASS_NAME, 'link-to-product-page').get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list
