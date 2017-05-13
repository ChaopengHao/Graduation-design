# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongspiderItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()  # 商品链接
    ID = scrapy.Field()  # 商品ID
    name = scrapy.Field()  # 商品名字
    comment_num = scrapy.Field()  # 评论人数
    shop_name = scrapy.Field()  # 店家名字
    price = scrapy.Field()  # 价钱
    commentVersion = scrapy.Field()  # 为了得到评论的地址需要该字段
    score1count = scrapy.Field()  # 评分为1星的人数
    score2count = scrapy.Field()  # 评分为2星的人数
    score3count = scrapy.Field()  # 评分为3星的人数
    score4count = scrapy.Field()  # 评分为4星的人数
    score5count = scrapy.Field()  # 评分为5星的人数
    photo =scrapy.Field()   #
    resolution = scrapy.Field()
    front_camera = scrapy.Field()
    rear_camera = scrapy.Field()
    brand = scrapy.Field()
    core_num = scrapy.Field()


class JDBookItem(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    keywords = scrapy.Field()
    description = scrapy.Field()
    img = scrapy.Field()
    channel = scrapy.Field()
    tag = scrapy.Field()
    sub_tag = scrapy.Field()
    value = scrapy.Field()
    comments = scrapy.Field()
    price = scrapy.Field()



