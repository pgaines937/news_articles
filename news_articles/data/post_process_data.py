#!/usr/bin/env python3
#
# Post Processor for Google Finance Spider scraped data
# Name: Patrick Gaines
#

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
FINAL_DATASET = 'dataset'


def convert_json_to_csv(filename, collection):
    try:
        item_list = []

        page = open(filename, "r", encoding="utf8")
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
        for item in item_list:
            item.pop('_id')
            for key, values in item.items():
                for value in values:
                   item_dict[key].append(value)

        print(list(item_dict.keys()))
        print(list(item_dict.values()))

        values_list = item_dict.values()

        index = 0
        record = [[], [], [], [], [], []]
        object_list = []
        while values_list[0]:
        for key_list in values_list:
            record[index] = key_list.pop(index)




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
        print("Loading " + ARTICLES_DATA + " file in the " + ARTICLES_COLLECTION + " present inside the database " + MONGODB_DATABASE)
        convert_json_to_csv(ARTICLES_DATA, articles_flattened_collection)

        # Loading stock data from a json file to MongoDB
        #print("Loading " + STOCK_DATA + " file in the " + STOCK_COLLECTION + " present inside the database " + MONGODB_DATABASE)
        #convert_json_to_csv(STOCK_DATA, stock_collection)

        # Flatten the articles collection
        #print("Flattening the articles collection")
        #flatten_articles()

    except Exception as detail:
        print("Error ==> ", detail)
