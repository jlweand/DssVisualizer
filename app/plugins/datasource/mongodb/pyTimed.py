from bson import ObjectId
from plugins.datasource.mongodb.annotations import Annotations
from plugins.datasource.mongodb.common import Common

class PyTimed:

    def getTimedCollection(self):
        return Common().getDatabase().timed

    def importTimed(self, json):
        collection = self.getTimedCollection()
        result = collection.insert_many(json)
        return len(result.inserted_ids)

    # select data by date range of the 'start' column
    def selectTimedData(self, startDate, endDate):
        collection = self.getTimedCollection()
        findJson = { "start": {"$gte" : startDate, "$lte": endDate}}
        cursor = collection.find(findJson)
        return self.fixTheDates(cursor)

    # select single data point
    def selectTimedDataById(self, dataId):
        collection = self.getTimedCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return self.fixTheDates(cursor)

    # add a fixedData record to this data point
    def insertFixedTimedData(self, dataId, timed_id, content, className, start, title, typeTimed):
        collection = self.getTimedCollection()
        insertId = {"_id" : ObjectId(dataId)}
        push = { "$set": {"fixedData": {"timed_id": timed_id, "content": content, "className": className,"start": start, "title": title, "type": typeTimed}}}
        result = collection.update_one(insertId, push)
        return result.modified_count

    # update a previously 'fixed' record.
    def updateFixedTimedData(self, dataId, timed_id, content, className, start, title, typeTimed):
        collection = self.getTimedCollection()
        updateId = {"_id" : ObjectId(dataId)}
        push = { "$set": {"fixedData": {"timed_id": timed_id, "content": content, "className": className,"start": start, "title": title, "type": typeTimed}}}
        result = collection.update_one(updateId, push)
        return result.modified_count

    # delete the fixedData
    def deleteFixedTimedData(self, dataId):
        collection = self.getTimedCollection()
        deleteId = {"_id" : ObjectId(dataId)}
        push = {"$unset": {"fixedData": ""}}
        result = collection.update_one(deleteId, push)
        return result.modified_count

    # add an annotation for the dataId
    def addAnnotationTimed(self, dataId, annotationText):
        collection = self.getTimedCollection()
        return Annotations().addAnnotation(collection, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationTimed(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getTimedCollection()
        return Annotations().editAnnotation(collection, dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation for the dataId
    def deleteAnnotationTimed(self, dataId, annotationText):
        collection = self.getTimedCollection()
        return Annotations().deleteAnnotation(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForTimed(self, dataId):
        collection = self.getTimedCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToTimedTimeline(self, startTime, annotationText):
        collection = self.getTimedCollection()
        metadata = Common().createMetadataForTimelineAnnotations()

        timed = {}
        timed["className"] = ""
        timed["content"] = ""
        timed["type"] = ""
        timed["title"] = ""
        timed["start"] = startTime
        timed["metadata"] = metadata

        return Annotations().addAnnotationToTimeline(collection, timed, annotationText)

    def fixTheDates(self, cursor):
        objects = Common().formatOutput(cursor)
        for obj in objects:
            obj["id"] = obj["_id"]["$oid"]
            obj["start"] = Common().formatEpochDatetime(obj["start"]["$date"])
            obj["metadata"]["importDate"] = Common().formatEpochDatetime(obj["metadata"]["importDate"]["$date"])

        return objects