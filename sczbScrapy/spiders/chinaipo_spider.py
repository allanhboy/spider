import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

class ChinaipoSpider(CrawlSpider):
    name = "ChinaipoSpider"
    allowed_domains = ['chinaipo.com']
    start_urls = ['http://www.chinaipo.com/']

    rules = (
        Rule(LinkExtractor(allow=('/stock/\d*$',)), follow=True),

        Rule(LinkExtractor(allow=('/stock/\d*/profile.html',)),
             callback='parse_profile',
             follow=True),
    )

    def parse_profile(self, response):
        pass