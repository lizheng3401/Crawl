# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class NovelItem(scrapy.Item):
    chapter_name = scrapy.Field()
    chapter_link = scrapy.Field()
    title = scrapy.Field()
    chapter_content = scrapy.Field()

class BookItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link = scrapy.Field()
    author = scrapy.Field()
    words = scrapy.Field()
    update_time = scrapy.Field()
    status = scrapy.Field()
    chapters = scrapy.Field(NovelItem.fields)
