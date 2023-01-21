"""
This is the J.P. Morgan module.
Main website URL: https://am.jpmorgan.com/
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


def etf_jpmorgan_irl(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://am.jpmorgan.com/ie/en/asset-management/institutional/products/fund-explorer/etf

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://am.jpmorgan.com/ie/en/asset-management/institutional/products/fund-explorer/etf")

    # Interaction with cookies.
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-pc-btn-handler"))).click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "onetrust-close-btn-handler"))).click()

    try:
        driver.execute_script("arguments[0].style.display = 'none';", driver.find_element(By.CLASS_NAME, "jpm-modal-overlay"))
    except NoSuchElementException:
        pass

    # Interaction with legal disclaimer.
    wdwait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "accept"))).click()

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "ReactVirtualized__Table__Grid")))

    etf_row = []
    found = 10
    while found > 0:

        # For each row.
        for row in driver.find_elements(By.CSS_SELECTOR, ".ReactVirtualized__Table__Grid .ReactVirtualized__Table__row"):

            # If not alread processed.
            if row not in etf_row:
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", row)
                sleep(0.3)

                etf_data = []
                class_link = row.find_elements(By.CLASS_NAME, "Link")

                etf_data.append(row.find_element(By.CLASS_NAME, "FXT__RowCell__FundName__Header_Item").text)  # Ticker
                etf_data.append(class_link[0].text)  # Name
                etf_data.append(class_link[0].get_attribute('href'))  # URL

                etf_row.append(row)
                etf_list.append(etf_data)
                found += 1

            else:
                found -= 0.5

    return etf_list


def etf_jpmorgan_usa(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://am.jpmorgan.com/us/en/asset-management/per/products/fund-explorer/etf

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://am.jpmorgan.com/us/en/asset-management/per/products/fund-explorer/etf")

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "ReactVirtualized__Table__Grid")))

    try:
        driver.execute_script("arguments[0].style.display = 'none';", driver.find_element(By.CLASS_NAME, "jpm-modal-overlay"))
    except NoSuchElementException:
        pass

    etf_row = []
    found = 10
    while found > 0:

        # For each row.
        for row in driver.find_elements(By.CSS_SELECTOR, ".ReactVirtualized__Table__Grid .ReactVirtualized__Table__row"):

            # If not alread processed.
            if row not in etf_row:
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", row)
                sleep(0.3)

                etf_data = []
                class_link = row.find_elements(By.CLASS_NAME, "Link")

                etf_data.append(row.find_element(By.CLASS_NAME, "FXT__RowCell__FundName__Header_Item").text)  # Ticker
                etf_data.append(class_link[0].text)  # Name
                etf_data.append(class_link[0].get_attribute('href'))  # URL

                etf_row.append(row)
                etf_list.append(etf_data)
                found += 1

            else:
                found -= 0.5

    return etf_list
