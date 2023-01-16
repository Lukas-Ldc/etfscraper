"""
This is the Franklin Templeton module.
Main website URL: https://www.franklintempleton.com/
"""

from re import search
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_franklintempleton_irl(driver):
    """This function retrieves ETFs from the following URL: https://www.franklintempleton.ie/our-funds/price-and-performance-etfs

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.franklintempleton.ie/our-funds/price-and-performance-etfs#fund-identifiers")

    # Interaction with cookies.
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

    # Waiting for the presence of a line in the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "ag-cell-value")))

    # For each page.
    breakk = False
    while not breakk:

        # Scrolling to the page buttons.
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center', inline: 'center'});", driver.find_element(By.CLASS_NAME, "ft__btn--pagination"))
        sleep(3)

        # For each row in the table.
        for etf_row in driver.find_element(By.CLASS_NAME, "ag-center-cols-container").find_elements(By.CLASS_NAME, "ag-row"):
            etf_data = []

            etf_data.append(str(etf_row.find_elements(By.CLASS_NAME, "ag-cell")[2].find_element(By.TAG_NAME, "span").text).split(" ")[0])  # Ticker
            etf_data.append(str(etf_row.find_elements(By.TAG_NAME, "a")[0].text).rsplit(" - ", 1)[0])  # Name
            etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute("href"))  # URL

            etf_list.append(etf_data)

        if search(r'pagination__btn--hide', driver.find_elements(By.CLASS_NAME, "ft__btn--pagination")[1].get_attribute('class')):
            breakk = True
        else:
            driver.find_elements(By.CLASS_NAME, "ft__btn--pagination")[1].click()

    return etf_list


def etf_franklintempleton_usa(driver):
    """This function retrieves ETFs from the following URL: https://www.franklintempleton.com/investments/options/exchange-traded-funds

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.franklintempleton.com/investments/options/exchange-traded-funds")

    # Interaction with cookies.
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-reject-all-handler")))
    driver.find_element(By.ID, "onetrust-reject-all-handler").click()

    # Waiting for the presence of a line in the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "ag-cell-value")))

    # For each page.
    breakk = False
    while not breakk:

        # Scrolling to the page buttons.
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center', inline: 'center'});", driver.find_element(By.CLASS_NAME, "ft__btn--pagination"))
        sleep(3)

        # For each row in the table.
        for etf_row in driver.find_element(By.CLASS_NAME, "ag-center-cols-container").find_elements(By.CLASS_NAME, "ag-row"):
            etf_data = []

            etf_data.append(str(etf_row.find_elements(By.TAG_NAME, "a")[0].text).rsplit(" - ", 1)[1])  # Ticker
            etf_data.append(str(etf_row.find_elements(By.TAG_NAME, "a")[0].text).rsplit(" - ", 1)[0])  # Name
            etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute("href"))  # URL

            etf_list.append(etf_data)

        if search(r'pagination__btn--hide', driver.find_elements(By.CLASS_NAME, "ft__btn--pagination")[1].get_attribute('class')):
            breakk = True
        else:
            driver.find_elements(By.CLASS_NAME, "ft__btn--pagination")[1].click()

    return etf_list
