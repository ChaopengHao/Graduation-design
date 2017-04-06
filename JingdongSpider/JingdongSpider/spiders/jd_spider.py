# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from JingdongSpider.items import JingdongspiderItem

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
            jingdong_good = JingdongspiderItem()
            jingdong_good["name"] = good.xpath('./div/div[@class="p-name"]/a/em/text()').extract()
            jingdong_good["shop_name"] = good.xpath('./div/div[@class="p-shop"]/@data-shop_name').extract()
            jingdong_good["link"] = good.xpath('./div/div[@class="p-img"]/a/@href').extract()
            jingdong_good["photo"] = good.xpath('./div/div[@class="p-img"]/a/img/@data-lazy-img').extract()
            jingdong_good["ID"] = good.xpath('./div/@data-sku').extract()
            # print good.xpath('./div/div[@class="p-name"]/a/i').extract()
            # print good.xpath('./div/div[@class="p-name"]').extract()
            # print good.xpath('./div/div[@class="p-price"]').extract()
            url = "http:" + jingdong_good["link"][0]
            yield scrapy.Request(url=url, callback=parse_good, meta={"item":jingdong_good})

    def parse_good(self, response):
        item = response.meta["item"]
