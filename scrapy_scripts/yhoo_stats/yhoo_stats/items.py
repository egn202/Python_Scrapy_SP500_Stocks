# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YhooStatsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_tk = scrapy.Field()
    shares_out = scrapy.Field()
    sh_float = scrapy.Field()
    insiders = scrapy.Field()
    institution = scrapy.Field()
    sh_short = scrapy.Field()
    short_ratio = scrapy.Field()
    short_to_float = scrapy.Field()
    short_to_out = scrapy.Field()
    fwd_div = scrapy.Field()
    fwd_div_yld = scrapy.Field()
    _5Y_div_yld = scrapy.Field()
    payout_ratio = scrapy.Field()
    profit_margin = scrapy.Field()
    oper_margin = scrapy.Field()
    ROA = scrapy.Field()
    ROE = scrapy.Field()
    Rev = scrapy.Field()
    rev_sh = scrapy.Field()
    Q_rev_gr = scrapy.Field()
    gross_profit = scrapy.Field()
    EBITDA = scrapy.Field()
    NI = scrapy.Field()
    EPS = scrapy.Field()
    Q_earnings_gr = scrapy.Field()
    cash = scrapy.Field()
    cash_per_sh = scrapy.Field()
    debt = scrapy.Field()
    debt_to_eq = scrapy.Field()
    curr_ratio = scrapy.Field()
    bv_per_sh = scrapy.Field()
    op_cf = scrapy.Field()
    fcf = scrapy.Field()

