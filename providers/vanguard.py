"""
This is the Vanguard module.
Main website URL: https://global.vanguard.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


def etf_vanguard_irl(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://www.ie.vanguard/products

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.ie.vanguard/products?fund-type=etf")

    # Interaction with cookies.
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))).click()

    # Interaction with legal disclaimer.
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "mat-select-0"))).click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "mat-option-0"))).click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "investorType"))).click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "mat-option-22"))).click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//europe-core-consent-box[.//button]")))
    driver.find_element(By.TAG_NAME, "europe-core-consent-box").find_element(By.CLASS_NAME, "eds-cta-btn__primary-black").click()

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, "product-header")))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, ".product-table tr.ng-star-inserted"):
        etf_data = []
        tag_a = etf_row.find_elements(By.TAG_NAME, "a")

        etf_data.append(str(etf_row.find_element(By.CSS_SELECTOR, '[headers="header-symbol-BLMB"]').find_element(By.TAG_NAME, "span").text).split(" ")[0])  # Ticker
        etf_data.append(str(tag_a[0].text).split("\n")[0])  # Name
        etf_data.append(tag_a[0].get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list


def etf_vanguard_usa(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://institutional.vanguard.com/fund-list/

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://institutional.vanguard.com/fund-list/?filters=etf%2C&sortBy=alphabetical")

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.ID, "tableData")))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, "#tableData tr"):
        etf_data = []
        class_link = etf_row.find_element(By.CLASS_NAME, "link-primary")

        etf_data.append(etf_row.find_element(By.CLASS_NAME, "symbolValueStyle").text)  # Ticker
        etf_data.append(class_link.text)  # Name
        etf_data.append(class_link.get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list
