from scrapy import Spider
from yhoo_profile.items import YhooProfileItem

with open('spx_tickers.csv', 'r') as f:
    tickers = f.readlines()
    tickers = [ticker.strip() for ticker in tickers]

class YhooProfile(Spider):
    name = "YhooProfile_spider"
    allowed_urls = ['https://finance.yahoo.com/']
    start_urls = [f'https://finance.yahoo.com/quote/{ticker}/profile?p={ticker}' for ticker in tickers]

    def parse(self, response):
        
        name_tk = response.xpath('//h1[@class="D(ib) Fz(18px)"]//text()').extract()
        address = response.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[1]/div/div/p[1]/text()').extract()
        sector = response.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[1]/div/div/p[2]/span[2]/text()').extract()
        industry = response.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[1]/div/div/p[2]/span[4]/text()').extract()
        employees = response.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[1]/div/div/p[2]/span[6]/span/text()').extract()
        exec1_name = response.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/section[1]/table/tbody/tr[1]/td[1]/span/text()').extract()
        exec1_title = response.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/section[1]/table/tbody/tr[1]/td[2]/span/text()').extract()
        exec1_pay = response.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/section[1]/table/tbody/tr[1]/td[3]/span/text()').extract()
        exec1_born = response.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/section[1]/table/tbody/tr[1]/td[5]/span/text()').extract()
        exec2_name = response.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/section[1]/table/tbody/tr[2]/td[1]/span/text()').extract()
        exec2_title = response.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/section[1]/table/tbody/tr[2]/td[2]/span/text()').extract()
        exec2_pay = response.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/section[1]/table/tbody/tr[2]/td[3]/span/text()').extract()
        exec2_born = response.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/section[1]/table/tbody/tr[2]/td[5]/span/text()').extract()
        exec3_name = response.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/section[1]/table/tbody/tr[3]/td[1]/span/text()').extract()
        exec3_title = response.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/section[1]/table/tbody/tr[3]/td[2]/span/text()').extract()
        exec3_pay = response.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/section[1]/table/tbody/tr[3]/td[3]/span/text()').extract()
        exec3_born = response.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/section[1]/table/tbody/tr[3]/td[5]/span/text()').extract()
        govscore = response.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/section[3]/div/p/span[2]/text()').extract()

        item = YhooProfileItem()
        item['name_tk'] = name_tk
        item['address'] = address
        item['sector'] = sector
        item['industry'] = industry
        item['employees'] = employees
        item['exec1_name'] = exec1_name
        item['exec1_title'] = exec1_title
        item['exec1_pay'] = exec1_pay
        item['exec1_born'] = exec1_born
        item['exec2_name'] = exec2_name
        item['exec2_title'] = exec2_title
        item['exec2_pay'] = exec2_pay
        item['exec2_born'] = exec2_born
        item['exec3_name'] = exec3_name
        item['exec3_title'] = exec3_title
        item['exec3_pay'] = exec3_pay
        item['exec3_born'] = exec3_born
        item['govscore'] = govscore

        yield item
