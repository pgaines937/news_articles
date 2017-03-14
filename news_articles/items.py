# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, Join
from scrapy.utils.markup import replace_escape_chars
import time
import datetime

class NewsArticle(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    headline = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()
    article_text = scrapy.Field()
    sentiment_polarity = scrapy.Field()
    sentiment_subjectivity = scrapy.Field()
