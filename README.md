Scrapy project for gathering news article headlines and metadata

# Start Scrapyd:
> scrapyd

# Deploy project to Scrapyd (http://localhost:6800)

    cd project
    scrapy deploy

# Run

Start a spider

    curl http://www.pgaines937.io:6800/schedule.json -d project=news_articles -d spider=nasdaq_spider

List spiders

    curl http://www.pgaines937.io:6800/listspiders.json?project=default

List jobs

    curl http://www.pgaines937.io:6800/listjobs.json?project=default

Cancel job

    curl http://www.pgaines937.io:6800/cancel.json -d project=news_articles -d job=4abb6c78fd1a11e28ed9fefdb24fae0a