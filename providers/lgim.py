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
    wdwait.until(expected_conditions.invisibility_of_element((By.CLASS_NAME, "canvas-zone-wrapper")))
    wdwait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "flex-row-reverse")))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CLASS_NAME, "overflow-hidden")[1:]:
        etf_data = []
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", etf_row)
        sleep(0.2)

        tag_a = etf_row.find_elements(By.TAG_NAME, "a")[0]

        etf_data.append("-")  # Ticker
        etf_data.append(tag_a.text)  # Name
        etf_data.append(tag_a.get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
