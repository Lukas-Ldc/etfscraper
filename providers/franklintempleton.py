"""
This is the Franklin Templeton module.
Main website URL: https://www.franklintempleton.com/
"""

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


def etf_franklintempleton_irl(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://www.franklintempleton.ie/our-funds/price-and-performance-etfs

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.franklintempleton.ie/our-funds/price-and-performance-etfs#fund-identifiers")

    # Interaction with cookies.
    try:
        wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-pc-btn-handler"))).click()
        wdwait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "ot-pc-refuse-all-handler"))).click()
    except TimeoutException:
        pass

    # Waiting for the presence of a line in the table.
    wdwait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "ag-center-cols-container")))

    # Retrieval of web page elements.
    class_page = driver.find_elements(By.CLASS_NAME, "ft__btn--pagination")

    # For each page.
    while True:

        # Scrolling to the page buttons.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", class_page[1])
        sleep(1)

        # For each row in the table.
        for etf_row in driver.find_elements(By.CSS_SELECTOR, ".ag-center-cols-container .ag-row"):
            etf_data = []
            tag_a = etf_row.find_elements(By.TAG_NAME, "a")

            etf_data.append(etf_row.find_element(By.CSS_SELECTOR, '[col-id="BLOOMBERG"]').text)  # Ticker
            etf_data.append(str(tag_a[0].text).split("-")[0].strip())  # Name
            etf_data.append(tag_a[0].get_attribute("href"))  # URL

            etf_list.append(etf_data)

        if "pagination__btn--hide" in class_page[1].get_attribute('class'):
            break
        else:
            class_page[1].click()

    return etf_list


def etf_franklintempleton_usa(driver: webdriver, wdwait: WebDriverWait):
    """This function retrieves ETFs from the following URL: https://www.franklintempleton.com/investments/options/exchange-traded-funds

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.franklintempleton.com/investments/options/exchange-traded-funds")

    # Interaction with cookies.
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))).click()

    # Waiting for the presence of a line in the table.
    wdwait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "ag-cell-value")))

    # Retrieval of web page elements.
    class_page = driver.find_elements(By.CLASS_NAME, "ft__btn--pagination")

    # For each page.
    while True:

        # Scrolling to the page buttons.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", class_page[1])
        sleep(1)

        # For each row in the table.
        for etf_row in driver.find_elements(By.CSS_SELECTOR, ".ag-center-cols-container .ag-row"):
            etf_data = []
            tag_a = etf_row.find_elements(By.TAG_NAME, "a")

            etf_data.append(str(tag_a[0].text).rsplit(" - ", 1)[1])  # Ticker
            etf_data.append(str(tag_a[0].text).rsplit(" - ", 1)[0])  # Name
            etf_data.append(tag_a[0].get_attribute("href"))  # URL

            etf_list.append(etf_data)

        if "pagination__btn--hide" in class_page[1].get_attribute('class'):
            break
        else:

            class_page[1].click()

    return etf_list
