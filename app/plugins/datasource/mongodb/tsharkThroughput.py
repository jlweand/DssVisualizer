from bson import ObjectId
from plugins.datasource.mongodb.annotations import Annotations
from plugins.datasource.mongodb.common import Common

class TsharkThroughput:

    def getTsharkThroughputCollection(self):
        return Common().getDatabase().tsharkThroughput

    def importTsharkThroughputData(self, json):
        collection = self.getTsharkThroughputCollection()
        result = collection.insert_many(json)
        return len(result.inserted_ids)

    # select data by date range of the 'start' column
    def selectTsharkThroughputData(self, startDate, endDate, techName, eventName):
        collection = self.getTsharkThroughputCollection()
        findJson = Common().updateTechAndEventNames(startDate, endDate, techName, eventName, False, True)
        cursor = collection.find(findJson)
        return self.fixTheData(cursor)

    # select single data point
    def selectTsharkThroughputDataById(self, dataId):
        collection = self.getTsharkThroughputCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return self.fixTheData(cursor)

    # add a fixedData record to this data point
    def insertFixedTsharkThroughputData(self, dataId, x, y):
        collection = self.getTsharkThroughputCollection()
        updateId = {"_id": ObjectId(dataId)}
        fixedData = {"$set": {"fixedData": {"x": x, "y": y}}}
        result = collection.update_one(updateId, fixedData)
        return result.modified_count

    # update a previously 'fixed' record.
    def updateFixedTsharkThroughputData(self, dataId, x, y):
        collection = self.getTsharkThroughputCollection()
        updateId = {"_id" : ObjectId(dataId)}
        fixedData = {"$set": {"fixedData": {"x": x, "y": y}}}

        result = collection.update_one(updateId, fixedData)
        return result.modified_count

    # delete the fixedData
    def deleteFixedTsharkThroughputData(self, dataId):
        collection = self.getTsharkThroughputCollection()
        updateId = {"_id" : ObjectId(dataId)}
        fixedData = {"$unset": {"fixedData": "" }}
        result = collection.update_one(updateId, fixedData)
        return result.modified_count

    # add an annotation for the dataId
    def addAnnotationTsharkThroughput(self, dataId, annotationText):
        collection = self.getTsharkThroughputCollection()
        return Annotations().addAnnotation(collection, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationTsharkThroughput(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getTsharkThroughputCollection()
        return Annotations().editAnnotation(collection, dataId, oldAnnotationText, newAnnotationText)

    #delete an annotation for the dataId
    def deleteAnnotationTsharkThroughput(self, dataId, annotationText):
        collection = self.getTsharkThroughputCollection()
        return Annotations().deleteAnnotation(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForTsharkThroughput(self, dataId):
        collection = self.getTsharkThroughputCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToTsharkThroughputTimeline(self, startTime, annotationText):
        collection = self.getTsharkThroughputCollection()
        metadata = Common().createMetadataForTimelineAnnotations()

        tshark = {}
        tshark["x"] = startTime
        tshark["y"] = ""
        tshark["metadata"] = metadata

        return Annotations().addAnnotationToTimeline(collection, tshark, annotationText)

    def fixTheData(self, cursor):
        objects = Common().formatOutput(cursor)
        for obj in objects:
            obj["id"] = obj["_id"]["$oid"]
            obj["metadata"]["importDate"] = Common().formatEpochDatetime(obj["metadata"]["importDate"]["$date"])

            if obj["x"] != "":
                obj["x"] = Common().formatEpochDatetime(obj["x"]["$date"])

        return objects
