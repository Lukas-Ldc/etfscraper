"""
Execute this file to make the script work.
It uses the modules of the "providers" folder to retrieve the data.
The final results are saved in the "output" folder.
"""
from os import path
from csv import writer, QUOTE_ALL
from datetime import datetime
from selenium import webdriver

from providers.amundi import etf_amundi
from providers.charlesschwab import etf_charlesschwab
from providers.defiance import etf_defiance
from providers.dimensional import etf_dimensional
from providers.dws import etf_dws
from providers.fidelity import etf_fidelity
from providers.firsttrust import etf_firsttrust
from providers.globalx import etf_globalx
from providers.goldmansachs import etf_goldmansachs_gbr, etf_goldmansachs_usa
from providers.invesco import etf_invesco_irl, etf_invesco_usa
from providers.ishares import etf_ishares_gbr, etf_ishares_usa
from providers.jpmorgan import etf_jpmorgan_irl, etf_jpmorgan_usa
from providers.lgim import etf_lgim
from providers.proshares import etf_proshares
from providers.sprott import etf_sprott
from providers.vaneck import etf_vaneck_irl, etf_vaneck_usa
from providers.vanguard import etf_vanguard_irl, etf_vanguard_usa
from providers.wisdomtree import etf_wisdomtree

# Initialisations
headers = ["TICKER", "NAME", "URL"]
etfs_list = []
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)

# Scraping
for etf in etf_amundi(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()

for etf in etf_charlesschwab(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()

for etf in etf_defiance(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()

for etf in etf_dimensional(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()

for etf in etf_dws(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()

for etf in etf_fidelity(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()

for etf in etf_firsttrust(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()

for etf in etf_globalx(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()

for etf in etf_goldmansachs_gbr(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()
for etf in etf_goldmansachs_usa(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()

for etf in etf_invesco_irl(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()
for etf in etf_invesco_usa(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()

for etf in etf_ishares_gbr(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()
for etf in etf_ishares_usa(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()

for etf in etf_jpmorgan_irl(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()
for etf in etf_jpmorgan_usa(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()

for etf in etf_lgim(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()

for etf in etf_proshares(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()

for etf in etf_sprott(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()

for etf in etf_vaneck_irl(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()
for etf in etf_vaneck_usa(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()

for etf in etf_vanguard_irl(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()
for etf in etf_vanguard_usa(driver):
    etfs_list.append(etf)
driver.delete_all_cookies()

for etf in etf_wisdomtree(driver):
    etfs_list.append(etf)
driver.quit()

# File saving
date = str(datetime.now()).split(".")[0].replace(" ", "T")
csv_file = path.join(path.dirname(__file__), "output", f"etfscraper_{date}.csv")

with open(csv_file, mode='w', encoding="utf-8") as file:
    csvwriter = writer(file, delimiter=",", quoting=QUOTE_ALL)
    csvwriter.writerow(headers)
    csvwriter.writerows(etfs_list)
