from bson import ObjectId
from datetime import datetime
from plugins.datasource.mongodb.annotations import Annotations
from plugins.datasource.mongodb.common import Common
from pprint import pprint

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
        #findJson = {"start": {"$gte": datetime.strptime(startDate, Common().getDatetimeFormatString()), "$lt": datetime.strptime(endDate, Common().getDatetimeFormatString())}}
        findJson = { "start": {"$gte" : startDate, "$lte": endDate}}
        cursor = collection.find(findJson)
        return self.fixTheData(cursor)

    # select single data point
    def selectTsharkProtocolDataById(self, dataId):
        collection = self.getTsharkProtocolCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return self.fixTheData(cursor)

    # add a fixedData record to this data point
    def insertFixedTsharkProtocolData(self, dataId, oldDataId, content, className, title, startDate):
        collection = self.getTsharkProtocolCollection()
        insertId = {"_id": ObjectId(dataId)}
        insertText = {"$set": {"id": oldDataId, "content": content , "className": className, "title": title, "start": startDate}}
        result = collection.update_one(insertId, insertText)
        return result.modified_count

    # update a previously 'fixed' record.
    def updateFixedTsharkProtocolData(self, dataId, oldDataId, content, className, title, startDate):
        collection = self.getTsharkProtocolCollection()
        updateId = {"_id" : ObjectId(dataId)}
        updateText = {"$set": {"id": oldDataId, "content": content , "className": className, "title": title, "start": startDate}}
        result = collection.update_one(updateId, updateText)
        return result.modified_count

    # delete the fixedData
    def deleteFixedTsharkProtocolData(self, dataId):
        collection = self.getTsharkProtocolCollection()
        deleteId = {"_id" : ObjectId(dataId)}
        deleteText = {"$unset": {"id": "", "content": "", "className": "", "title": "", "start": ""}}
        result = collection.update_one(deleteId, deleteText)
        return result.modified_count

    # add an annotation for the dataId
    def addAnnotationTsharkProtocol(self, dataId, annotationText):
        collection = self.getTsharkProtocolCollection()
        return Annotations().addAnnotation(collection, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationTsharkProtocol(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getTsharkProtocolCollection()
        return Annotations().editAnnotation(collection, dataId, oldAnnotationText, newAnnotationText)

    #delete an annotation for the dataId
    def deleteAnnotationTsharkProtocol(self, dataId, annotationText):
        collection = self.getTsharkProtocolCollection()
        return Annotations().deleteAnnotation(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForTsharkProtocol(self, dataId):
        collection = self.getTsharkProtocolCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToTsharkProtocolTimeline(self, startTime, annotationText):
        collection = self.getTsharkProtocolCollection()
        metadata = Common().createMetadataForTimelineAnnotations()

        tshark = {}
        tshark["className"] = ""
        tshark["content"] = ""
        tshark["type"] = ""
        tshark["title"] = ""
        tshark["start"] = datetime.strptime(startTime, Common().getDatetimeFormatString())
        tshark["metadata"] = metadata

        return Annotations().addAnnotationToTimeline(collection, tshark, annotationText)

    def fixTheData(self, cursor):
        objects = Common().formatOutput(cursor)
        for obj in objects:
            obj["id"] = obj["_id"]["$oid"]
            obj["start"] = Common().formatEpochDatetime(obj["start"]["$date"])
            obj["metadata"]["importDate"] = Common().formatEpochDatetime(obj["metadata"]["importDate"]["$date"])

        return objects
