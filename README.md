Scrapy project for gathering news article headlines and metadata.

Uses a customized MongoDBPipeline that fetches the article text with the newspaper module and generates a sentiment polarity value with the textblob module.

# Run Spider

    cd news_articles
    scrapy crawl google_finance