import scrapy
import time
import datetime

"""google_finance_spider.py

run with: scrapy runspider google_finance_spider.py -o google_finance.jl
            scrapy crawl google_finance -o google_finance.json"""


class GoogleFinanceSpider(scrapy.Spider):
    name = "google_finance"
    start_urls = [
        'https://www.google.com/finance/company_news?q=NASDAQ:GOOG&ei=Xo_FWLm0IM7U2AbT8pvQDQ',
    ]

    def parse(self, response):
        for news_headline in response.css('div.news'):
            yield {
                'headline': news_headline.css('span.name').xpath('a/text()').extract(),
                'url': news_headline.css('span.name').xpath('a/@href').extract(),
                'date': news_headline.css('span.date').xpath('text()').extract()
            }

        next_page = response.css('td.nav_b a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)