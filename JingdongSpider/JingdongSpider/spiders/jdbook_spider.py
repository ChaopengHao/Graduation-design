# -*- coding: utf-8 -*-

# import scrapy # 可以用这句代替下面三句，但不推荐
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy import Request
import json
import scrapy
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor

from JingdongSpider.items import JDBookItem  # 如果报错是pyCharm对目录理解错误的原因，不影响


class JDBookSpider(Spider):
    name = "jdbook"
    allowed_domains = ["jd.com", "pm.3.cn"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = [
        # 起始url，这里设置为从最大tid开始，向0的方向迭代
        "http://item.jd.com/11678007.html"
    ]


    # 用来保持登录状态，可把chrome上拷贝下来的字符串形式cookie转化成字典形式，粘贴到此处
    cookies = {}

    # 发送给服务器的http头信息，有的网站需要伪装出浏览器头进行爬取，有的则不需要
    headers = {
        # 'Connection': 'keep - alive',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }

    # 对请求的返回进行处理的配置
    meta = {
        'dont_redirect': True,  # 禁止网页重定向
        'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
    }

    def get_next_url(self, old_url):
        '''
        description: 返回下次迭代的url
        :param oldUrl: 上一个爬去过的url
        :return: 下次要爬取的url
        '''
        # 传入的url格式：http://www.heartsong.top/forum.php?mod=viewthread&tid=34
        list = old_url.split('/')  #用等号分割字符串
        old_item_id = int(list[3].split('.')[0])
        new_item_id = old_item_id - 1
        if new_item_id == 0:  # 如果tid迭代到0了，说明网站爬完，爬虫可以结束了
            return
        new_url = '/'.join([list[0], list[1], list[2], str(new_item_id)+ '.html'])  # 构造出新的url
        return str(new_url)  # 返回新的url

    def start_requests(self):
        """
        这是一个重载函数，它的作用是发出第一个Request请求
        :return:
        """
        # 带着headers、cookies去请求self.start_urls[0],返回的response会被送到
        # 回调函数parse中
        yield Request(self.start_urls[0], callback=self.parse, headers=self.headers, cookies=self.cookies, meta=self.meta)

    def parse(self, response):
        """
        用以处理主题贴的首页
        :param response:
        :return:
        """
        selector = Selector(response)
        item = JDBookItem()
        extractor = LxmlLinkExtractor(allow=r'http://item.jd.com/\d.*html')
        link = extractor.extract_links(response)
        try:
            item['_id'] =  response.url.split('/')[3].split('.')[0]
            item['url'] = response.url
            item['title'] = selector.xpath('/html/head/title/text()').extract()[0][0:-16]
            item['keywords'] = selector.xpath('/html/head/meta[2]/@content').extract()[0]
            item['description'] = selector.xpath('/html/head/meta[3]/@content').extract()[0]
            item['img'] = 'http:' + selector.xpath('//*[@id="spec-n1"]/img/@src').extract()[0]
            item['channel'] = selector.xpath('//*[@id="root-nav"]/div/div/strong/a/text()').extract()[0]
            item['tag'] = selector.xpath('//*[@id="root-nav"]/div/div/span[1]/a[1]/text()').extract()[0]
            item['sub_tag'] = selector.xpath('//*[@id="root-nav"]/div/div/span[1]/a[2]/text()').extract()[0]
            item['value'] = selector.xpath('//*[@id="root-nav"]/div/div/span[1]/a[2]/text()').extract()[0]
            # comments = list()
            # node_comments = selector.xpath('//*[@id="hidcomment"]/div')
            # for node_comment in node_comments:
            #     comment = dict()
            #     node_comment_attrs = node_comment.xpath('.//div[contains(@class, "i-item")]')
            #     for attr in node_comment_attrs:
            #         url = attr.xpath('.//div/strong/a/@href').extract()[0]
            #         comment['url'] = 'http:' + url
            #         content = attr.xpath('.//div/strong/a/text()').extract()[0]
            #         comment['content'] = content
            #         time = attr.xpath('.//div/span[2]/text()').extract()[0]
            #         comment['time'] = time
            #     comments.append(comment)
            # item['comments'] = comments
            s1 = str(item['_id'])
            price_url = "http://pm.3.cn/prices/pcpmgets?callback=jQuery&skuids=" + s1 + "&origin=2"
            print price_url
            yield Request(price_url, meta={'item': item}, callback=self.parse_price, headers=self.headers, cookies=self.cookies,)
        except Exception, ex:
            print 'something wrong', str(ex)

        next_url = self.get_next_url(response.url)  # response.url就是原请求的url
        if next_url != None:  # 如果返回了新的url
            yield Request(next_url, callback=self.parse, headers=self.headers, cookies=self.cookies, meta=self.meta)

    def parse_price(self, response):
        item = response.meta['item']
        print item
        templ = response.body.split('jQuery([')
        s = templ[1][:-4]  # 获取到需要的json内容
        js = json.loads(str(s))  # js是一个map
        if js.has_key('pcp'):
            item['price'] = js['pcp']
        else:
            item['price'] = js['p']
        yield item