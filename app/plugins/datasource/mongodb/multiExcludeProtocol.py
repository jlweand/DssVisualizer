from bson import ObjectId
from datetime import datetime
from plugins.datasource.mongodb.annotations import Annotations
from plugins.datasource.mongodb.common import Common
from pprint import pprint

class MultiExcludeProtocol:

    def getMultiExcludeProtocolCollection(self):
        return Common().getDatabase().multiExcludeProtocol

    def importMultiExcludeProtocolData(self, json):
        collection = self.getMultiExcludeProtocolCollection()
        result = collection.insert_many(json)
        return len(result.inserted_ids)

    # select data by date range of the 'start' column
    def selectMultiExcludeProtocolData(self, startDate, endDate):
        collection = self.getMultiExcludeProtocolCollection()
        #findJson = {"start": {"$gte": datetime.strptime(startDate, Common().getDatetimeFormatString()), "$lt": datetime.strptime(endDate, Common().getDatetimeFormatString())}}
        findJson = { "start": {"$gte" : startDate, "$lte": endDate}}
        cursor = collection.find(findJson)
        return self.fixTheData(cursor)

    # select single data point
    def selectMultiExcludeProtocolDataById(self, dataId):
        collection = self.getMultiExcludeProtocolCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return self.fixTheData(cursor)

    # add a fixedData record to this data point
    def insertFixedMultiExcludeProtocolData(self, dataId, oldDataId, content, className, title, startDate):
        collection = self.getMultiExcludeProtocolCollection()
        insertId = {"_id": ObjectId(dataId)}
        insertText = {"$set": {"id": oldDataId, "content": content , "className": className, "title": title, "start": startDate}}
        result = collection.update_one(insertId, insertText)
        return result.modified_count

    # update a previously 'fixed' record.
    def updateFixedMultiExcludeProtocolData(self, dataId, oldDataId, content, className, title, startDate):
        collection = self.getMultiExcludeProtocolCollection()
        updateId = {"_id" : ObjectId(dataId)}
        updateText = {"$set": {"id": oldDataId, "content": content , "className": className, "title": title, "start": startDate}}
        result = collection.update_one(updateId, updateText)
        return result.modified_count

    # delete the fixedData
    def deleteFixedMultiExcludeProtocolData(self, dataId):
        collection = self.getMultiExcludeProtocolCollection()
        deleteId = {"_id" : ObjectId(dataId)}
        deleteText = {"$unset": {"id": "", "content": "", "className": "", "title": "", "start": ""}}
        result = collection.update_one(deleteId, deleteText)
        return result.modified_count

    # add an annotation for the dataId
    def addAnnotationMultiExcludeProtocol(self, dataId, annotationText):
        collection = self.getMultiExcludeProtocolCollection()
        return Annotations().addAnnotation(collection, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationMultiExcludeProtocol(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getMultiExcludeProtocolCollection()
        return Annotations().editAnnotation(collection, dataId, oldAnnotationText, newAnnotationText)

    #delete an annotation for the dataId
    def deleteAnnotationMultiExcludeProtocol(self, dataId, annotationText):
        collection = self.getMultiExcludeProtocolCollection()
        return Annotations().deleteAnnotation(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForMultiExcludeProtocol(self, dataId):
        collection = self.getMultiExcludeProtocolCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToMultiExcludeProtocolTimeline(self, startTime, annotationText):
        collection = self.getMultiExcludeProtocolCollection()
        metadata = Common().createMetadataForTimelineAnnotations()

        multiExclude = {}
        multiExclude["className"] = ""
        multiExclude["content"] = ""
        multiExclude["type"] = ""
        multiExclude["title"] = ""
        multiExclude["start"] = datetime.strptime(startTime, Common().getDatetimeFormatString())
        multiExclude["metadata"] = metadata

        return Annotations().addAnnotationToTimeline(collection, multiExclude, annotationText)

    def fixTheData(self, cursor):
        objects = Common().formatOutput(cursor)
        for obj in objects:
            obj["id"] = obj["_id"]["$oid"]
            obj["start"] = Common().formatEpochDatetime(obj["start"]["$date"])
            obj["metadata"]["importDate"] = Common().formatEpochDatetime(obj["metadata"]["importDate"]["$date"])

        return objects

