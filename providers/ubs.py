"""
This is the UBS module.
Main website URL: https://www.ubs.com/
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


def etf_ubs(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://www.ubs.com/ch/en/assetmanagement/funds/etf.html

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.ubs.com/ch/en/assetmanagement/funds/etf.html")

    # Interaction with cookies.
    try:
        wdwait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "privacysettings__declineAllCookies"))).click()
    except TimeoutException:
        pass

    # Interaction with legal disclaimer.
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "privateinvestors--id-2-label"))).click()
    sleep(2)
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", driver.find_element(By.CLASS_NAME, "contextdisclaimer__profilesContentWrapper"))
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "contextdisclaimer__footer--sticky-visible")))
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", driver.find_element(By.CLASS_NAME, "contextdisclaimer__footer--sticky-visible"))
    sleep(2)
    driver.find_element(By.CLASS_NAME, "contextdisclaimer__footer--sticky-visible").find_element(By.TAG_NAME, "button").click()

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "MuiTableBody-root")))

    # Setting the number of rows per page.
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", driver.find_element(By.CLASS_NAME, "dropdown-container-button"))
    sleep(2)
    wdwait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "dropdown-container-button"))).click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "item")))
    driver.find_elements(By.CLASS_NAME, "item")[2].click()

    # Retrieval of web page elements.
    select_next = driver.find_element(By.CSS_SELECTOR, '[aria-label="Go to next page"]')

    # For each page.
    while True:

        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", driver.find_element(By.CLASS_NAME, "MuiPagination-ul"))
        sleep(1)

        # For each row in the table.
        for etf_row in driver.find_elements(By.CSS_SELECTOR, "tbody tr"):
            etf_data = []
            tag_a = etf_row.find_elements(By.TAG_NAME, "a")

            etf_data.append("-")  # Ticker
            etf_data.append(tag_a[0].text)  # Name
            etf_data.append(tag_a[0].get_attribute("href"))  # URL

            etf_list.append(etf_data)

        if "Mui-disabled" in select_next.get_attribute('class'):
            break
        else:
            select_next.click()

    return etf_list
