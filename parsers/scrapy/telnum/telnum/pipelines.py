# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TelnumPipeline(object):
    def process_item(self, item, spider):
        for i in range(len(item['tel_num'])):
            digit_num = ''
            for j in item['tel_num'][i]:
                if j.isdigit():
                    digit_num += j
            item['tel_num'][i] = digit_num
        return item
