"""
This is the Sprott module.
Main website URL: https://sprott.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


def etf_sprott(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://sprott.com/

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://sprott.com/")

    # Interaction with cookies.
    try:
        wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll"))).click()
    except TimeoutException:
        pass

    # Waiting for the presence of the menu.
    wdwait.until(expected_conditions.presence_of_element_located((By.ID, "mainNav")))

    # For each row in the menu.
    for etf_row in driver.find_element(By.ID, "mainNav").find_element(By.ID, "2").find_elements(By.TAG_NAME, "li"):
        etf_data = []
        tag_a = etf_row.find_element(By.TAG_NAME, "a")
        ticker = etf_row.find_element(By.TAG_NAME, "span").get_attribute('textContent')

        etf_data.append(ticker)  # Ticker
        etf_data.append(' '.join(str(tag_a.get_attribute('textContent')).replace(ticker, "").split()))  # Name
        etf_data.append(tag_a.get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
