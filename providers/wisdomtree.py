"""
This is the WisdomTree module.
Main website URL: https://www.wisdomtree.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import ElementNotInteractableException


def etf_wisdomtree_irl(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://www.wisdomtree.eu/en-ie/products

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.wisdomtree.eu/en-ie/products")

    # Interaction with cookies.
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "secondary"))).click()
    wdwait.until(expected_conditions.presence_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection"))).click()

    # Interaction with legal disclaimer.
    wdwait.until(expected_conditions.presence_of_element_located((By.ID, "accept-terms-btn"))).click()

    # Waiting for the presence of a line in the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "nameLink")))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, "tbody tr"):
        etf_data = []
        tag_a = etf_row.find_elements(By.TAG_NAME, "a")

        etf_data.append(etf_row.find_elements(By.TAG_NAME, "td")[1].text)  # Ticker
        etf_data.append(tag_a[0].text)  # Name
        etf_data.append(tag_a[0].get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list


def etf_wisdomtree_usa(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://www.wisdomtree.com/investments/etfs

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.wisdomtree.com/investments/etfs")

    # Removing the local website overlay.
    try:
        wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "continue-btn"))).click()
    except ElementNotInteractableException:
        pass

    # Waiting for the presence of a line in the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "nameLink")))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, "tbody tr"):
        etf_data = []

        etf_data.append(etf_row.find_element(By.CLASS_NAME, "tickerLink").text)  # Ticker
        etf_data.append(etf_row.find_element(By.CLASS_NAME, "nameLink").text)  # Name
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
