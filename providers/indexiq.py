"""
This is the IndexIQ module.
Main website URL: https://www.newyorklifeinvestments.com/
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_indexiq(driver):
    """This function retrieves ETFs from the following URL: https://www.newyorklifeinvestments.com/etf

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.newyorklifeinvestments.com/etf")

    # Interaction with cookies.
    WebDriverWait(driver, timeout=20).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "modal-footer__cookies")))
    driver.find_element(By.CLASS_NAME, "modal-footer__cookies").click()

    # Interaction with type of investor.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '[data-selector="individual"]')))
    driver.find_element(By.CLASS_NAME, "cmp-role-selection__modal").find_element(By.CSS_SELECTOR, '[data-selector="individual"]').click()

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=20).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "datatable-scroll")))

    # Scrolling at the bottom of the page.
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(5)

    # For each row in the table.
    for etf_row in driver.find_element(By.CLASS_NAME, "datatable-scroll").find_elements(By.CLASS_NAME, "datatable-row-center"):
        etf_data = []

        etf_data.append(etf_row.find_element(By.CLASS_NAME, "cmp-product-finder__table--cell-ticker").find_element(By.TAG_NAME, "span").text)  # Ticker
        etf_data.append(etf_row.find_element(By.CLASS_NAME, "cmp-product-finder__table--cell-fundNm").find_element(By.TAG_NAME, "a").text)  # Name
        etf_data.append(etf_row.find_element(By.CLASS_NAME, "cmp-product-finder__table--cell-fundNm").find_element(By.TAG_NAME, "a").get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
