import scrapy

class JDSpider(scrapy.Spider):
    name = "jdspider"
    start_urls = []
    for i in range(1,120):
        url = "http://list.jd.com/list.html?cat=9987,653,655&page=" + str(i)
        start_urls.append(url)

    def parse(self, response):
        pass