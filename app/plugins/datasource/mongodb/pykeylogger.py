from pymongo import MongoClient
from core.apis.datasource.annotations import Annotations
from bson.json_util import dumps
from datetime import datetime

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
        result = collection.find({ "start": {"$gte" : datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S'), "$lt": datetime.strptime(endDate, '%Y-%m-%d %H:%M:%S')}})
        return dumps(result)

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
