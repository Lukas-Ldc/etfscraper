"""
This is the Legal & General module.
Main website URL: ttps://www.legalandgeneral.com/worldwide/
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


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

    # Interaction with cookies.
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-pc-btn-handler"))).click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "save-preference-btn-handler"))).click()

    # Interaction with legal disclaimer.
    wdwait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "popup-checkbox"))).find_element(By.TAG_NAME, "input").click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "btn-accept"))).click()

    # Waiting for the presence of a line in the table.
    driver.get("https://fundcentres.lgim.com/en/ie/institutional/fund-centre/ETF/")

    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "fund-row")))
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", driver.find_element(By.CLASS_NAME, "fund-row"))
    sleep(1)

    # For each row in the table.
    row_n = 0
    for etf_row in driver.find_elements(By.CSS_SELECTOR, ".outer-table .fund-row"):
        etf_data = []

        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", etf_row)
        sleep(0.3)
        class_accord = etf_row.find_element(By.CLASS_NAME, "accordion-arrow-icon")
        class_accord.click()
        sleep(0.3)

        etf_row_rload = driver.find_element(By.CLASS_NAME, "outer-table").find_elements(By.CLASS_NAME, "fund-row")[row_n]
        class_fund = etf_row_rload.find_element(By.CLASS_NAME, "fund-page-link")

        etf_data.append(etf_row_rload.find_elements(By.XPATH, "//td[@class='column-listingTicker']")[0].text)  # Ticker
        etf_data.append(class_fund.text)  # Name
        etf_data.append(class_fund.get_attribute("href"))  # URL

        class_accord.click()
        sleep(0.3)

        etf_list.append(etf_data)
        row_n += 1

    return etf_list
