# -*- coding: utf-8 -*-
import codecs
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from anekdot.items import AnekdotItem


class AnekdotDaySpider(scrapy.Spider):
    name = 'anekdot_day'
    allowed_domains = ['anekdot.ru']
    start_urls = ['https://www.anekdot.ru/release/anekdot/day']

    def parse(self, response):

        root = Selector(response)

        # item = AnekdotItem()
        # item['url'] = response.url

        # item['content'] = root.xpath('//div[@class="topicbox"]/div[@class="text"]/text()').extract()

        # return item

        for anekdot_xtext in root.xpath('//div[@class="topicbox"]/div[@class="text"]'):
            print('\n'.join(anekdot_xtext.xpath('./text()').extract()))
            print('------------')
