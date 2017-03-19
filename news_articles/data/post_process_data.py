#!/usr/bin/env python3
#
# Post Processor for Google Finance Spider scraped data
# Name: Patrick Gaines
#

from pymongo import MongoClient
from pandas.io.json import json_normalize
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


def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


"""Flattens the nested articles into a dict"""
def flatten_articles():
    try:
        article_data = {}
        for articles in database.articles.find():
            for key, values in articles.items():
                print(key, values)
               #for value in values:
                #    print(key, value)
                    #article_data[key] = value
            #    article_data.
            #if len(articles['url']) is not 0:
            #    print(articles['url'])


    except Exception as e:
        print("Error: " + str(e))


if __name__ == '__main__':
    try:
        # Getting Connection from MongoDB
        conn = MongoClient(MONGODB_URI)

        # Connecting to MongoDB
        print("Connecting to database in MongoDB named as " + MONGODB_DATABASE)
        database = conn[MONGODB_DATABASE]

        # Creating a collection named businessCollection in MongoDB
        print("Creating a collection in " + MONGODB_DATABASE + " named as " + FLATTENED_COLLECTION)
        collection = database[FLATTENED_COLLECTION]

        # Loading BusinessCollection from a json file to MongoDB
        #print("Loading NASDAQ_GOOG.json file into the " + QUANDL_DATA + " present inside the database " + MONGODB_DATABASE)
        #loadJsonIntoDB("NASDAQ_GOOG.json", collection)

        # Flatten the articles collection
        print("Flattening the articles collection")
        flatten_articles()

    except Exception as detail:
        print("Error ==> ", detail)
