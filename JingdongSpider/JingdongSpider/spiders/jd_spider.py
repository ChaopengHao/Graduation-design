import scrapy
from scrapy.selector import Selector

class JDSpider(scrapy.Spider):
    name = "jdspider"
    start_urls = []
    for i in range(1,2):
        url = "http://list.jd.com/list.html?cat=9987,653,655&page=" + str(i)
        print url
        start_urls.append(url)

    def parse(self, response):
        selector = Selector(response=response)
        goods = selector.xpath('//li[@class="gl-item"]')
        for good in goods:
            print good.xpath('./div/div[@class="p-name"]/a/em/text()').extract()
            print good.xpath('./div/div[@class="p-shop"]/@data-shop_name').extract()
            print good.xpath('./div/div[@class="p-img"]/a/@href').extract()
            print good.xpath('./div/@data-sku').extract()
            # print good.xpath('./div/div[@class="p-name"]/a/i').extract()
            # print good.xpath('./div/div[@class="p-name"]').extract()
            # print good.xpath('./div/div[@class="p-price"]').extract()
            print "good"