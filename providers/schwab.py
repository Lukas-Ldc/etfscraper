"""
This is the Charles Schwab module.
Main website URL: https://www.schwab.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_schwab(driver):
    """This function retrieves ETFs from the following URL: https://www.schwab.com/research/etfs/tools/schwab-etfs

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.schwab.com/research/etfs/tools/schwab-etfs")

    # Waiting for the presence of the iframe and switching to it.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "schwab-responsive-iframe--no-wrapper")))
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "schwab-responsive-iframe--no-wrapper").find_element(By.TAG_NAME, "iframe"))

    # Waiting for the presence of the button.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.ID, "ctrlSchwabETFsTypes11")))

    # For all ETF tables.
    for etf_table in ["ctrlSchwabETFsTypes11", "ctrlSchwabETFsTypes31", "ctrlSchwabETFsTypes51", "ctrlSchwabETFsTypes71"]:
        driver.find_element(By.ID, etf_table).click()

        # Waiting for the presence of the table.
        WebDriverWait(driver, timeout=10).until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "mvloader")))

        # For each row in the table.
        for etf_row in driver.find_element(By.CLASS_NAME, "mvActiveContainer").find_elements(By.CLASS_NAME, "SchwabETFsSymbolModule"):
            etf_data = []

            etf_data.append(etf_row.find_element(By.CLASS_NAME, "symbol").find_element(By.TAG_NAME, "a").text)  # Ticker
            etf_data.append(etf_row.find_element(By.CLASS_NAME, "description").find_elements(By.TAG_NAME, "div")[0].text)  # Name
            etf_data.append(etf_row.find_element(By.CLASS_NAME, "symbol").find_element(By.TAG_NAME, "a").get_attribute('href'))  # URL

            etf_list.append(etf_data)

    return etf_list
