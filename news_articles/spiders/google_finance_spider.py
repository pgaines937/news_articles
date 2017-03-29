import scrapy

"""google_finance_spider.py

run with: scrapy runspider google_finance_spider.py -o google_finance.jl
            scrapy crawl google_finance -o google_finance.json

after the spider runs, export the database:
            mongoexport --db scrapy --collection articles --out articles.json"""

class GoogleFinanceSpider(scrapy.Spider):
    name = "google_finance"
    allowed_domains = ["www.google.com"]
    start_urls = [
        'https://www.google.com/finance/company_news?q=NASDAQ:GOOG&ei=jufFWMGjCYayjAG925mYDA&startdate=2016-12-01&enddate=2017-01-01&start=0&num=100',
        'https://www.google.com/finance/company_news?q=NASDAQ:GOOG&ei=jufFWMGjCYayjAG925mYDA&startdate=2017-01-01&enddate=2017-02-01&start=0&num=100',
        'https://www.google.com/finance/company_news?q=NASDAQ:GOOG&ei=jufFWMGjCYayjAG925mYDA&startdate=2017-02-01&enddate=2017-03-01&start=0&num=100',
        'https://www.google.com/finance/company_news?q=NASDAQ:GOOG&ei=jufFWMGjCYayjAG925mYDA&startdate=2017-03-01&enddate=2017-04-01&start=0&num=100'
        'https://www.google.com/search?q=google&biw=1920&bih=950&tbm=nws&ei=BxfcWP7PJMme0gKQ5rKwCQ&start=0&num=100'
        'https://www.google.com/search?q=google&biw=1920&bih=950&tbm=nws&ei=BxfcWP7PJMme0gKQ5rKwCQ&start=100&num=100'
        'https://www.google.com/search?q=google&biw=1920&bih=950&tbm=nws&ei=BxfcWP7PJMme0gKQ5rKwCQ&start=200&num=100'
        'https://www.google.com/search?q=google&biw=1920&bih=950&tbm=nws&ei=BxfcWP7PJMme0gKQ5rKwCQ&start=300&num=100'
        'https://www.google.com/search?q=google&biw=1920&bih=950&tbm=nws&ei=BxfcWP7PJMme0gKQ5rKwCQ&start=400&num=100'
        'https://www.google.com/search?q=google&biw=1920&bih=950&tbm=nws&ei=BxfcWP7PJMme0gKQ5rKwCQ&start=500&num=100'

    ]

    def parse(self, response):
        for news_headline in response.css('div.news'):
            yield {
                'headline_text': news_headline.css('a#n-cn-').xpath('text()').extract(),
                'url': news_headline.css('a#n-cn-').xpath('@href').extract()
            }