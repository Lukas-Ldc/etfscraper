"""
This is the Innovator module.
Main website URL: https://www.innovatoretfs.com/
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


def etf_innovator(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://www.innovatoretfs.com/define/etfs/

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.innovatoretfs.com/define/etfs/#allproducts")

    # Waiting for the presence of a line in the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.XPATH, "//tbody[.//a]")))

    # Openning the menu.
    sleep(2)
    driver.execute_script("window.scrollTo(0, 0);")
    sleep(1)
    driver.find_element(By.ID, "siteNav").find_elements(By.TAG_NAME, "a")[1].click()
    sleep(1)
    for submenu in driver.find_element(By.ID, "siteNav").find_elements(By.CLASS_NAME, "collapsed"):
        submenu.click()

    # For each element in the menu.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, "#dropdown_nav_submenu li"):
        etf_data = []
        tag_a = etf_row.find_element(By.TAG_NAME, "a")

        try:
            etf_data.append(etf_row.find_element(By.TAG_NAME, "span").text)  # Ticker
            etf_data.append(tag_a.text)  # Name
            etf_data.append(tag_a.get_attribute("href"))  # URL

            etf_list.append(etf_data)

        except NoSuchElementException:
            pass

    # For each row in the table.
    for etf_row in driver.find_elements(By.CSS_SELECTOR, "#allproducts tr")[1:]:
        etf_data = []
        tag_a = etf_row.find_elements(By.TAG_NAME, "a")

        etf_data.append(tag_a[0].text)  # Ticker
        etf_data.append(tag_a[4].text)  # Name
        etf_data.append(tag_a[0].get_attribute("href"))  # URL

        etf_list.append(etf_data)

    return etf_list
