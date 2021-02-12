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

csv_file = open('yhoo_stats.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

urls = [f'https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}' for ticker in tickers]

writer.writerow(['ticker','px2sales'])

for url in urls:
    stats_dict = {}
    
    driver.get(url)
    # time.sleep(2)

    tk = driver.find_element_by_xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1').text
    px2sales = driver.find_element_by_xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody/tr[6]/td[2]').text

    stats_dict['tk'] = tk
    stats_dict['px2sales'] = px2sales

    writer.writerow(stats_dict.values())

csv_file.close()
driver.close()


# //*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody/tr[6]/td[2]
# //*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1
# //*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1