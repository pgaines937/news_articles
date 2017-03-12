import scrapy

from scrapy.contrib.loader import XPathItemLoader
from news_articles.items import NewsArticle

"""nasdaq_spider.py

run with: scrapy runspider nasdaq_spider.py -o nasdaq.jl
            scrapy crawl nasdaq -o nasdaq.json"""


class NasdaqSpider(scrapy.Spider):
    name = "nasdaq"
    start_urls = [
        'http://www.nasdaq.com/symbol/goog/news-headlines',
    ]

    def parse(self, response):
        items = []
        l = XPathItemLoader(item=NewsArticle(), response=response)
        l.add_css('news-headlines')
        l.add_xpath('headline', 'div/span/a/text()')
        l.add_xpath('url', 'div/span/a/@href')
        l.add_xpath('timestamp', 'div/small/text()')
        items.append(l.load_item())
        return items