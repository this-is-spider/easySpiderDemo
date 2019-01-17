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
            yield scrapy.Request(url=url, callback=self.crawl_content)

    def crawl_content(self, response):
        item = WoolItem()
        item['title'] = response.css('h2 a::text').extract_first()
        item['category'] = response.css('.category a::text').extract_first()
        item['date'] = response.css('.date::text').extract_first()
        item['content'] = response.css('article').extract_first()
        yield item

    def start_requests(self):
        base_url = 'http://www.haoyangmao.cc/page/'
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            url = base_url + str(page) + '?s'
            yield scrapy.Request(url, self.parse)