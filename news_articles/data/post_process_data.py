#!/usr/bin/python3.5
#
# Post Processor for Google Finance Spider scraped data
# Name: Patrick Gaines
#

from pymongo import MongoClient
from .. import settings
import json

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
    pass


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
        print("Loading NASDAQ_GOOG.json file into the " + QUANDL_COLLECTION + " present inside " + settings.MONGODB_DATABASE)
        loadJsonIntoDB("testData.json", collection)

        # Flatten the articles collection
        print("Flattening the articles collection")
        flatten_articles()

    except Exception as detail:
        print("Error ==> ", detail)
