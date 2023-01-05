"""
This is the Finex module.
Main website URL: https://www.finexetf.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_finex(driver):
    """This function retrieves ETFs from the following URL: https://www.finexetf.com/product/

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.finexetf.com/product/")

    # Interaction with legal notice.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "chooseColumn-0-2-97")))
    driver.find_element(By.CLASS_NAME, "chooseColumn-0-2-97").find_elements(By.TAG_NAME, "div")[0].click()
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "title-0-2-116")))
    driver.find_elements(By.CLASS_NAME, "title-0-2-116")[1].click()
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "agreeCheckbox-0-2-124")))
    driver.find_element(By.CLASS_NAME, "agreeCheckbox-0-2-124").click()
    WebDriverWait(driver, timeout=10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "button-0-2-127")))
    driver.find_element(By.CLASS_NAME, "button-0-2-127").click()

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "root-0-2-62")))

    # For each row in the menu.
    for etf_row in driver.find_elements(By.CLASS_NAME, "root-0-2-62")[0].find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr"):
        etf_data = []

        etf_data.append(str(etf_row.find_elements(By.TAG_NAME, "td")[3].text).split(" ")[0])  # Ticker
        etf_data.append(etf_row.find_element(By.TAG_NAME, "a").text)  # Name
        etf_data.append(etf_row.find_element(By.TAG_NAME, "a").get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
