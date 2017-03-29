import scrapy
import time
import datetime

"""nasdaq_spider.py

run with:
            scrapy crawl nasdaq
            scrapy runspider nasdaq_spider.py -o nasdaq.jl
            scrapy crawl nasdaq -o nasdaq.json

after the spider runs, export the database:
            mongoexport --db scrapy --collection articles3 --out articles.json"""


class NasdaqSpider(scrapy.Spider):
    name = "nasdaq"
    start_urls = [
        'http://www.nasdaq.com/symbol/goog/news-headlines',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=2',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=3',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=4',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=5',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=6',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=7',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=8',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=9',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=10',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=11',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=12',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=13',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=14',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=15',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=16',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=17',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=18',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=19',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=20',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=21',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=22',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=23',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=24',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=25',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=26',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=27',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=28',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=29',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=30',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=31',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=32',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=33',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=34',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=35',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=36',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=37',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=38',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=39',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=40',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=41',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=42',
        'http://www.nasdaq.com/symbol/goog/news-headlines?page=43'
    ]

    def parse(self, response):
        for news_headline in response.css('div.news-headlines'):
            yield {
                'headline': news_headline.xpath('div/span/a/text()').extract(),
                'url': news_headline.xpath('div/span/a/@href').extract()
                #'timestamp': news_headline.xpath('div/small/text()').extract()
            }

        """next_page = response.css('li.quotes_content_left_lb_NextPage a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)"""