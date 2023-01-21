"""
This is the Goldman Sachs module.
Main website URL: https://www.gsam.com/
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


def etf_goldmansachs_gbr(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://www.gsam.com/content/gsam/uk/en/advisers/products/etf-fund-finder.html

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.gsam.com/content/gsam/uk/en/advisers/products/etf-fund-finder.html")

    # Interaction with legal disclaimer.
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "tocaccept"))).click()
    wdwait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "center-modal-overlay-container")))

    # Interaction with cookies.
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "truste-consent-required"))).click()

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "performance_data")))

    # Loading the entire table
    t_size = driver.find_element(By.ID, "gridContainerWrapper").size['height']
    t_size_new = t_size + 1
    while t_size != t_size_new:
        t_size = driver.find_element(By.ID, "gridContainerWrapper").size['height']
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", driver.find_element(By.CLASS_NAME, "exposedSitemap"))
        sleep(3)
        t_size_new = driver.find_element(By.ID, "gridContainerWrapper").size['height']

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, "#gridContainerWrapper .performance_data .assetclass-link"):
        etf_data = []

        etf_data.append(etf_row.find_element(By.TAG_NAME, "span").text)  # Ticker
        etf_data.append(etf_row.get_attribute('title'))  # Name
        etf_data.append(etf_row.get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list


def etf_goldmansachs_usa(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://www.gsam.com/content/gsam/us/en/individual/products/etf-fund-finder.html

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.gsam.com/content/gsam/us/en/individual/products/etf-fund-finder.html")

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "performance_data")))

    # Loading the entire table
    t_size = driver.find_element(By.ID, "gridContainerWrapper").size['height']
    t_size_new = t_size + 1
    while t_size != t_size_new:
        t_size = driver.find_element(By.ID, "gridContainerWrapper").size['height']
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", driver.find_element(By.CLASS_NAME, "exposedSitemap"))
        sleep(3)
        t_size_new = driver.find_element(By.ID, "gridContainerWrapper").size['height']

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, "#gridContainerWrapper .performance_data .assetclass-link"):
        etf_data = []

        etf_data.append(etf_row.find_element(By.TAG_NAME, "span").text)  # Ticker
        etf_data.append(etf_row.get_attribute('title'))  # Name
        etf_data.append(etf_row.get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list
