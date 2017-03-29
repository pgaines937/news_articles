import scrapy

"""google_news_spider.py

first from the command line, start up the python http server with the command:

            sudo python3 -m http.server 80

Then Ctrl+Z to detach, and 'bg' to run the server in the background

run with:
            scrapy crawl google_news
            scrapy runspider google_news_spider.py -o google_news.jl
            scrapy crawl google_news -o google_news.json

after the spider runs, export the database:
            mongoexport --db scrapy --collection articles4 --out articles.json"""

class GoogleNewsSpider(scrapy.Spider):
    name = "google_news"
    start_urls = [
        'http://www.pgaines937.io/google0.html',
        'http://www.pgaines937.io/google1.html',
        'http://www.pgaines937.io/google2.html',
        'http://www.pgaines937.io/google3.html',
        'http://www.pgaines937.io/google4.html',
        'http://www.pgaines937.io/google5.html'
    ]

    def parse(self, response):
        for news_headline in response.css('div.ires'):
            yield {
                'headline_text': news_headline.xpath('//a/text()').extract(),
                'url': news_headline.xpath('//a/@href').extract()
            }