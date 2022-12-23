"""
This is the First Trust module.
Main website URL: https://www.ftportfolios.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def etf_firsttrust(driver):
    """This function retrieves ETFs from the following URL: https://www.ftportfolios.com/Retail/etf/etflist.aspx

    Arguments:
        driver (WebDriver): The Selenium WebDriver used for scraping.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.ftportfolios.com/Retail/etf/etflist.aspx")

    # Waiting for the presence of the table.
    WebDriverWait(driver, timeout=10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "searchResults")))

    # For each table.
    for etf_table in driver.find_elements(By.CLASS_NAME, "searchResults"):

        # For each row in the table.
        for etf_row in etf_table.find_elements(By.TAG_NAME, "tr")[1:]:
            etf_data = []

            etf_data.append(etf_row.find_elements(By.TAG_NAME, "td")[1].text)  # Ticker
            etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].text)  # Name
            etf_data.append(etf_row.find_elements(By.TAG_NAME, "a")[0].get_attribute('href'))  # URL

            etf_list.append(etf_data)

    return etf_list
