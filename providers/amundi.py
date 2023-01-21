"""
This is the Amundi module.
Main website URL: https://www.amundietf.com/?skip=true
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


def etf_amundi(driver, wdwait):
    """This function retrieves ETFs from the following URL: https://www.amundietf.fr/fr/professionnels/produits-etf/recherche

    Arguments:
        driver (WebDriver): The web browser that allows to interact with web pages.
        wdwait (WebDriverWait): The timeout that allows to wait for explicit conditions.
    Returns:
        etf_list (list): The results of the scraping.
    """
    etf_list = []
    driver.get("https://www.amundietf.fr/fr/professionnels/produits-etf/recherche")

    # Interaction with legal disclaimer.
    wdwait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[data-profile="INSTIT"]'))).click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "confirmDisclaimer"))).click()

    # Interaction with cookies.
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "CookiesDisclaimerRibbonV1-Settings"))).click()
    wdwait.until(expected_conditions.element_to_be_clickable((By.ID, "CookiesDisclaimerPopupV1-Save"))).click()

    # Waiting for the presence of a line in the table.
    wdwait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, "tbody")))

    # Retrieval of web page elements.
    select_next_a = driver.find_element(By.CSS_SELECTOR, '[aria-label="Next"]')
    select_next_li = driver.find_elements(By.CSS_SELECTOR, ".pagination li")

    # For each page.
    while True:

        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", select_next_a)

        # For each row in the table.
        for etf_row in driver.find_elements(By.CSS_SELECTOR, "tbody tr"):
            etf_data = []
            tag_a_list = etf_row.find_elements(By.TAG_NAME, "a")

            etf_data.append(tag_a_list[0].text)  # Ticker
            etf_data.append(str(tag_a_list[2].text).split("\n")[0])  # Name
            etf_data.append(tag_a_list[0].get_attribute("href"))  # URL

            etf_list.append(etf_data)

        if 'disabled' in select_next_li[-1].get_attribute('class'):
            break
        else:
            select_next_a.click()

    return etf_list
