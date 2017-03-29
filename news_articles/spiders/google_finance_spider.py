import scrapy

"""google_finance_spider.py

run with: scrapy runspider google_finance_spider.py -o google_finance.jl
            scrapy crawl google_finance -o google_finance.json

after the spider runs, export the database:
            mongoexport --db scrapy --collection articles2 --out articles.json"""

class GoogleFinanceSpider(scrapy.Spider):
    name = "google_finance"
    allowed_domains = ["www.google.com"]
    start_urls = [
        'http://www.nasdaq.com/symbol/goog/news-headlines'
    ]

    def parse(self, response):
        for news_headline in response.css('div.news'):
            yield {
                'headline_text': news_headline.css('a').xpath('text()').extract(),
                'url': news_headline.css('a').xpath('@href').extract()
            }