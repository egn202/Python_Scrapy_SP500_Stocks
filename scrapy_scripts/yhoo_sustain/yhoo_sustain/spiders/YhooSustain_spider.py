from scrapy import Spider
from yhoo_sustain.items import YhooSustainItem

with open('spx_tickers.csv', 'r') as f:
    tickers = f.readlines()
    tickers = [ticker.strip() for ticker in tickers]

class YhooSustain(Spider):
    name = "YhooSustain_spider"
    allowed_urls = ['https://finance.yahoo.com/']
    start_urls = [f'https://finance.yahoo.com/quote/{ticker}/sustainability?p={ticker}' for ticker in tickers]

    def parse(self, response):
        name_tk = response.xpath('//h1[@class="D(ib) Fz(18px)"]//text()').extract()
        esg_score = response.xpath('//div[@class="Fz(36px) Fw(600) D(ib) Mend(5px)"]/text()').extract()
        env_risk = response.xpath('//div[@class="D(ib) Fz(23px) smartphone_Fz(22px) Fw(600)"]/text()')[0].extract()
        social_risk = response.xpath('//div[@class="D(ib) Fz(23px) smartphone_Fz(22px) Fw(600)"]/text()')[1].extract()
        gov_risk = response.xpath('//div[@class="D(ib) Fz(23px) smartphone_Fz(22px) Fw(600)"]/text()')[2].extract()

        item = YhooSustainItem()
        item['name_tk'] = name_tk
        item['esg_score'] = esg_score
        item['env_risk'] = env_risk
        item['social_risk'] = social_risk
        item['gov_risk'] = gov_risk
        
        yield item
