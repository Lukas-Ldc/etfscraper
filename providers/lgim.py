"""
This is the Legal & General module.
Main website URL: ttps://www.legalandgeneral.com/worldwide/
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_lgim(driver):
    """This function retrieves ETFs from the following URL: https://fundcentres.lgim.com/en/ie/institutional/fund-centre/ETF/

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://fundcentres.lgim.com/en/ie/institutional/fund-centre/ETF/")

    # Interaction with cookies.
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-pc-btn-handler")))
    driver.find_element(By.ID, "onetrust-pc-btn-handler").click()
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "save-preference-btn-handler")))
    driver.find_element(By.CLASS_NAME, "save-preference-btn-handler").click()

    # Interaction with legal notice.
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "popup-checkbox")))
    driver.find_element(By.CLASS_NAME, "popup-checkbox").find_element(By.TAG_NAME, "input").click()
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "btn-accept")))
    driver.find_element(By.CLASS_NAME, "btn-accept").click()

    # Waiting for the presence of a line in the table.
    driver.get("https://fundcentres.lgim.com/en/ie/institutional/fund-centre/ETF/")
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "fund-row")))
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center', inline: 'center'});", driver.find_element(By.CLASS_NAME, "fund-row"))
    sleep(1)

    # For each row in the table.
    row_n = 0
    for etf_row in driver.find_element(By.CLASS_NAME, "outer-table").find_elements(By.CLASS_NAME, "fund-row"):
        etf_data = []

        driver.execute_script(f"window.scrollTo(0, {etf_row.location['y']});")
        sleep(0.6)
        etf_row.find_element(By.CLASS_NAME, "accordion-arrow-icon").click()
        sleep(0.3)

        etf_row_rload = driver.find_element(By.CLASS_NAME, "outer-table").find_elements(By.CLASS_NAME, "fund-row")[row_n]
        etf_data.append(etf_row_rload.find_elements(By.XPATH, "//td[@class='column-listingTicker']")[0].text)  # Ticker
        etf_data.append(etf_row_rload.find_element(By.CLASS_NAME, "fund-page-link").text)  # Name
        etf_data.append(etf_row_rload.find_element(By.CLASS_NAME, "fund-page-link").get_attribute("href"))  # URL

        etf_row.find_element(By.CLASS_NAME, "accordion-arrow-icon").click()
        sleep(0.3)

        etf_list.append(etf_data)
        row_n += 1

    return etf_list
