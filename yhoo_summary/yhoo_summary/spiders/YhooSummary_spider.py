from scrapy import Spider
from yhoo_summary.items import YhooSummaryItem

with open('spx_tickers.csv', 'r') as f:
    tickers = f.readlines()
    tickers = [ticker.strip() for ticker in tickers]

class YhooSummary(Spider):
    name = "YhooSummary_spider"
    allowed_urls = ['https://finance.yahoo.com/']
    start_urls = [f'https://finance.yahoo.com/quote/{ticker}?p={ticker}' for ticker in tickers]

    def parse(self, response):
        rows = response.xpath('//td[@class="Ta(end) Fw(600) Lh(14px)"]//text()')

        name_tk = response.xpath('//h1[@class="D(ib) Fz(18px)"]//text()').extract()
        _52wkrange = rows[5].extract()
        avg_vol = rows[7].extract()
        mktcap = rows[8].extract()
        beta = rows[9].extract()
        PE = rows[10].extract()
        EPS = rows[11].extract()
        DivYld = rows[15].extract()
        _1YTargetEst = rows[17].extract()

        item = YhooSummaryItem()
        item['name_tk'] = name_tk
        item['_52wkrange'] = _52wkrange
        item['avg_vol'] = avg_vol
        item['mktcap'] = mktcap
        item['beta'] = beta
        item['PE'] = PE
        item['EPS'] = EPS
        item['DivYld'] = DivYld
        item['_1YTargetEst'] = _1YTargetEst

        yield item




        # 52wkrange = response.xpath('//td[@data-test="FIFTY_TWO_WK_RANGE-value"]//text()').extract()
        # avg_vol = response.xpath('//td[@data-test="AVERAGE_VOLUME_3MONTH-value"]//text()').extract()
        # mktcap = 
        # beta = scrapy.Field()
        # PE = scrapy.Field()
        # EPS = scrapy.Field()
        # 1YTargetEst = scrapy.Field()