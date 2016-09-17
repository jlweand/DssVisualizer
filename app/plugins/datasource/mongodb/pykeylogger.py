import ujson
from pymongo import MongoClient

class PyKeyLogger:

    def __init__(self):
        client = MongoClient()
        db = client.jensTest

    def importKeypressData(json):
        collection = db.keypressData
        result = collection.insert_many(json)
        return len(result.inserted_ids)

    def importClick(json):
        collection = db.click
        result = collection.insert_one(json)
        return result.inserted_id

    def importTimed(json):
        collection = db.timed
        result = collection.insert_one(json)
        return result.inserted_id
