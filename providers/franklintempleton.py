"""
This is the Franklin Templeton module.
Main website URL: https://www.franklintempleton.com/
"""

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


def etf_franklintempleton_irl(driver, wdwait):
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
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))).click()

    # Waiting for the presence of a line in the table.
    wdwait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "ag-cell-value")))

    # Retrieval of web page elements.
    class_page = driver.find_elements(By.CLASS_NAME, "ft__btn--pagination")

    # For each page.
    while True:

        # Scrolling to the page buttons.
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", class_page[1])
        sleep(3)

        # For each row in the table.
        for etf_row in driver.find_elements(By.CSS_SELECTOR, ".ag-center-cols-container .ag-row"):
            etf_data = []
            tag_a = etf_row.find_elements(By.TAG_NAME, "a")

            etf_data.append(str(etf_row.find_elements(By.CLASS_NAME, "ag-cell")[2].find_element(By.TAG_NAME, "span").text).split(" ")[0])  # Ticker
            etf_data.append(str(tag_a[0].text).rsplit(" - ", 1)[0])  # Name
            etf_data.append(tag_a[0].get_attribute("href"))  # URL

            etf_list.append(etf_data)

        if "pagination__btn--hide" in class_page[1].get_attribute('class'):
            break
        else:
            class_page[1].click()

    return etf_list


def etf_franklintempleton_usa(driver, wdwait):
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
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", class_page[1])
        sleep(3)

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
