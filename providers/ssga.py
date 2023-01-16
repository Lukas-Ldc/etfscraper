"""
This is the SSGA module.
Main website URL: https://www.ssga.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_ssga_irl(driver):
    """This function retrieves ETFs from the following URL: https://www.ssga.com/ie/en_gb/institutional/etfs/fund-finder

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.ssga.com/ie/en_gb/institutional/etfs/fund-finder")

    # Interaction with cookies.
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.ID, "js-ssmp-clrCookieSettingsLabel")))
    driver.find_element(By.ID, "js-ssmp-clrCookieSettingsLabel").click()
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "save-preference-btn-handler")))
    driver.find_element(By.CLASS_NAME, "save-preference-btn-handler").click()
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.ID, "js-ssmp-clrButtonLabel")))
    driver.find_element(By.ID, "js-ssmp-clrButtonLabel").click()

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "ssmp-mobile-header")))
    WebDriverWait(driver, timeout=20).until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "loader-container")))

    # For each row in the table.
    for etf_row in driver.find_element(By.CLASS_NAME, "tb-body").find_elements(By.TAG_NAME, "tr")[:-1]:
        etf_data = []

        if etf_row.get_attribute('class') != "index":
            etf_data.append(str(etf_row.find_elements(By.TAG_NAME, "a")[3].text).split(" ")[0])  # Ticker
            etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[1].text)  # Name
            etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[1].get_attribute('href'))  # URL

            etf_list.append(etf_data)

    return etf_list


def etf_ssga_usa(driver):
    """This function retrieves ETFs from the following URL: https://www.ssga.com/us/en/individual/etfs/fund-finder

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.ssga.com/us/en/individual/etfs/fund-finder")

    # Interaction with cookies.
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.ID, "js-ssmp-clrButtonLabel")))
    driver.find_element(By.ID, "js-ssmp-clrButtonLabel").click()

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "ssmp-mobile-header")))
    WebDriverWait(driver, timeout=20).until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "loader-container")))

    # For each row in the table.
    for etf_row in driver.find_element(By.CLASS_NAME, "tb-body").find_elements(By.TAG_NAME, "tr")[:-1]:
        etf_data = []

        if etf_row.get_attribute('class') != "index":
            etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[3].text)  # Ticker
            etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[1].text)  # Name
            etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[1].get_attribute('href'))  # URL

            etf_list.append(etf_data)

    return etf_list
