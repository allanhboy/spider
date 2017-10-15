import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class ChinaipoSpider(CrawlSpider):
    name = "ChinaipoSpider"
    allowed_domains = ['chinaipo.com']
    start_urls = ['http://www.chinaipo.com/']

    rules = (
        Rule(LinkExtractor(allow=('/stock/\d*$',)), follow=True),

        Rule(LinkExtractor(allow=('/stock/\d*/profile.html',)),
             callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
