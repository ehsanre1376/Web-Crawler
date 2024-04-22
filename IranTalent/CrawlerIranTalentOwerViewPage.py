import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from tqdm import tqdm


def CrawlerIranTalentOwerViewPage(url):
    try:
        site = requests.get(url)
        soup = BeautifulSoup(site.text, "html.parser")

    except Exception:
        time.sleep(2)
        try:
            site = requests.get(url)
            soup = BeautifulSoup(site.text, "html.parser")

        except Exception:
            time.sleep(5)
            site = requests.get(url)
            soup = BeautifulSoup(site.text, "html.parser")

    # Site---------------------------------------------
    courses = soup.select(
        "body > app-root > div > div > div > div > company-branding > div > div.row.d-flex.flex-wrap > div.col-md-9.col-xs-12 > brand-overview > div > form > div.card-section.company-information.padding-top-16.ng-untouched.ng-pristine.ng-valid > div > div > div > div > div.col-md-7.col-xs-6 > a"
    )
    try:
        siteLink = courses[0].get("href")
    except Exception:
        siteLink = "#"

    # CEO-------------------------------------------------------
    courses = soup.select(
        "body > app-root > div > div > div > div > company-branding > div > div.row.d-flex.flex-wrap > div.col-md-9.col-xs-12 > brand-overview > div > form > div.card-section.company-information.padding-top-16.ng-untouched.ng-pristine.ng-valid > div > div > div > div > div.col-md-7.col-xs-6 > p"
    )
    try:
        ceo = courses[0].text.strip()
    except Exception:
        ceo = None

    # CreatDate------------------------------------------------------------
    courses = soup.select(
        "body > app-root > div > div > div:nth-child(2) > div > company-branding > div > div.row.d-flex.flex-wrap > div.col-md-9.col-xs-12 > brand-overview > div > form > div.card-section.company-information.padding-top-16.ng-untouched.ng-pristine.ng-valid > div > div > div:nth-child(1) > div:nth-child(3) > div.col-md-7.col-xs-6 > p"
    )
    try:
        date = courses[0].text.strip()
    except Exception:
        date = None

    # address-------------------------------------
    courses = soup.select(
        "body > app-root > div > div > div:nth-child(2) > div > company-branding > div > div.row.d-flex.flex-wrap > div.col-md-9.col-xs-12 > brand-overview > div > form > div.card-section.company-information.padding-top-16.ng-untouched.ng-pristine.ng-valid > div > div > div:nth-child(2) > div:nth-child(2) > div.col-md-7.col-xs-6 > p"
    )
    try:
        address = courses[0].text.strip()
    except Exception:
        address = None

    # Location------------------------------------------------
    courses = soup.select(
        "body > app-root > div > div > div:nth-child(2) > div > company-branding > div > div.row.d-flex.flex-wrap > div.col-md-9.col-xs-12 > brand-overview > div > form > div.card-section.company-information.padding-top-16.ng-untouched.ng-pristine.ng-valid > div > div > div:nth-child(2) > div:nth-child(1) > div.col-md-7.col-xs-6 > p"
    )
    try:
        Location = courses[0].text.strip().replace(",", "")
    except Exception:
        Location = None

    # Titles-----------------------------------------------
    courses = soup.select(
        "body > app-root > div > div > div:nth-child(2) > div > company-branding > div > div.row.d-flex.flex-wrap > div.col-md-9.col-xs-12 > brand-overview > div > form > div > h1"
    )
    try:
        Titles = courses[0].text.strip().replace("درباره ", "")
    except Exception:
        Titles = None

    # Industrial-----------------------------------------------
    courses = soup.select(
        "body > app-root > div > div > div:nth-child(2) > div > company-branding > div > div.row.d-flex.flex-wrap > div.col-md-9.col-xs-12 > brand-overview > div > form > div.card-section.company-information.padding-top-16.ng-untouched.ng-pristine.ng-valid > div > div > div:nth-child(1) > div:nth-child(4) > div.col-md-7.col-xs-6 > p"
    )
    try:
        Industrial = courses[0].text.strip()
    except Exception:
        Industrial = None

    # personnel------------------------------------------------------
    courses = soup.select(
        "body > app-root > div > div > div:nth-child(2) > div > company-branding > div > div.row.d-flex.flex-wrap > div.col-md-9.col-xs-12 > brand-overview > div > form > div.card-section.company-information.padding-top-16.ng-untouched.ng-pristine.ng-valid > div > div > div:nth-child(1) > div:nth-child(5) > div.col-md-7.col-xs-6 > p"
    )
    try:
        personnel = courses[0].text.strip()
    except Exception:
        personnel = None
    # ------------------------------------------------------
    return siteLink, ceo, date, address, Location, Titles, Industrial, personnel
