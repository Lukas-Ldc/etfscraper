"""
Execute this file to make the script work.
It uses the modules of the "providers" folder to retrieve the data.
The final results are saved in the "output" folder.
"""
import traceback
from os import path
from time import sleep
from csv import writer, QUOTE_ALL
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchWindowException

from providers.advisorshares import etf_advisorshares
from providers.allianz import etf_allianz
from providers.amundi import etf_amundi
from providers.ark import etf_ark
from providers.capitalgroup import etf_capitalgroup
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
from providers.wisdomtree import etf_wisdomtree_irl, etf_wisdomtree_usa

# Initialisations
etf_functions = [
    etf_advisorshares,
    etf_allianz,
    etf_amundi,
    etf_ark,
    etf_capitalgroup,
    etf_charlesschwab,
    etf_defiance,
    etf_dimensional,
    etf_direxion,
    etf_dws,
    etf_etc,
    etf_etfmg,
    etf_expat,
    etf_fidelity,
    etf_finex,
    etf_firsttrust,
    etf_franklintempleton_irl,
    etf_franklintempleton_usa,
    etf_globalx,
    etf_goldmansachs_gbr,
    etf_goldmansachs_usa,
    etf_hanetf,
    etf_horizons,
    etf_indexiq,
    etf_innovator,
    etf_invesco_irl,
    etf_invesco_usa,
    etf_ishares_gbr,
    etf_ishares_usa,
    etf_jpmorgan_irl,
    etf_jpmorgan_usa,
    etf_lgim,
    etf_pacer,
    etf_proshares,
    etf_sprott,
    etf_ssga_irl,
    etf_ssga_usa,
    etf_ubs,
    etf_vaneck_irl,
    etf_vaneck_usa,
    etf_vanguard_irl,
    etf_vanguard_usa,
    etf_wisdomtree_irl,
    etf_wisdomtree_usa
]

etfs_list = []
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
wdwait = WebDriverWait(driver, timeout=20)  # Adjust this timeout depending on your bandwidth (maximum loading time of an element on a page).

# Scraping
STOP = False
for func in etf_functions:
    ATTEMPTS = 3

    while ATTEMPTS > 0:
        func_str = str(func).split(' ')[1]
        try:
            results = func(driver, wdwait)
            for etf in results:
                etfs_list.append(etf)
            if len(results) < 1:
                print(f"-------- No results came from {func_str} --------")
            else:
                print(f"-- Results from {func_str} saved --")
            driver.delete_all_cookies()
            ATTEMPTS = 0
            sleep(3)  # Adjust this timeout depending on your bandwidth (time before scraping the next page).

        except NoSuchWindowException:
            print(f"-------- Window closed when {func_str} was running, results skipped and program stopped --------")
            print(traceback.format_exc())
            STOP = True
            ATTEMPTS = 0

        except Exception:
            print(f"-------- Exception for {func_str}, attempt {4-ATTEMPTS}, results skipped after 3 try --------")
            if ATTEMPTS == 1:
                print(traceback.format_exc())
            ATTEMPTS -= 1
            driver.delete_all_cookies()
            sleep(10)

    if STOP:
        break

driver.quit()

# File saving
if len(etfs_list) > 1:
    date = str(datetime.now()).split(".")[0].replace(" ", "T")
    csv_file = path.join(path.dirname(__file__), "output", f"etfscraper_{date}.csv")

    with open(csv_file, mode='w', encoding="utf-8") as file:
        csvwriter = writer(file, delimiter=",", quoting=QUOTE_ALL)
        csvwriter.writerow(["TICKER", "NAME", "URL"])
        csvwriter.writerows(etfs_list)
