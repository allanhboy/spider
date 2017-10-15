import scrapy

from myScrapy.items import XiaohuarItem

class XiaoHuarSpider(scrapy.spiders.Spider):
    name = "xiaohuar"
    allowed_domains = ["xiaohuar.com"]
    start_urls = [
        "http://www.xiaohuar.com/hua/"
    ]

    def parse(self, response):
        current_url = response.url
        body = response.body
        unicode_body = response.body_as_unicode()

        for sel in  response.xpath('//*[@id="list_img"]/div/div[1]/div'):       
            name = sel.xpath('div/div/span[@class="price"]/text()').extract()
            img = sel.xpath('div/div/a/img/@src').extract()
            school = sel.xpath('div/div/div/a/text()').extract();
            item = XiaohuarItem()
            item['name'] = name
            item['img'] = img
            item['school'] = school
            yield item