"""
This is the Fidelity module.
Main website URL: https://www.fidelity.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


def etf_fidelity(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://www.fidelity.com/etfs/different-types-of-etfs

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.fidelity.com/etfs/different-types-of-etfs")

    # Waiting for the presence of a line in the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "tabs--content-active")))

    # For each element in the first type of table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, "strong.last-child"):
        if "®" in etf_row.get_attribute('textContent'):
            etf_data = []
            tag_a = etf_row.find_element(By.TAG_NAME, "a")

            etf_data.append(tag_a.get_attribute('textContent'))  # Ticker
            etf_data.append(str(etf_row.get_attribute('textContent')).split("(")[0].strip())  # Name
            etf_data.append(tag_a.get_attribute('href'))  # URL

            etf_list.append(etf_data)

    # For each row in the second type of table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, ".table-simple td"):
        if "®" in etf_row.get_attribute('textContent'):
            etf_data = []
            ticker = str(etf_row.get_attribute('textContent')).split("(")[1].replace("We're sorry, quotes are currently unavailable. Please try again.", "") \
                                                                            .replace("Close Popover", "").replace(")", "").replace("*", "").strip()

            etf_data.append(ticker)  # Ticker
            etf_data.append(str(etf_row.get_attribute('textContent')).split("(")[0].replace("†", "").strip())  # Name
            etf_data.append(f"https://screener.fidelity.com/ftgw/etf/goto/snapshot/snapshot.jhtml?symbols={ticker}")  # URL

            if etf_data not in etf_list:
                etf_list.append(etf_data)

    return etf_list
