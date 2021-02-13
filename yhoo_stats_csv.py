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

writer.writerow(['ticker','ev','trail_pe','fwd_pe','peg','px2sales','px2book','ev2rev','ev2ebitda'])

for url in urls:
    stats_dict = {}
    
    driver.get(url)
    time.sleep(1)    
    tk = driver.find_element_by_xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1').text
    ev = driver.find_element_by_xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]').text
    trail_pe = driver.find_element_by_xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody/tr[3]/td[2]').text
    fwd_pe = driver.find_element_by_xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody/tr[4]/td[2]').text
    peg = driver.find_element_by_xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody/tr[5]/td[2]').text
    px2sales = driver.find_element_by_xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody/tr[6]/td[2]').text
    px2book = driver.find_element_by_xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody/tr[7]/td[2]').text
    ev2rev = driver.find_element_by_xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody/tr[8]/td[2]').text
    ev2ebitda = driver.find_element_by_xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[1]/div[2]/div/div[1]/div[1]/table/tbody/tr[9]/td[2]').text

    stats_dict['tk'] = tk
    stats_dict['ev'] = ev
    stats_dict['trail_pe'] = trail_pe
    stats_dict['fwd_pe'] = fwd_pe
    stats_dict['peg'] = peg
    stats_dict['px2sales'] = px2sales
    stats_dict['px2book'] = px2book
    stats_dict['ev2rev'] = ev2rev
    stats_dict['ev2ebitda'] = ev2ebitda

    writer.writerow(stats_dict.values())

csv_file.close()
driver.close()

