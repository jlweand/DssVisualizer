from bson import ObjectId
from datetime import datetime
# from plugins.datasource.mongodb.annotations import Annotations
from plugins.datasource.mongodb.common import Common
# from pprint import pprint

from bson.json_util import dumps

class TsharkProtocol:

    def getTsharkProtocolCollection(self):
        return Common().getDatabase().tsharkProtocol

    def importTsharkProtocolData(self, json):
        collection = self.getTsharkProtocolCollection()
        result = collection.insert_many(json)
        return len(result.inserted_ids)

    # select data by date range of the 'start' column
    def selectTsharkProtocolData(self, startDate, endDate):
        collection = self.getTsharkProtocolCollection()
        findJson = { "start": {"$gte" : datetime.strptime(startDate, Common().getDatetimeFormatString()), "$lt": datetime.strptime(endDate, Common().getDatetimeFormatString())}}
        cursor = collection.find(findJson)
        return dumps(cursor)

    # select single data point
    def selectTsharkProtocolDataById(self, dataId):
        collection = self.getTsharkProtocolCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return dumps(cursor)

    # add a fixedData record to this data point
    def insertFixedTsharkProtocolData(self, dataId, oldDataId, content, className, title, start):
        collection = self.getTsharkProtocolCollection()
        insertId = {"_id": ObjectId(dataId)}
        insertText = {"$set": {"id": oldDataId, "content": content , "className": className, "title": title, "start": start}}
        result = collection.update_one(insertId, insertText)
        return result.modified_count

    # update a previously 'fixed' record.
    def updateFixedTsharkProtocolData(self, dataId, content, className, title, start):
        collection = self.getTsharkProtocolCollection()
        updateId = {"_id" : ObjectId(dataId)}
        updateText = {"$set": {"id": oldDataId, "content": content , "className": className, "title": title, "start": start}}
        result = collection.update_one(updateId, updateText)
        return result.modified_count

    # delete the fixedData
    def deleteFixedTsharkProtocolData(self, dataId):
        collection = self.getTsharkProtocolCollection()
        deleteId = {"_id" : ObjectId(dataId)}
        deleteText = {"$unset": {"id": "", "content": "", "className": "", "title": "", "start": ""}}
        result = collection.update_one(deleteId, deleteText)
        return result.modified_count
