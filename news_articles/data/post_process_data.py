#!/usr/bin/env python3
#
# Post Processor for Google Finance Spider scraped data
# Name: Patrick Gaines
#

from pymongo import MongoClient
import json

MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'scrapy'
MONGODB_COLLECTION = 'articles'
FLATTENED_COLLECTION = 'articles_flattened'
QUANDL_DATA = 'NASDAQ_GOOG.json'
FINAL_DATASET = 'dataset'

def loadJsonIntoDB(fileName, collection):
    try:
        page = open(fileName, "r")
        parsedJson = json.loads(page.read())
        for item in parsedJson:
            collection.insert(item)
    except Exception as e:
        print("Error: " + str(e))


"""Flattens the nested articles into a dict"""
def flatten_articles():
    try:
        pipe = [{"$project": {"url": 1, "publish_date": 1, "sentiment_subjectivity": 1, "sentiment_polarity": 1,
                              "headline_text": 1, "article_text": 1}}]
        result = database.articles.aggregate(pipeline=pipe)
        print(result)
    except Exception as e:
        print("Error: " + str(e))


if __name__ == '__main__':
    try:
        # Getting Connection from MongoDB
        conn = MongoClient(settings.MONGODB_URI)

        # Connecting to MongoDB
        print("Connecting to database in MongoDB named as " + settings.MONGODB_DATABASE)
        database = conn[settings.MONGODB_DATABASE]

        # Creating a collection named businessCollection in MongoDB
        print("Creating a collection in " + settings.MONGODB_DATABASE + " named as " + FLATTENED_COLLECTION)
        collection = database[FLATTENED_COLLECTION]

        # Loading BusinessCollection from a json file to MongoDB
        print("Loading NASDAQ_GOOG.json file into the " + QUANDL_DATA + " present inside " + settings.MONGODB_DATABASE)
        loadJsonIntoDB("NASDAQ_GOOG.json", collection)

        # Flatten the articles collection
        print("Flattening the articles collection")
        flatten_articles()

    except Exception as detail:
        print("Error ==> ", detail)
