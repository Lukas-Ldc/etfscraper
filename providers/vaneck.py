"""
This is the VanEck module.
Main website URL: https://www.vaneck.com/
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


def etf_vaneck_irl(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://www.vaneck.com/ie/en/fundlisting/overview/etfs/

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.vaneck.com/ie/en/fundlisting/overview/etfs/")

    # Interaction with legal disclaimer.
    wdwait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "agree"))).click()

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "td.text-left")))

    # Cannot interact with cookies, making them disapear.
    wdwait.until(expected_conditions.presence_of_element_located((By.ID, "usercentrics-root")))
    driver.execute_script("arguments[0].remove();", driver.find_element(By.ID, "usercentrics-root"))
    sleep(2)

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, "table#overview tbody tr"):
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", etf_row)

        etf_data = []
        tag_a = etf_row.find_elements(By.TAG_NAME, "a")

        etf_data.append(tag_a[0].text)  # Ticker
        etf_data.append(tag_a[1].text)  # Name
        etf_data.append(tag_a[0].get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list


def etf_vaneck_usa(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://www.vaneck.com/us/en/etf-mutual-fund-finder/etfs/

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.vaneck.com/us/en/etf-mutual-fund-finder/etfs/")

    # Interaction with legal disclaimer.
    wdwait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[data-ve-gtm="ahp-investor-type"]')))
    wdwait.until(expected_conditions.invisibility_of_element_located((By.ID, "viewport-wide-spinner")))
    driver.find_element(By.CSS_SELECTOR, '[data-ve-gtm="ahp-investor-type"]').click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[data-id="retail"]'))).click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[data-ve-gtm="ahp-disclaimer-agree"]'))).click()

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "td.text-left")))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, "table#overview tbody tr"):
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", etf_row)

        etf_data = []
        tag_a = etf_row.find_elements(By.TAG_NAME, "a")

        etf_data.append(tag_a[0].text)  # Ticker
        etf_data.append(tag_a[1].text)  # Name
        etf_data.append(tag_a[0].get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list
