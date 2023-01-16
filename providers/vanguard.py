"""
This is the Vanguard module.
Main website URL: https://global.vanguard.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_vanguard_irl(driver):
    """This function retrieves ETFs from the following URL: https://www.ie.vanguard/products

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.ie.vanguard/products?fund-type=etf")

    # Interaction with cookies.
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-reject-all-handler")))
    driver.find_element(By.ID, "onetrust-reject-all-handler").click()

    # Interaction with legal notice.
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.ID, "mat-select-0")))
    driver.find_element(By.ID, "mat-select-0").click()
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.ID, "mat-option-0")))
    driver.find_element(By.ID, "mat-option-0").click()
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.ID, "investorType")))
    driver.find_element(By.ID, "investorType").click()
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.ID, "mat-option-22")))
    driver.find_element(By.ID, "mat-option-22").click()
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.XPATH, "//europe-core-consent-box[.//button]")))
    driver.find_element(By.TAG_NAME, "europe-core-consent-box").find_element(By.CLASS_NAME, "eds-cta-btn__primary-black").click()

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "product-header")))

    # For each row in the table.
    for etf_row in driver.find_element(By.CLASS_NAME, "product-table").find_elements(By.XPATH, "//tr[@class='ng-star-inserted']"):
        etf_data = []

        etf_data.append(str(etf_row.find_element(By.CSS_SELECTOR, '[headers="header-symbol-BLMB"]').find_element(By.TAG_NAME, "span").text).split(" ")[0])  # Ticker
        etf_data.append(str(etf_row.find_element(By.TAG_NAME, "a").text).split("\n")[0])  # Name
        etf_data.append(etf_row.find_element(By.TAG_NAME, "a").get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list


def etf_vanguard_usa(driver):
    """This function retrieves ETFs from the following URL: https://institutional.vanguard.com/fund-list/

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://institutional.vanguard.com/fund-list/?filters=etf%2C&sortBy=alphabetical")

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.ID, "tableData")))

    # For each row in the table.
    for etf_row in driver.find_element(By.ID, "tableData").find_elements(By.TAG_NAME, "tr"):
        etf_data = []

        etf_data.append(etf_row.find_element(By.CLASS_NAME, "symbolValueStyle").text)  # Ticker
        etf_data.append(etf_row.find_element(By.CLASS_NAME, "link-primary").text)  # Name
        etf_data.append(etf_row.find_element(By.CLASS_NAME, "link-primary").get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list
