# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WoolItem(scrapy.Item):
    title = scrapy.Field()
    category = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
