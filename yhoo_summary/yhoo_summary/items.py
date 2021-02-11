# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YhooSummaryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    px = scrapy.Field()
    name_tk = scrapy.Field()
    _52wkrange = scrapy.Field()
    avg_vol = scrapy.Field()
    mktcap = scrapy.Field()
    beta = scrapy.Field()
    PE = scrapy.Field()
    EPS = scrapy.Field()
    DivYld = scrapy.Field()
    _1YTargetEst = scrapy.Field()