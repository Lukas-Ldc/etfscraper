"""
This is the Horizons module.
Main website URL: https://horizonsetfs.com/
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


def etf_horizons(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://horizonsetfs.com/products/

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://horizonsetfs.com/products/")

    # Waiting for the presence the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.ID, "product-listing-table-all")))

    # Scrolling to the page buttons.
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", driver.find_element(By.CLASS_NAME, "disclaimer-text-column"))
    sleep(3)

    # For each page.
    while True:

        # For each row in the table.
        for etf_row in driver.find_elements(By.CSS_SELECTOR, "#product-listing-table-all tbody tr"):
            etf_data = []
            tag_a = etf_row.find_elements(By.TAG_NAME, "a")

            etf_data.append(tag_a[0].text)  # Ticker
            etf_data.append(tag_a[1].text)  # Name
            etf_data.append(tag_a[0].get_attribute("href"))  # URL

            etf_list.append(etf_data)

        if "disabled" in driver.find_element(By.ID, "product-listing-table-all_next").get_attribute('class'):
            break
        else:
            driver.find_element(By.ID, "product-listing-table-all_next").click()

    return etf_list
