from pymongo import MongoClient
from core.apis.datasource.annotations import Annotations
from bson import ObjectId
from bson.json_util import dumps
from datetime import datetime
import ujson

class PyKeyLogger:

    def getDatabase(self):
        client = MongoClient()
        return client.dssvisualizer

    def importKeypressData(self, json):
        collection = self.getDatabase().keypressData
        result = collection.insert_many(json)
        return len(result.inserted_ids)

    def importClick(self, json):
        collection = self.getDatabase().click
        result = collection.insert_many(json)
        return len(result.inserted_ids)

    def importTimed(self, json):
        collection = self.getDatabase().timed
        result = collection.insert_many(json)
        return len(result.inserted_ids)

# Keypress #
    # select data by date range of the 'start' column
    def selectKeyPressData(self, startDate, endDate):
        collection = self.getDatabase().keypressData
        findJson = { "start": {"$gte" : datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S'), "$lt": datetime.strptime(endDate, '%Y-%m-%d %H:%M:%S')}}
        cursor = collection.find(findJson)
        return self.formatOutput(cursor, False)

    def selectKeyPressDataById(self, dataId):
        collection = self.getDatabase().keypressData
        cursor = collection.find({"_id": ObjectId(dataId)})
        return self.formatOutput(cursor, False)

    # insert a new record.  This record must be tied to the original record.
    # the oldDataId will be a new 'column' called sourceId. it is of type ObjectId
    def insertFixedKeyPressData(self, oldDataId, content, className, start):
        return 0

    # update a previously 'fixed' record. Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def updateFixedKeyPressData(self, dataId, content, className, start):
        return 0

    # delete a record.  Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def deleteFixedKeyPressData(self, dataId):
        return 0

# Click #
    # select data by date range of the 'start' column
    def selectClickData(self, startDate, endDate):
        return 0

    # insert a new record.  This record must be tied to the original record.
    # the oldDataId will be a new 'column' called sourceId. it is of type ObjectId
    def insertFixedClickData(self, oldDataId, content, _type, classname, title, start, end):
        return 0

    # update a previously 'fixed' record. Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def updateFixedClickData(self, dataId, content, _type, classname, title, start, end):
        return 0

    # delete a record.  Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def deleteFixedClickData(self, dataId):
        return 0

# Timed #
    # select data by date range of the 'start' column
    def selectTimedData(self, startDate, endDate):
        return 0

    # insert a new record.  This record must be tied to the original record.
    # the oldDataId will be a new 'column' called sourceId. it is of type ObjectId
    def insertFixedTimedData(self, oldDataId, content, _type, classname, title, start, end):
        return 0

    # update a previously 'fixed' record. Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def updateFixedTimedData(self, dataId, content, _type, classname, title, start, end):
        return 0

    # delete a record.  Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def deleteFixedTimedData(self, dataId):
        return 0


    def formatOutput(self, cursor, hasEndDate):
        bsonResult = dumps(cursor)
        objects = ujson.loads(bsonResult)
        for obj in objects:
            obj = self.fixTheDates(obj, hasEndDate)

        return objects

    def fixTheDates(self, obj, hasEndDate):
        obj["start"] = self.formatDatetime(obj["start"]["$date"])
        obj["metadata"]["importDate"] = self.formatDatetime(obj["metadata"]["importDate"]["$date"])

        if(hasEndDate):
            obj["end"] = self.formatDatetime(obj["end"]["$date"])

        return obj

    def formatDatetime(self, epoch):
        return datetime.fromtimestamp(epoch / 1e3).isoformat()
