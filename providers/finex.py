"""
This is the Finex module.
Main website URL: https://www.finexetf.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


def etf_finex(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://www.finexetf.com/product/

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.finexetf.com/product/")

    # Interaction with legal disclaimer.
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "chooseColumn-0-2-97")))
    driver.find_element(By.CLASS_NAME, "chooseColumn-0-2-97").find_elements(By.TAG_NAME, "div")[0].click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "title-0-2-116")))
    driver.find_elements(By.CLASS_NAME, "title-0-2-116")[1].click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "agreeCheckbox-0-2-124"))).click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "button-0-2-127"))).click()

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "root-0-2-62")))

    # For each row in the menu.
    for etf_row in driver.find_elements(By.CLASS_NAME, "root-0-2-62")[0].find_elements(By.CSS_SELECTOR, "tbody tr"):
        etf_data = []
        tag_a = etf_row.find_element(By.TAG_NAME, "a")

        etf_data.append(str(etf_row.find_elements(By.TAG_NAME, "td")[3].text).split(" ")[0])  # Ticker
        etf_data.append(tag_a.text)  # Name
        etf_data.append(tag_a.get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
