"""
This is the Fidelity module.
Main website URL: https://www.fidelity.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


def etf_fidelity(driver):
    """This function retrieves ETFs from the following URL: https://www.fidelity.com/etfs/different-types-of-etfs

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []

    multi_try = 3
    while multi_try > 0:
        try:
            driver.get("https://www.fidelity.com/etfs/different-types-of-etfs")
            # Waiting for the presence of a line in the table.
            WebDriverWait(driver, timeout=8).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "tabs--content-active")))
            multi_try = 0
        except TimeoutException:
            multi_try -= 1

    # For each element.
    for etf_row in driver.find_elements(By.XPATH, "//strong[@class='last-child']"):
        etf_data = []

        if "®" in etf_row.get_attribute('textContent'):
            etf_data.append(etf_row.find_element(By.TAG_NAME, "a").get_attribute('textContent'))  # Ticker
            etf_data.append(str(etf_row.get_attribute('textContent')).split("(")[0].strip())  # Name
            etf_data.append(etf_row.find_element(By.TAG_NAME, "a").get_attribute('href'))  # URL

            etf_list.append(etf_data)

    # For each row in the table.
    for etf_table in driver.find_elements(By.CLASS_NAME, "table-simple"):
        for etf_row in etf_table.find_elements(By.TAG_NAME, "td"):
            etf_data = []

            if "®" in etf_row.get_attribute('textContent'):
                ticker = str(etf_row.get_attribute('textContent')).split("(")[1].replace("Close Popover", "") \
                                                                                .replace("We're sorry, quotes are currently unavailable. Please try again.", "") \
                                                                                .replace(")", "").replace("*", "").strip()
                etf_data.append(ticker)  # Ticker
                etf_data.append(str(etf_row.get_attribute('textContent')).split("(")[0].replace("†", "").strip())  # Name
                etf_data.append(f"https://screener.fidelity.com/ftgw/etf/goto/snapshot/snapshot.jhtml?symbols={ticker}")  # URL

                if etf_data not in etf_list:
                    etf_list.append(etf_data)

    return etf_list
