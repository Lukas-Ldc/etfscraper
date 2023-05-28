"""
This is the SSGA module.
Main website URL: https://www.ssga.com/
"""
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def etf_ssga_irl(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://www.ssga.com/ie/en_gb/institutional/etfs/fund-finder

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.ssga.com/ie/en_gb/institutional/etfs/fund-finder")

    # Interaction with cookies and legal disclaimer.
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "js-ssmp-clrCookieSettingsLabel")))
    ActionChains(driver).move_to_element(driver.find_element(By.ID, "js-ssmp-clrCookieSettingsLabel")).perform()
    driver.find_element(By.ID, "js-ssmp-clrCookieSettingsLabel").click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "save-preference-btn-handler"))).click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "js-ssmp-clrButtonLabel"))).click()

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "ssmp-mobile-header")))
    wdwait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "loader-container")))
    wdwait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tb-body tr")))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, ".tb-body tr")[:-1]:
        if etf_row.get_attribute('class') != "index":
            etf_data = []
            tag_a = etf_row.find_elements(By.TAG_NAME, "a")

            etf_data.append(str(tag_a[3].text).split(" ")[0])  # Ticker
            etf_data.append(tag_a[1].text)  # Name
            etf_data.append(tag_a[1].get_attribute('href'))  # URL

            etf_list.append(etf_data)

    return etf_list


def etf_ssga_usa(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://www.ssga.com/us/en/individual/etfs/fund-finder

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.ssga.com/us/en/individual/etfs/fund-finder")

    # Interaction with cookies and legal disclaimer.
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "js-ssmp-clrCookieSettingsLabel")))
    ActionChains(driver).move_to_element(driver.find_element(By.ID, "js-ssmp-clrCookieSettingsLabel")).perform()
    driver.find_element(By.ID, "js-ssmp-clrCookieSettingsLabel").click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "save-preference-btn-handler"))).click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "js-ssmp-clrButtonLabel"))).click()

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "ssmp-mobile-header")))
    wdwait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "loader-container")))
    wdwait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tb-body tr")))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, ".tb-body tr")[:-1]:
        if etf_row.get_attribute('class') != "index":
            etf_data = []
            tag_a = etf_row.find_elements(By.TAG_NAME, "a")

            etf_data.append(tag_a[3].text)  # Ticker
            etf_data.append(tag_a[1].text)  # Name
            etf_data.append(tag_a[1].get_attribute('href'))  # URL

            etf_list.append(etf_data)

    return etf_list
