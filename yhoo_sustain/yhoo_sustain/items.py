# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YhooSustainItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_tk = scrapy.Field()
    esg_score = scrapy.Field()
    env_risk = scrapy.Field()
    social_risk = scrapy.Field()
    gov_risk = scrapy.Field()
