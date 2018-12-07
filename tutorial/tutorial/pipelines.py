# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from tutorial.items import BookItem, NovelItem

MYSQL_HOSTS = '120.79.137.249'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_PORT = '3306'
MYSQL_DB = 'crawl'

conn = pymysql.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB)
cursor = conn.cursor()

class TutorialPipeline(object):
    def process_item(self, item, spider):
        # if isinstance(item, BookItem):
        #     sql = "insert into ebook_book(title,link, author, words, update_time, status)\
        #         values (%s,%s,%s,%s,%s,%s)"
        #     for i in range(1, 10):
        #         try:
        #             cursor.execute(sql, (item['title'], item['link'],
        #                                  item['author'], item['words'], item['update_time'], item['status']))
        #             conn.commit()
        #             break
        #         except:
        #             conn.rollback()
        # elif isinstance(item, NovelItem):
        #     sql = """
        #         insert into ebook_novel(book_name,chapter_link,
        #             chapter_name, chapter_content)
        #         values (%s,%s,%s,%s)
        #         """
        #     for i in range(1, 10):
        #         try:
        #             cursor.execute(sql, (item['book_name'], item['chapter_link'],
        #                                  item['chapter_name'], item['chapter_content']))
        #             conn.commit()
        #             break
        #         except:
        #             conn.rollback()
        return item
