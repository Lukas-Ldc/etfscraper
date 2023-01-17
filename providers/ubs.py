"""
This is the UBS module.
Main website URL: https://www.ubs.com/
"""
from re import search
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_ubs(driver):
    """This function retrieves ETFs from the following URL: https://www.ubs.com/ch/en/assetmanagement/funds/etf.html

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.ubs.com/ch/en/assetmanagement/funds/etf.html")

    # Interaction with cookies.
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "privacysettings__declineAllCookies")))
    driver.find_element(By.CLASS_NAME, "privacysettings__declineAllCookies").click()

    # Interaction with type of investor.
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.ID, "privateinvestors--id-2-label")))
    driver.find_element(By.ID, "privateinvestors--id-2-label").click()
    sleep(2)
    driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.CLASS_NAME, "contextdisclaimer__profilesContentWrapper"))
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "contextdisclaimer__footer--sticky-visible")))
    driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.CLASS_NAME, "contextdisclaimer__footer--sticky-visible"))
    sleep(2)
    driver.find_element(By.CLASS_NAME, "contextdisclaimer__footer--sticky-visible").find_element(By.TAG_NAME, "button").click()

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "MuiTableBody-root")))

    # Setting the number of rows per page.
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center', inline: 'center'});", driver.find_element(By.CLASS_NAME, "dropdown-container-button"))
    sleep(2)
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "dropdown-container-button")))
    driver.find_element(By.CLASS_NAME, "dropdown-container-button").click()
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "item")))
    driver.find_elements(By.CLASS_NAME, "item")[2].click()

    # For each page.
    breakk = False
    while not breakk:

        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center', inline: 'center'});", driver.find_element(By.CLASS_NAME, "MuiPagination-ul"))
        sleep(1)

        # For each row in the table.
        for etf_row in driver.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"):
            etf_data = []

            etf_data.append("-")  # Ticker
            etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].text)  # Name
            etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute("href"))  # URL

            etf_list.append(etf_data)

        if search(r'Mui-disabled', driver.find_element(By.CSS_SELECTOR, '[aria-label="Go to next page"]').get_attribute('class')):
            breakk = True
        else:
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Go to next page"]').click()

    return etf_list
