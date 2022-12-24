"""
This is the VanEck module.
Main website URL: https://www.vaneck.com/
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_vaneck_irl(driver):
    """This function retrieves ETFs from the following URL: https://www.vaneck.com/ie/en/fundlisting/overview/etfs/

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.vaneck.com/ie/en/fundlisting/overview/etfs/")

    # Interaction with legal notice.
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "agree")))
    driver.find_element(By.CLASS_NAME, "agree").click()

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.XPATH, "//td[@class='text-left']")))

    # Cannot interact with cookies, making them disapear.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.ID, "usercentrics-root")))
    driver.execute_script("arguments[0].remove();", driver.find_element(By.ID, "usercentrics-root"))
    sleep(2)

    # For each row in the table.
    for etf_row in driver.find_element(By.XPATH, "//table[@id='overview']").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"):
        etf_data = []

        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].text)  # Ticker
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[1].text)  # Name
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list


def etf_vaneck_usa(driver):
    """This function retrieves ETFs from the following URL: https://www.vaneck.com/us/en/etf-mutual-fund-finder/etfs/

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.vaneck.com/us/en/etf-mutual-fund-finder/etfs/")

    # Interaction with legal notice.
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[data-ve-gtm="ahp-investor-type"]')))
    WebDriverWait(driver, timeout=10).until(expected_conditions.invisibility_of_element_located((By.ID, "viewport-wide-spinner")))
    driver.find_element(By.CSS_SELECTOR, '[data-ve-gtm="ahp-investor-type"]').click()
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[data-id="retail"]')))
    driver.find_element(By.CSS_SELECTOR, '[data-id="retail"]').click()
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[data-ve-gtm="ahp-disclaimer-agree"]')))
    driver.find_element(By.CSS_SELECTOR, '[data-ve-gtm="ahp-disclaimer-agree"]').click()

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.XPATH, "//td[@class='text-left']")))

    # For each row in the table.
    for etf_row in driver.find_element(By.XPATH, "//table[@id='overview']").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"):
        etf_data = []

        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].text)  # Ticker
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[1].text)  # Name
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list
