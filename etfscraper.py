"""
Execute this file to make the script work.
It uses the modules of the "providers" folder to retrieve the data.
The final results are saved in the "output" folder.
"""
from os import path
from csv import writer, QUOTE_ALL
from datetime import datetime
from selenium import webdriver

from providers.globalx import etf_globalx
from providers.ishares import etf_ishares
from providers.vanguard import etf_vanguard

# Initialisations
headers = ["TICKER", "NAME", "URL"]
etfs_list = []
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)

# Scraping
for etf in etf_globalx(driver):
    etfs_list.append(etf)
for etf in etf_ishares(driver):
    etfs_list.append(etf)
for etf in etf_vanguard(driver):
    etfs_list.append(etf)

driver.quit()

# File saving
date = str(datetime.now()).split(".")[0].replace(" ", "T")
csv_file = path.join(path.dirname(__file__), "output", f"etfscraper_{date}.csv")

with open(csv_file, mode='w', encoding="utf-8") as file:
    csvwriter = writer(file, delimiter=",", quoting=QUOTE_ALL)
    csvwriter.writerow(headers)
    csvwriter.writerows(etfs_list)
