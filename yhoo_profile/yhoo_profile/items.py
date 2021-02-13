# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YhooProfileItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_tk = scrapy.Field()
    address = scrapy.Field()
    sector = scrapy.Field()
    industry = scrapy.Field()
    employees = scrapy.Field()
    exec1_name = scrapy.Field()
    exec1_title = scrapy.Field()
    exec1_pay = scrapy.Field()
    exec1_born = scrapy.Field()
    exec2_name = scrapy.Field()
    exec2_title = scrapy.Field()
    exec2_pay = scrapy.Field()
    exec2_born = scrapy.Field()
    exec3_name = scrapy.Field()
    exec3_title = scrapy.Field()
    exec3_pay = scrapy.Field()
    exec3_born = scrapy.Field()
    govscore = scrapy.Field()


