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

csv_file = open('change.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

urls = [f'https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}' for ticker in tickers]

writer.writerow(['ticker','change'])

for url in urls:
    stats_dict = {}
    
    driver.get(url)
    time.sleep(1)    
    ticker = driver.find_element_by_xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1').text
    change = driver.find_element_by_xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[2]/div/div[1]/div/div/table/tbody/tr[2]/td[2]').text
    # analysts = driver.find_element_by_xpath('//*[@id="Col2-5-QuoteModule-Proxy"]/div/section/a/h2').text

    stats_dict['ticker'] = ticker
    stats_dict['change'] = change
    # stats_dict['analysts'] = analysts
    
    writer.writerow(stats_dict.values())

csv_file.close()
driver.close()

