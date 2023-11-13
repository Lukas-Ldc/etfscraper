"""
This is the Legal & General module.
Main website URL: ttps://www.legalandgeneral.com/worldwide/
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


def etf_lgim(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://fundcentres.lgim.com/en/ie/institutional/fund-centre/ETF/

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://fundcentres.lgim.com/en/ie/institutional/fund-centre/ETF/")

    try:
        # Interaction with cookies.
        wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))).click()
        # Interaction with legal disclaimer.
        wdwait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".popup-checkbox input"))).click()
        wdwait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "btn-accept"))).click()
    except TimeoutException:
        pass

    # Waiting for the presence of a line in the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#fc-root .min-h-screen .truncate")))
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", driver.find_elements(By.CLASS_NAME, "overflow-hidden")[0])
    sleep(1)

    # For each row in the table.
    for etf_row in driver.find_elements(By.CLASS_NAME, "overflow-hidden"):
        etf_data = []

        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", etf_row)

        sleep(0.3)
        etf_row.find_element(By.CSS_SELECTOR, '.w-full button .justify-between').click()
        sleep(0.3)

        etf_row.find_elements(By.CSS_SELECTOR, "nav button")[1].click()
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "tbody")[1].find_elements(By.TAG_NAME, "td")[2].text)  # Ticker
        etf_row.find_element(By.CSS_SELECTOR, '.w-full button .justify-between').click()
        sleep(0.3)

        etf_data.append(etf_row.find_element(By.TAG_NAME, "a").text)  # Name
        etf_data.append(etf_row.find_element(By.TAG_NAME, "a").get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
