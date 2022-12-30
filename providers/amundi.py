"""
This is the Amundi module.
Main website URL: https://www.amundietf.com/?skip=true
"""
from re import search
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_amundi(driver):
    """This function retrieves ETFs from the following URL: https://www.amundietf.fr/fr/professionnels/produits-etf/recherche

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.amundietf.fr/fr/professionnels/produits-etf/recherche")

    # Interaction with type of investor.
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[data-profile="INSTIT"]')))
    driver.find_element(By.CSS_SELECTOR, '[data-profile="INSTIT"]').click()
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.ID, "confirmDisclaimer")))
    driver.find_element(By.ID, "confirmDisclaimer").click()

    # Interaction with cookies.
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.ID, "CookiesDisclaimerRibbonV1-Settings")))
    driver.find_element(By.ID, "CookiesDisclaimerRibbonV1-Settings").click()
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.ID, "CookiesDisclaimerPopupV1-Save")))
    driver.find_element(By.ID, "CookiesDisclaimerPopupV1-Save").click()

    # Waiting for the presence of a line in the table.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.TAG_NAME, "tbody")))

    # For each page.
    breakk = False
    while not breakk:

        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center', inline: 'center'});", driver.find_element(By.TAG_NAME, "thead"))
        sleep(1.5)

        # For each row in the table.
        for etf_row in driver.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"):
            etf_data = []

            driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center', inline: 'center'});", etf_row)

            etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].text)  # Ticker
            etf_data.append(str(etf_row.find_elements(By.TAG_NAME, "a")[2].text).split("\n")[0])  # Name
            etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute("href"))  # URL

            etf_list.append(etf_data)

        sleep(0.5)
        if search(r'disabled', driver.find_element(By.CLASS_NAME, "pagination").find_elements(By.TAG_NAME, "li")[-1].get_attribute('class')):
            breakk = True
        else:
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Next"]').click()

    return etf_list
