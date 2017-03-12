import scrapy
import time
import datetime

"""nasdaq_spider.py

run with: scrapy runspider nasdaq_spider.py -o nasdaq.jl
            scrapy crawl nasdaq -o nasdaq.json"""


class NasdaqSpider(scrapy.Spider):
    name = "nasdaq"
    start_urls = [
        'http://www.nasdaq.com/symbol/goog/news-headlines',
    ]

    def parse(self, response):
        for news_headline in response.css('div.news-headlines'):
            yield {
                'headline': news_headline.xpath('div.news-headlines/div/span/a/text()').extract(),
                'url': news_headline.xpath('div.news-headlines/div/span/a/@href').extract(),
                'timestamp': news_headline.xpath('div.news-headlines/div/small/text()').extract()
            }

        next_page = response.css('li.quotes_content_left_lb_NextPage a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)