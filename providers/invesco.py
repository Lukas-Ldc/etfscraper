"""
This is the Invesco module.
Main website URL: https://www.invesco.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_invesco_usa(driver):
    """This function retrieves ETFs from the following URL: https://www.invesco.com/us/financial-products/etfs/performance

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.invesco.com/us/financial-products/etfs/performance")

    # Interaction with the type of investor.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.ID, "Individual Investor")))
    driver.find_element(By.CSS_SELECTOR, '[data-investor="IndividualInvestor"]').find_element(By.CLASS_NAME, "o-label").click()
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[data-event-action="audience role selector click"]')))
    driver.find_element(By.CSS_SELECTOR, '[data-event-action="audience role selector click"]').click()

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=10).until(expected_conditions.visibility_of_element_located((By.ID, "etfPerformancesTable")))

    # For each row in the table.
    for etf_row in driver.find_element(By.ID, "etfPerformancesTable").find_elements(By.CLASS_NAME, "fund-link"):
        etf_data = []

        etf_data.append(etf_row.find_element(By.CLASS_NAME, "ticker-label-bold").find_element(By.TAG_NAME, "a").text)  # Ticker
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].text)  # Name
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list


def etf_invesco_irl(driver):
    """This function retrieves ETFs from the following URL: https://etf.invesco.com/ie/private/en/products

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://etf.invesco.com/ie/private/en/products")

    # Interaction with cookies.
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "agree-button")))
    driver.find_element(By.CLASS_NAME, "agree-button").click()

    # Interaction with the country.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.XPATH, "//select[@class='all_terms']")))
    driver.execute_script("arguments[0].style.display = 'block';", driver.find_element(By.XPATH, "//select[@class='all_terms']"))
    WebDriverWait(driver, timeout=10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//select[@class='all_terms']")))
    Select(driver.find_element(By.XPATH, "//select[@class='all_terms']")).select_by_value("Ireland")

    # Interaction with the type of investor.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[@class='private']")))
    driver.find_element(By.XPATH, "//button[@class='private']").click()
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.ID, "overlay_button_submit")))
    driver.find_element(By.ID, "overlay_button_submit").click()

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "view-content")))

    # For each row in the table.
    for etf_row in driver.find_element(By.CLASS_NAME, "view-content").find_elements(By.CLASS_NAME, "visible-md"):
        etf_data = []

        etf_data.append(etf_row.find_element(By.CLASS_NAME, 'ticker').text)  # Ticker
        etf_data.append(etf_row.find_element(By.CLASS_NAME, 'short-name').text)  # Name
        etf_data.append(etf_row.get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list
