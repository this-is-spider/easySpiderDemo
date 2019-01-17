# -*- coding: utf-8 -*-
import scrapy,time
from wool.items import WoolItem


class WoolsSpider(scrapy.Spider):
    name = 'wools'
    allowed_domains = ['www.haoyangmao.cc']
    start_urls = ['http://www.haoyangmao.cc/page/1?s/']

    def parse(self, response):
        urls = response.css(".post-con h3 a::attr('href')").extract()
        for url in urls:
            time.sleep(1)
            yield scrapy.Request(url=url, callback=self.crawl_content)



    def crawl_content(self, response):
        item = WoolItem()
        item['title'] = response.css('h2 a::text').extract_first()
        item['category'] = response.css('.category a::text').extract_first()
        item['date'] = response.css('.date::text').extract_first()
        item['content'] = response.css('article p').extract()
        yield item