"""
This is the Charles Schwab module.
Main website URL: https://www.schwab.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


def etf_charlesschwab(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://www.schwab.com/research/etfs/tools/schwab-etfs

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.schwab.com/research/etfs/tools/schwab-etfs")

    # Waiting for the presence of the iframe and switching to it.
    wdwait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, ".schwab-responsive-iframe--no-wrapper iframe")))

    # Waiting for the presence of the button.
    wdwait.until(expected_conditions.presence_of_element_located((By.ID, "ctrlSchwabETFsTypes11")))

    # For all ETF tables.
    for etf_table in ["ctrlSchwabETFsTypes11", "ctrlSchwabETFsTypes31", "ctrlSchwabETFsTypes51", "ctrlSchwabETFsTypes71"]:
        driver.find_element(By.ID, etf_table).click()

        # Waiting for the presence of the table.
        wdwait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "mvloader")))

        # For each row in the table.
        for etf_row in driver.find_elements(By.CSS_SELECTOR, ".mvActiveContainer .SchwabETFsSymbolModule"):
            etf_data = []
            select_symbol_a = etf_row.find_element(By.CSS_SELECTOR, ".symbol a")

            etf_data.append(select_symbol_a.text)  # Ticker
            etf_data.append(etf_row.find_element(By.CLASS_NAME, "description").find_elements(By.TAG_NAME, "div")[0].text)  # Name
            etf_data.append(select_symbol_a.get_attribute('href'))  # URL

            etf_list.append(etf_data)

    return etf_list
