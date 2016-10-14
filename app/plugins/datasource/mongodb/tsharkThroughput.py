from bson import ObjectId
from datetime import datetime
from plugins.datasource.mongodb.annotations import Annotations
from plugins.datasource.mongodb.common import Common
from pprint import pprint

class TsharkThroughput:

    def getTsharkCollection(self):
        return Common().getDatabase().tsharkThroughput

    def importTsharkData(self, json):
        collection = self.getTsharkCollection()
        result = collection.insert_many(json)
        return len(result.inserted_ids)

# Tshark #
    # select data by date range of the 'start' column
    def selectTsharkData(self, startDate, endDate):
        collection = self.getTsharkCollection()
        findJson = { "x": {"$gte" : datetime.strptime(startDate, Common().getDatetimeFormatString()), "$lt": datetime.strptime(endDate, Common().getDatetimeFormatString())}}
        cursor = collection.find(findJson)
        return self.fixTheData(cursor)

    # select single data point
    def selectTsharkDataById(self, dataId):
        collection = self.getTsharkCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return self.fixTheData(cursor)

    # add a fixedData record to this data point
    def insertFixedTsharkData(self, dataId, x, y):
        collection = self.getTsharkCollection()
        updateId = {"_id": ObjectId(dataId)}
        fixedData = {"$set": {"fixedData": {"x": x, "y": y}}}
        result = collection.update_one(updateId, fixedData)
        return result.modified_count

    # update a previously 'fixed' record.
    def updateFixedTsharkData(self, dataId, x, y):
        collection = self.getTsharkCollection()
        updateId = {"_id" : ObjectId(dataId)}
        fixedData = {"$set": {"fixedData": {"x": x, "y": y}}}

        result = collection.update_one(updateId, fixedData)
        return result.modified_count;

    # delete the fixedData
    def deleteFixedTsharkData(self, dataId):
        collection = self.getTsharkCollection()
        updateId = {"_id" : ObjectId(dataId)}
        fixedData = {"$unset": {"fixedData": "" }}
        result = collection.update_one(updateId, fixedData)
        return result.modified_count

    # add an annotation for the dataId
    def addAnnotationTshark(self, dataId, annotationText):
        collection = self.getTsharkCollection()
        return Annotations().addAnnotation(collection, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationTshark(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getTsharkCollection()
        return Annotations().editAnnotation(collection, dataId, oldAnnotationText, newAnnotationText)

    #delete an annotation for the dataId
    def deleteAnnotationTshark(self, dataId, annotationText):
        collection = self.getTsharkCollection()
        return Annotations().deleteAnnotation(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForTshark(self, dataId):
        collection = self.getTsharkCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToTsharkTimeline(self, startTime, annotationText):
        collection = self.getTsharkCollection()
        metadata = Common().createMetadataForTimelineAnnotations()

        tshark = {}
        tshark["x"] = ""
        tshark["y"] = ""
        tshark["metadata"] = metadata

        return Annotations().addAnnotationToTimeline(collection, tshark, annotationText)

    def fixTheData(self, cursor):
        objects = Common().formatOutput(cursor)
        for obj in objects:
            obj["_id"] = obj["_id"]["$oid"]
            obj["metadata"]["importDate"] = Common().formatEpochDatetime(obj["metadata"]["importDate"]["$date"])

            if obj["x"] != "":
                obj["x"] = Common().formatEpochDatetime(obj["x"]["$date"])

        return objects
