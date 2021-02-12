# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class WikiItem(scrapy.Item):
    symbol = scrapy.Field()
    name = scrapy.Field()
    sector = scrapy.Field()
    sub_industry = scrapy.Field()
    hq = scrapy.Field()
    dt_add = scrapy.Field()
    founded = scrapy.Field()