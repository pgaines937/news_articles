import scrapy
import time
import datetime

from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

"""google_finance_spider.py

run with: scrapy runspider google_finance_spider.py -o google_finance.jl
            scrapy crawl google_finance -o google_finance.json"""


class GoogleFinanceSpider(CrawlSpider):
    name = "google_finance"
    start_urls = [
        'https://www.google.com/finance/company_news?q=NASDAQ%3AGOOG&startdate=2017-1-01&enddate=2017-2-01&ei=-8zFWLnSFoe62Aam_4XoCQ',
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('.//td[@class="nav_b"]',)), callback="parse", follow=True),
    )

    def parse(self, response):
        for news_headline in response.css('div.news'):
            yield {
                'headline': news_headline.css('span.name').xpath('a/text()').extract(),
                'url': news_headline.css('span.name').xpath('a/@href').extract(),
                'date': news_headline.css('span.date').xpath('text()').extract()
            }