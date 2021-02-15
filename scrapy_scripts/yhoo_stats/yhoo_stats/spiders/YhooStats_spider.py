from scrapy import Spider
from yhoo_stats.items import YhooStatsItem

with open('spx_tickers.csv', 'r') as f:
    tickers = f.readlines()
    tickers = [ticker.strip() for ticker in tickers]

class YhooStats(Spider):
    name = "YhooStats_spider"
    allowed_urls = ['https://finance.yahoo.com/']
    start_urls = [f'https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}' for ticker in tickers]

    def parse(self, response):
        
        name_tk = response.xpath('//h1[@class="D(ib) Fz(18px)"]//text()').extract()
        shares_out = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[9].extract()
        sh_float = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[10].extract()
        insiders = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[11].extract()
        institution = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[12].extract()
        sh_short = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[13].extract()
        short_ratio = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[14].extract()
        short_to_float = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[15].extract()
        short_to_out = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[16].extract()
        fwd_div = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[18].extract()
        fwd_div_yld = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[19].extract()
        _5Y_div_yld = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[22].extract()
        payout_ratio = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[23].extract()
        profit_margin = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[30].extract()
        oper_margin = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[31].extract()
        ROA = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[32].extract()
        ROE = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[33].extract()
        Rev = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[34].extract()
        rev_sh = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[35].extract()
        Q_rev_gr = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[36].extract()
        gross_profit = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[37].extract()
        EBITDA = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[38].extract()
        NI = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[39].extract()
        EPS = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[40].extract()
        Q_earnings_gr = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[41].extract()
        cash = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[42].extract()
        cash_per_sh = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[43].extract()
        debt = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[44].extract()
        debt_to_eq = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[45].extract()
        curr_ratio = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[46].extract()
        bv_per_sh = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[47].extract()
        op_cf = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[48].extract()
        fcf = response.xpath('//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]//text()')[49].extract()

        item = YhooStatsItem()
        item['name_tk'] = name_tk
        item['shares_out'] = shares_out
        item['sh_float'] = sh_float
        item['insiders'] = insiders
        item['institution'] = institution
        item['sh_short'] = sh_short
        item['short_ratio'] = short_ratio
        item['short_to_float'] = short_to_float
        item['short_to_out'] = short_to_out
        item['fwd_div'] = fwd_div
        item['fwd_div_yld'] = fwd_div_yld
        item['_5Y_div_yld'] = _5Y_div_yld
        item['payout_ratio'] = payout_ratio
        item['profit_margin'] = profit_margin
        item['oper_margin'] = oper_margin
        item['ROA'] = ROA
        item['ROE'] = ROE
        item['Rev'] = Rev
        item['rev_sh'] = rev_sh
        item['Q_rev_gr'] = Q_rev_gr
        item['gross_profit'] = gross_profit
        item['EBITDA'] = EBITDA
        item['NI'] = NI
        item['EPS'] = EPS
        item['Q_earnings_gr'] = Q_earnings_gr
        item['cash'] = cash
        item['cash_per_sh'] = cash_per_sh
        item['debt'] = debt
        item['debt_to_eq'] = debt_to_eq
        item['curr_ratio'] = curr_ratio
        item['bv_per_sh'] = bv_per_sh
        item['op_cf'] = op_cf
        item['fcf'] = fcf

        yield item