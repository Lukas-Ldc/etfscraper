"""
Execute this file to make the script work.
It uses the modules of the "providers" folder to retrieve the data.
The final results are saved in the "output" folder.
"""
from os import path
from csv import writer, QUOTE_ALL
from datetime import datetime
from selenium import webdriver

from providers.advisorshares import etf_advisorshares
from providers.amundi import etf_amundi
from providers.ark import etf_ark
from providers.charlesschwab import etf_charlesschwab
from providers.defiance import etf_defiance
from providers.dimensional import etf_dimensional
from providers.direxion import etf_direxion
from providers.dws import etf_dws
from providers.etc import etf_etc
from providers.etfmg import etf_etfmg
from providers.expat import etf_expat
from providers.fidelity import etf_fidelity
from providers.finex import etf_finex
from providers.firsttrust import etf_firsttrust
from providers.franklintempleton import etf_franklintempleton_irl, etf_franklintempleton_usa
from providers.globalx import etf_globalx
from providers.goldmansachs import etf_goldmansachs_gbr, etf_goldmansachs_usa
from providers.hanetf import etf_hanetf
from providers.horizons import etf_horizons
from providers.indexiq import etf_indexiq
from providers.innovator import etf_innovator
from providers.invesco import etf_invesco_irl, etf_invesco_usa
from providers.ishares import etf_ishares_gbr, etf_ishares_usa
from providers.jpmorgan import etf_jpmorgan_irl, etf_jpmorgan_usa
from providers.lgim import etf_lgim
from providers.pacer import etf_pacer
from providers.proshares import etf_proshares
from providers.sprott import etf_sprott
from providers.ssga import etf_ssga_irl, etf_ssga_usa
from providers.ubs import etf_ubs
from providers.vaneck import etf_vaneck_irl, etf_vaneck_usa
from providers.vanguard import etf_vanguard_irl, etf_vanguard_usa
from providers.wisdomtree import etf_wisdomtree

# Initialisations
headers = ["TICKER", "NAME", "URL"]
etfs_list = []
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)


def concatenaclear(etflist):
    """This function takes a list of ETFs and appends it to the global ETF list and then clear the driver's cookies.

    Arguments:
        etflist (list): The ETF list to append to the global list.
    """
    for etf in etflist:
        etfs_list.append(etf)
    driver.delete_all_cookies()


# Scraping
concatenaclear(etf_advisorshares(driver))
concatenaclear(etf_amundi(driver))
concatenaclear(etf_ark(driver))
concatenaclear(etf_charlesschwab(driver))
concatenaclear(etf_defiance(driver))
concatenaclear(etf_dimensional(driver))
concatenaclear(etf_direxion(driver))
concatenaclear(etf_dws(driver))
concatenaclear(etf_etc(driver))
concatenaclear(etf_etfmg(driver))
concatenaclear(etf_expat(driver))
concatenaclear(etf_fidelity(driver))
concatenaclear(etf_finex(driver))
concatenaclear(etf_firsttrust(driver))
concatenaclear(etf_franklintempleton_irl(driver))
concatenaclear(etf_franklintempleton_usa(driver))
concatenaclear(etf_globalx(driver))
concatenaclear(etf_goldmansachs_gbr(driver))
concatenaclear(etf_goldmansachs_usa(driver))
concatenaclear(etf_hanetf(driver))
concatenaclear(etf_horizons(driver))
concatenaclear(etf_indexiq(driver))
concatenaclear(etf_innovator(driver))
concatenaclear(etf_invesco_irl(driver))
concatenaclear(etf_invesco_usa(driver))
concatenaclear(etf_ishares_gbr(driver))
concatenaclear(etf_ishares_usa(driver))
concatenaclear(etf_jpmorgan_irl(driver))
concatenaclear(etf_jpmorgan_usa(driver))
concatenaclear(etf_lgim(driver))
concatenaclear(etf_pacer(driver))
concatenaclear(etf_proshares(driver))
concatenaclear(etf_sprott(driver))
concatenaclear(etf_ssga_irl(driver))
concatenaclear(etf_ssga_usa(driver))
concatenaclear(etf_ubs(driver))
concatenaclear(etf_vaneck_irl(driver))
concatenaclear(etf_vaneck_usa(driver))
concatenaclear(etf_vanguard_irl(driver))
concatenaclear(etf_vanguard_usa(driver))
concatenaclear(etf_wisdomtree(driver))

# Closing driver
driver.quit()

# File saving
date = str(datetime.now()).split(".")[0].replace(" ", "T")
csv_file = path.join(path.dirname(__file__), "output", f"etfscraper_{date}.csv")

with open(csv_file, mode='w', encoding="utf-8") as file:
    csvwriter = writer(file, delimiter=",", quoting=QUOTE_ALL)
    csvwriter.writerow(headers)
    csvwriter.writerows(etfs_list)
