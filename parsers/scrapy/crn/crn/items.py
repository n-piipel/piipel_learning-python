# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrnItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    ownership = scrapy.Field()
    num_employees = scrapy.Field()
    telnum = scrapy.Field()
    site = scrapy.Field()
    email = scrapy.Field()
    reg_employees = scrapy.Field()
    city = scrapy.Field()
