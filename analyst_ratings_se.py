from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
# import re
import time

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\where\you\download\the\chromedriver.exe')
driver = webdriver.Chrome(r'C:\Users\Eugene\chromedriver.exe')

with open('spx_tickers.csv', 'r') as f:
    tickers = f.readlines()
    tickers = [ticker.strip() for ticker in tickers]

csv_file = open('rec_rtng.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

urls = [f'https://finance.yahoo.com/quote/{ticker}/analysis?p={ticker}' for ticker in tickers]

writer.writerow(['rec_rtng','analysts'])

for url in urls:
    stats_dict = {}
    
    driver.get(url)
    time.sleep(1)    
    rec_rtng = driver.find_element_by_xpath('//*[@id="Col2-4-QuoteModule-Proxy"]/div/section/div/div/div[1]').text
    analysts = driver.find_element_by_xpath('//*[@id="Col2-5-QuoteModule-Proxy"]/div/section/a/h2').text

    stats_dict['rec_rtng'] = rec_rtng
    stats_dict['analysts'] = analysts
    
    writer.writerow(stats_dict.values())

csv_file.close()
driver.close()

