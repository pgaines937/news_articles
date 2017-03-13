import scrapy
import time
import datetime

from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.response import get_base_url

"""google_finance_spider.py

run with: scrapy runspider google_finance_spider.py -o google_finance.jl
            scrapy crawl google_finance -o google_finance.json"""


class GoogleFinanceSpider(scrapy.Spider):
    name = "google_finance"
    allowed_domains = ["www.google.com"]
    start_urls = [
        'https://www.google.com/finance/company_news?q=NASDAQ%3AGOOG&startdate=2017-1-01&enddate=2017-2-01&ei=-8zFWLnSFoe62Aam_4XoCQ',
    ]

    #rules = (
    #    Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('.//td[@class="nav_b"]/a/@href',)), callback="parse", follow=True),
    #)

    def parse(self, response):
        for news_headline in response.css('div.news'):
            yield {
                'headline': news_headline.css('span.name').xpath('a/text()').extract(),
                'url': news_headline.css('span.name').xpath('a/@href').extract(),
                'date': news_headline.css('span.date').xpath('text()').extract()
            }

        #next_page = response.xpath('.//td[@class="nav_b"]/a/@href').extract_first()
        next_page = response.css('td.nav_b a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)