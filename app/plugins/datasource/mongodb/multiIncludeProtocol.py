from bson import ObjectId
from datetime import datetime
from plugins.datasource.mongodb.annotations import Annotations
from plugins.datasource.mongodb.common import Common
from pprint import pprint

class MultiIncludeProtocol:

    def getMultiIncludeProtocolCollection(self):
        return Common().getDatabase().multiIncludeProtocol

    def importMultiIncludeProtocolData(self, json):
        collection = self.getMultiIncludeProtocolCollection()
        result = collection.insert_many(json)
        return len(result.inserted_ids)

    # select data by date range of the 'start' column
    def selectMultiIncludeProtocolData(self, startDate, endDate):
        collection = self.getMultiIncludeProtocolCollection()
        #findJson = {"start": {"$gte": datetime.strptime(startDate, Common().getDatetimeFormatString()), "$lt": datetime.strptime(endDate, Common().getDatetimeFormatString())}}
        findJson = { "start": {"$gte" : startDate, "$lte": endDate}}
        cursor = collection.find(findJson)
        return self.fixTheData(cursor)

    # select single data point
    def selectMultiIncludeProtocolDataById(self, dataId):
        collection = self.getMultiIncludeProtocolCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return self.fixTheData(cursor)

    # add a fixedData record to this data point
    def insertFixedMultiIncludeProtocolData(self, dataId, oldDataId, content, className, title, startDate):
        collection = self.getMultiIncludeProtocolCollection()
        insertId = {"_id": ObjectId(dataId)}
        insertText = {"$set": {"id": oldDataId, "content": content , "className": className, "title": title, "start": startDate}}
        result = collection.update_one(insertId, insertText)
        return result.modified_count

    # update a previously 'fixed' record.
    def updateFixedMultiIncludeProtocolData(self, dataId, oldDataId, content, className, title, startDate):
        collection = self.getMultiIncludeProtocolCollection()
        updateId = {"_id" : ObjectId(dataId)}
        updateText = {"$set": {"id": oldDataId, "content": content , "className": className, "title": title, "start": startDate}}
        result = collection.update_one(updateId, updateText)
        return result.modified_count

    # delete the fixedData
    def deleteFixedMultiIncludeProtocolData(self, dataId):
        collection = self.getMultiIncludeProtocolCollection()
        deleteId = {"_id" : ObjectId(dataId)}
        deleteText = {"$unset": {"id": "", "content": "", "className": "", "title": "", "start": ""}}
        result = collection.update_one(deleteId, deleteText)
        return result.modified_count

    # add an annotation for the dataId
    def addAnnotationMultiIncludeProtocol(self, dataId, annotationText):
        collection = self.getMultiIncludeProtocolCollection()
        return Annotations().addAnnotation(collection, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationMultiIncludeProtocol(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getMultiIncludeProtocolCollection()
        return Annotations().editAnnotation(collection, dataId, oldAnnotationText, newAnnotationText)

    #delete an annotation for the dataId
    def deleteAnnotationMultiIncludeProtocol(self, dataId, annotationText):
        collection = self.getMultiIncludeProtocolCollection()
        return Annotations().deleteAnnotation(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForMultiIncludeProtocol(self, dataId):
        collection = self.getMultiIncludeProtocolCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToMultiIncludeProtocolTimeline(self, startTime, annotationText):
        collection = self.getMultiIncludeProtocolCollection()
        metadata = Common().createMetadataForTimelineAnnotations()

        multiInclude = {}
        multiInclude["className"] = ""
        multiInclude["content"] = ""
        multiInclude["type"] = ""
        multiInclude["title"] = ""
        multiInclude["start"] = datetime.strptime(startTime, Common().getDatetimeFormatString())
        multiInclude["metadata"] = metadata

        return Annotations().addAnnotationToTimeline(collection, multiInclude, annotationText)

    def fixTheData(self, cursor):
        objects = Common().formatOutput(cursor)
        for obj in objects:
            obj["id"] = obj["_id"]["$oid"]
            obj["start"] = Common().formatEpochDatetime(obj["start"]["$date"])
            obj["metadata"]["importDate"] = Common().formatEpochDatetime(obj["metadata"]["importDate"]["$date"])

        return objects
