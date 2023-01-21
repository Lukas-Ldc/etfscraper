"""
This is the ProShares module.
Main website URL: https://www.proshares.com/
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


def etf_proshares(driver, wdwait):
    """This function retrieves ETFs from the following URLs: https://www.proshares.com/our-etfs/find-strategic-etfs and https://www.proshares.com/our-etfs/find-leveraged-and-inverse-etfs

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.proshares.com/our-etfs/find-strategic-etfs")

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.ID, "overviewBody")))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, "#overviewBody tr"):
        etf_data = []
        tag_a = etf_row.find_elements(By.TAG_NAME, "a")

        etf_data.append(tag_a[0].text)  # Ticker
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "td")[1].text)  # Name
        etf_data.append(tag_a[0].get_attribute('href'))  # URL

        etf_list.append(etf_data)

    driver.get("https://www.proshares.com/our-etfs/find-leveraged-and-inverse-etfs")

    # Waiting for the presence of the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.ID, "overviewBody")))

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, "#overviewBody tr"):
        etf_data = []
        tag_a = etf_row.find_elements(By.TAG_NAME, "a")

        etf_data.append(tag_a[0].text)  # Ticker
        etf_data.append(etf_row.find_elements(By.TAG_NAME, "td")[1].text)  # Name
        etf_data.append(tag_a[0].get_attribute('href'))  # URL

        etf_list.append(etf_data)

    return etf_list
