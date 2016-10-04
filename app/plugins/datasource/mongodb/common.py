from datetime import datetime
from pymongo import MongoClient
from bson.json_util import dumps
import ujson

class Common:

    def formatDatetime(self, epoch):
        return datetime.utcfromtimestamp(epoch / 1e3).isoformat()

    def getDatabase(self):
        client = MongoClient()
        return client.dssvisualizer

    def formatOutput(self, cursor):
        bsonResult = dumps(cursor)
        objects = ujson.loads(bsonResult)
        return objects
