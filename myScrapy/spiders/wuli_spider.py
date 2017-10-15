import scrapy


class WuLiSpider(scrapy.spiders.Spider):
    name = "WuLiSpider"
    allowed_domains = ["qjfhealth.com"]
    start_urls = [
        "http://test.qjfhealth.com/"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta={
                'splash': {
                    'endpoint': 'render.html'
                }
            })

    def parse(self, response):
        print("================================")
        print(response.body_as_unicode())
        print("================================")
