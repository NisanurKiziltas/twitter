from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import keys 
import time
import csv
import pandas as pd

driver_path = "D:\PROGRAM SETUP\chormedriver.exe"
browser = webdriver.Chrome(driver_path)

browser.get("https://www.google.com.tr/")
yazı_girişi = browser.find_element_by_css_selector(".gLFyf.gsfi")
yazı_girişi.send_keys("twitter deep learning türkiye")
time.sleep(2)
yazı_girişi.sent_keys(keys.ENTER)