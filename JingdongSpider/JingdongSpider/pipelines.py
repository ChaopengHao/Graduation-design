# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
import json
import codecs
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
import os
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.utils.project import get_project_settings
from scrapy import log
import chardet
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('scraped_data_utf8.json', 'w', encoding='utf-8')
        self.file.write('[')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line+',')
        return item

    def close_spider(self, spider):
        self.file.seek(-1, os.SEEK_END)
        self.file.truncate();
        self.file.write(']')
        self.file.close()


SETTINGS = get_project_settings()
class MySQLPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.stats)

    def __init__(self, stats):
        # Instantiate DB
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                                            host=SETTINGS['MYSQL_HOST'],
                                            user=SETTINGS['MYSQL_USER'],
                                            passwd=SETTINGS['MYSQL_PASSWD'],
                                            port=SETTINGS['MYSQL_PORT'],
                                            db=SETTINGS['MYSQL_DBNAME'],
                                            charset='utf8',
                                            use_unicode=False,
                                            cursorclass=MySQLdb.cursors.DictCursor
                                            )
        self.stats = stats
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        """ Cleanup function, called after crawing has finished to close open
            objects.
            Close ConnectionPool. """
        self.dbpool.close()

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._insert_record, item)
        query.addErrback(self._handle_error)
        return item

    def _insert_record(self, tx, item):
        sql = "insert into web_jdbookitem(book_id,title,url,keywords,description,img,channel,tag,sub_tag,value,price) " \
                  "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params = (item["_id"], item["title"], item["url"], item["keywords"], item["description"], item["img"],
                      item["channel"],item["tag"], item["sub_tag"], item["value"], item["price"])
        tx.execute(sql, params)

    def _handle_error(self, e):
        log.err(e)