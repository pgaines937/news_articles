#!/usr/bin/env python3
#
# Post Processor for Google Finance Spider scraped data
# Name: Patrick Gaines
#
import datetime
from pymongo import MongoClient
import pandas as pd
import json
import csv

MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'scrapy'
ARTICLES_COLLECTION = 'articles'
ARTICLES_FLATTENED_COLLECTION = 'articles_flattened'
STOCK_COLLECTION = 'stock_prices'
ARTICLES_DATA = 'articles.json'
ARTICLES_CSV = 'articles.csv'
STOCK_DATA = 'NASDAQ_GOOG.json'
STOCK_CSV = 'NASDAQ_GOOG.csv'
FINAL_DATASET = 'dataset.csv'


def convert_json_to_csv(articles_json, articles_csv, dataset_csv):
    try:
        item_list = []

        page = open(articles_json, "r", encoding="utf8")
        json_str = page.read()
        print(json_str)
        data_list = list(json_str.split('\n'))
        print(data_list)
        for item in data_list:
            if item:
                parsed_json = json.loads(item)
                print(parsed_json)
                item_list.append(parsed_json)
        item_dict = item_list.pop(0)
        item_dict.pop('_id')
        item_dict.pop('url')
        item_dict.pop('headline_text')
        item_dict.pop('article_text')
        for item2 in item_list:
            item2.pop('_id')
            item2.pop('url')
            item2.pop('headline_text')
            item2.pop('article_text')
            for key, values in item2.items():
                for value in values:
                   item_dict[key].append(value)
        print(list(item_dict.keys()))
        print(list(item_dict.values()))

        flat_list_of_dicts = []
        max_index = len(item_dict.keys()) - 1
        while list(item_dict.values())[max_index]:
            #record = { "url" : None, "headline_text" : None, "publish_date" : None, "sentiment_subjectivity" : None, "sentiment_polarity" : None, "article_text" : None }
            record = { "publish_date" : None, "sentiment_subjectivity" : None, "sentiment_polarity" : None }
            for key, value in item_dict.items():
                record[key] = value.pop()
            flat_list_of_dicts.append(record)

        print(flat_list_of_dicts)

        with open(articles_csv, 'w+', encoding="utf8") as f:  # Just use 'w' mode in 3.x
            w = csv.writer(f)
            flat_list_of_dicts[0]['Date'] = 'None'
            w.writerow(flat_list_of_dicts[0].keys())
            for item3 in flat_list_of_dicts:
                if item3['publish_date']:
                    publish_date = item3['publish_date']['$date']
                    date_list = list(publish_date.split('T'))
                    item3['Date'] = date_list[0]
                    w.writerow(item3.values())

        a = pd.read_csv(articles_csv)
        b = pd.read_csv('NASDAQ_GOOG.csv')
        b = b.dropna(axis=1)
        merged = a.merge(b, on='Date')
        merged.to_csv(dataset_csv, index=False)

    except Exception as e:
        print("Error: " + str(e))


def flatten_articles():
    """Flattens the nested articles into a dict"""
    try:
        article_data = {}
        for articles in database.articles.find():
            for key, value in articles.items():
                print(key, value)
                if not key in article_data:
                    print("Creating list")
                    article_data[key] = []
                print("Appending list")
                article_data[key] += value
        print(article_data)
    except Exception as e:
        print("Error: " + str(e))


if __name__ == '__main__':
    try:
        # Getting Connection from MongoDB
        conn = MongoClient(MONGODB_URI)

        # Connecting to MongoDB
        print("Connecting to database in MongoDB named as " + MONGODB_DATABASE)
        database = conn[MONGODB_DATABASE]

        # Creating a collection named articles in MongoDB
        print("Creating a collection in " + MONGODB_DATABASE + " named as " + ARTICLES_COLLECTION)
        articles_collection = database[ARTICLES_COLLECTION]

        # Creating a collection named articles_flattened in MongoDB
        print("Creating a collection in " + MONGODB_DATABASE + " named as " + ARTICLES_FLATTENED_COLLECTION)
        articles_flattened_collection = database[ARTICLES_FLATTENED_COLLECTION]

        # Creating a collection named stock_prices in MongoDB
        print("Creating a collection in " + MONGODB_DATABASE + " named as " + STOCK_COLLECTION)
        stock_collection = database[STOCK_COLLECTION]

        # Loading stock data from a json file to MongoDB
        #print("Loading NASDAQ_GOOG.json file into the " + QUANDL_DATA + " present inside the database " + MONGODB_DATABASE)
        #loadJsonIntoDB("NASDAQ_GOOG.json", collection)

        # Loading stock data from a json file to MongoDB
        print("Converting articles to csv and cross joining on stock data")
        convert_json_to_csv('articles2.json', 'articles2.csv', 'dataset2.csv')
        convert_json_to_csv('articles3.json', 'articles3.csv', 'dataset3.csv')
        convert_json_to_csv('articles4.json', 'articles4.csv', 'dataset4.csv')

        dataset_files = ['dataset2.csv', 'dataset3.csv', 'dataset4.csv']
        df_list = []
        for filename in sorted(dataset_files):
            df_list.append(pd.read_csv(filename))
        full_df = pd.concat(df_list)
        full_df.to_csv('combined_dataset.csv')

        # Loading stock data from a json file to MongoDB
        #print("Loading " + STOCK_DATA + " file in the " + STOCK_COLLECTION + " present inside the database " + MONGODB_DATABASE)
        #convert_json_to_csv(STOCK_DATA, stock_collection)

        # Flatten the articles collection
        #print("Flattening the articles collection")
        #flatten_articles()

    except Exception as detail:
        print("Error ==> ", detail)
