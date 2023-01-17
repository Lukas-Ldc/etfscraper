"""
This is the WisdomTree module.
Main website URL: https://www.wisdomtree.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import ElementNotInteractableException


def etf_wisdomtree_irl(driver):
    """This function retrieves ETFs from the following URL: https://www.wisdomtree.eu/en-ie/products

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.wisdomtree.eu/en-ie/products")

    # Interaction with cookies.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "secondary")))
    driver.find_element(By.CLASS_NAME, "secondary").click()
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection")))
    driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection").click()

    # Interaction with legal disclaimer.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.ID, "accept-terms-btn")))
    driver.find_element(By.ID, "accept-terms-btn").click()

    # Waiting for the presence of a line in the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "nameLink")))

    # For each row in the table.
    for etf_row in driver.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"):
        etf_data = []

        etf_data.append(etf_row.find_elements(By.TAG_NAME, "td")[1].text)  # Ticker
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].text)  # Name
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list


def etf_wisdomtree_usa(driver):
    """This function retrieves ETFs from the following URL: https://www.wisdomtree.com/investments/etfs

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.wisdomtree.com/investments/etfs")

    # Removing the local website overlay.
    try:
        WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "continue-btn")))
        driver.find_element(By.CLASS_NAME, "continue-btn").click()
    except ElementNotInteractableException:
        pass

    # Waiting for the presence of a line in the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "nameLink")))

    # For each row in the table.
    for etf_row in driver.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"):
        etf_data = []

        etf_data.append(etf_row.find_element(By.CLASS_NAME, "tickerLink").text)  # Ticker
        etf_data.append(etf_row.find_element(By.CLASS_NAME, "nameLink").text)  # Name
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
