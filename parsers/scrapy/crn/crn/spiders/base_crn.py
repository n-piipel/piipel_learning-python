# -*- coding: utf-8 -*-
import codecs

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from crn.items import CrnItem


class BaseCrnSpider(CrawlSpider):
    name = 'base_crn'
    allowed_domains = ['crn.ru']
    start_urls = ['https://www.crn.ru/catalog/list.php']

    rules = (
        Rule(LinkExtractor(allow=('catalog/list\.php\?COMPANIES=.+')), follow=True),
        Rule(LinkExtractor(allow=('catalog/detail*',)), callback='parse_page'),
    )
    
    def parse_page(self, response):

    # start_urls = ['https://www.crn.ru/catalog/detail.php?ID=49289']

    # def parse(self, response):

        root = Selector(response)

        item = CrnItem()
        item['url'] = response.url
        try:
            item['name'] = root.xpath('//div[@id="comblok_info"]/../h1/text()').extract()[0]
        except IndexError:
            pass

        try:
            item['ownership'] = root.xpath(u'//b[contains(text(), "Форма собственности:")]/../../td[2]/text()').extract()[0]
        except IndexError:
            pass

        try:
            item['num_employees'] = root.xpath(u'//b[contains(text(), "Количество сотрудников:")]/../../td[2]/text()').extract()[0]
        except IndexError:
            pass

        try:
            item['telnum'] = root.xpath(u'//b[contains(text(), "Телефон:")]/../../td[2]/text()').extract()[0]
        except IndexError:
            pass

        try:
            item['site'] = root.xpath(u'//b[contains(text(), "Сайт:")]/../../td[2]/a/text()').extract()[0]
        except IndexError:
            pass

        try:
            item['email'] = root.xpath(u'//b[contains(text(), "Общий e-mail:")]/../../td[2]/a/text()').extract()[0]
        except IndexError:
            pass

        try:
            item['reg_employees'] = ('\n'.join(root.xpath(u'//h3[contains(text(), "Зарегистрированные сотрудники компании")]/../following-sibling::table[1]/tr/td/text()|b/text()').extract())).strip()
        except IndexError:
            pass

        try:
            item['city'] = root.xpath(u'//b[contains(text(), "Город:")]/../../td[2]/text()').extract()[0]
        except IndexError:
            pass

        return item
