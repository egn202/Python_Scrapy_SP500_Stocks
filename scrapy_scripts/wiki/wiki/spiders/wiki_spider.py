# -*- coding: utf-8 -*-
from scrapy import Spider, Request #added request.enables passing url requests
from wiki.items import WikiItem #in order to say wiki.items, an init file needs to be present
#import wiki item from the items.py module

class WikiSpider(Spider):
    name = 'wiki_spider' #'projectname_spider' will be used to call the spider later in another module
    allowed_urls = ['https://en.wikipedia.org'] #needs to be a list. spider can only go to these websites
    start_urls = ['https://en.wikipedia.org/wiki/List_of_S%26P_500_companies']
    #
    def parse(self, response): 
        # Find all the table rows
        #response object passes all the website info to the script 
        # rows = response.xpath('//*[@id="mw-content-text"]/div/table/thead/tbody/tr')#[1:]
        # rows = response.xpath('//*[@id="mw-content-text"]/div/table/tbody/tr')[1:]
        rows = response.xpath('//*[@id="constituents"]/tbody/tr')[1:]

        for row in rows:
            # Relative xpath for all the other columns
            symbol = row.xpath('./td[1]/a/text()').extract_first()
            name = row.xpath('./td[2]/a/text()').extract_first()
            sector = row.xpath('./td[4]/text()').extract_first()
            sub_industry = row.xpath('./td[5]/text()').extract_first()
            hq = row.xpath('./td[6]/a/text()').extract_first()
            dt_add = row.xpath('./td[7]/text()').extract_first()
            founded = row.xpath('./td[9]/text()').extract_first().strip()

            item = WikiItem()
            item['symbol'] = symbol
            item['name'] = name
            item['sector'] = sector
            item['sub_industry'] = sub_industry
            item['hq'] = hq
            item['dt_add'] = dt_add
            item['founded'] = founded
            yield item
