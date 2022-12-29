"""
This is the Sprott module.
Main website URL: https://sprott.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_sprott(driver):
    """This function retrieves ETFs from the following URL: https://sprott.com/

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://sprott.com/")

    # Interaction with cookies.
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll")))
    driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll").click()

    # Waiting for the presence of a line in the table.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.ID, "mainNav")))

    # For each row in the table.
    for etf_row in driver.find_element(By.ID, "mainNav").find_element(By.ID, "1").find_elements(By.TAG_NAME, "li"):
        etf_data = []

        ticker = etf_row.find_element(By.TAG_NAME, "span").get_attribute('textContent')
        etf_data.append(ticker)  # Ticker
        etf_data.append(' '.join(str(etf_row.find_element(By.TAG_NAME, "a").get_attribute('textContent')).replace(ticker, "").split()))  # Name
        etf_data.append(etf_row.find_element(By.TAG_NAME, "a").get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
