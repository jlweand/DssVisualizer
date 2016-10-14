from bson import ObjectId
from datetime import datetime
from plugins.datasource.mongodb.annotations import Annotations
from plugins.datasource.mongodb.common import Common
from pprint import pprint

class MultiExcludeThroughput:

    def getMultiExcludeThroughputCollection(self):
        return Common().getDatabase().multiExcludeThroughput

    def importMultiExcludeThroughputData(self, json):
        collection = self.getMultiExcludeThroughputCollection()
        result = collection.insert_many(json)
        return len(result.inserted_ids)

    # select data by date range of the 'start' column
    def selectMultiExcludeThroughputData(self, startDate, endDate):
        collection = self.getMultiExcludeThroughputCollection()
        findJson = { "x": {"$gte" : datetime.strptime(startDate, Common().getDatetimeFormatString()), "$lt": datetime.strptime(endDate, Common().getDatetimeFormatString())}}
        cursor = collection.find(findJson)
        return self.fixTheData(cursor)

    # select single data point
    def selectMultiExcludeThroughputDataById(self, dataId):
        collection = self.getMultiExcludeThroughputCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return self.fixTheData(cursor)

    # add a fixedData record to this data point
    def insertFixedMultiExcludeThroughputData(self, dataId, x, y):
        collection = self.getMultiExcludeThroughputCollection()
        updateId = {"_id": ObjectId(dataId)}
        fixedData = {"$set": {"fixedData": {"x": x, "y": y}}}
        result = collection.update_one(updateId, fixedData)
        return result.modified_count

    # update a previously 'fixed' record.
    def updateFixedMultiExcludeThroughputData(self, dataId, x, y):
        collection = self.getMultiExcludeThroughputCollection()
        updateId = {"_id" : ObjectId(dataId)}
        fixedData = {"$set": {"fixedData": {"x": x, "y": y}}}

        result = collection.update_one(updateId, fixedData)
        return result.modified_count;

    # delete the fixedData
    def deleteFixedMultiExcludeThroughputData(self, dataId):
        collection = self.getMultiExcludeThroughputCollection()
        updateId = {"_id" : ObjectId(dataId)}
        fixedData = {"$unset": {"fixedData": "" }}
        result = collection.update_one(updateId, fixedData)
        return result.modified_count

    # add an annotation for the dataId
    def addAnnotationMultiExcludeThroughput(self, dataId, annotationText):
        collection = self.getMultiExcludeThroughputCollection()
        return Annotations().addAnnotation(collection, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationMultiExcludeThroughput(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getMultiExcludeThroughputCollection()
        return Annotations().editAnnotation(collection, dataId, oldAnnotationText, newAnnotationText)

    #delete an annotation for the dataId
    def deleteAnnotationMultiExcludeThroughput(self, dataId, annotationText):
        collection = self.getMultiExcludeThroughputCollection()
        return Annotations().deleteAnnotation(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForMultiExcludeThroughput(self, dataId):
        collection = self.getMultiExcludeThroughputCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToMultiExcludeThroughputTimeline(self, startTime, annotationText):
        collection = self.getMultiExcludeThroughputCollection()
        metadata = Common().createMetadataForTimelineAnnotations()

        multiExclude = {}
        multiExclude["x"] = ""
        multiExclude["y"] = ""
        multiExclude["metadata"] = metadata

        return Annotations().addAnnotationToTimeline(collection, multiExclude, annotationText)

    def fixTheData(self, cursor):
        objects = Common().formatOutput(cursor)
        for obj in objects:
            obj["_id"] = obj["_id"]["$oid"]
            obj["metadata"]["importDate"] = Common().formatEpochDatetime(obj["metadata"]["importDate"]["$date"])

            if obj["x"] != "":
                obj["x"] = Common().formatEpochDatetime(obj["x"]["$date"])

        return objects
