from bson import ObjectId
from plugins.datasource.mongodb.annotations import Annotations
from plugins.datasource.mongodb.common import Common

class PyKeyPress:

    def getKeyPressCollection(self):
        return Common().getDatabase().keypressData

    def importKeypressData(self, json):
        collection = self.getKeyPressCollection()
        result = collection.insert_many(json)
        return len(result.inserted_ids)

    # select data by date range of the 'start' column
    def selectKeyPressData(self, startDate, endDate):
        collection = self.getKeyPressCollection()
        findJson = { "start": {"$gte" : startDate, "$lte": endDate}}
        cursor = collection.find(findJson)
        return self.fixTheDates(cursor)

    # select single data point
    def selectKeyPressDataById(self, dataId):
        collection = self.getKeyPressCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return self.fixTheDates(cursor)

    # add a fixedData record to this data point
    def insertFixedKeyPressData(self, dataId, keypress_id, content, className, start):
        collection = self.getKeyPressCollection()
        insertId = {"_id" : ObjectId(dataId)}
        push = { "$set": {"fixedData": {"keypress_id": keypress_id, "content": content, "className": className,"start": start}}}
        result = collection.update_one(insertId, push)
        return result.modified_count

    # update a previously 'fixed' record.
    def updateFixedKeyPressData(self, dataId, keypress_id, content, className, start):
        collection = self.getKeyPressCollection()
        updateId = {"_id" : ObjectId(dataId)}
        push = { "$set": {"fixedData": {"keypress_id": keypress_id, "content": content, "className": className,"start": start}}}
        result = collection.update_one(updateId, push)
        return result.modified_count

    # delete the fixedData
    def deleteFixedKeyPressData(self, dataId):
        collection = self.getKeyPressCollection()
        deleteId = {"_id" : ObjectId(dataId)}
        push = {"$unset": {"fixedData": ""}}
        result = collection.update_one(deleteId, push)
        return result.modified_count

    # add an annotation for the dataId
    def addAnnotationKeyPress(self, dataId, annotationText):
        collection = self.getKeyPressCollection()
        return Annotations().addAnnotation(collection, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationKeyPress(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getKeyPressCollection()
        return Annotations().editAnnotation(collection, dataId, oldAnnotationText, newAnnotationText)

    #delete an annotation for the dataId
    def deleteAnnotationKeyPress(self, dataId, annotationText):
        collection = self.getKeyPressCollection()
        return Annotations().deleteAnnotation(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForKeyPress(self, dataId):
        collection = self.getKeyPressCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToKeyPressTimeline(self, startTime, annotationText):
        collection = self.getKeyPressCollection()
        metadata = Common().createMetadataForTimelineAnnotations()

        keyPress = {}
        keyPress["className"] = ""
        keyPress["content"] = ""
        keyPress["start"] = startTime
        keyPress["metadata"] = metadata

        return Annotations().addAnnotationToTimeline(collection, keyPress, annotationText)

    def fixTheDates(self, cursor):
        objects = Common().formatOutput(cursor)
        for obj in objects:
            obj["id"] = obj["_id"]["$oid"]
            obj["start"] = Common().formatEpochDatetime(obj["start"]["$date"])
            obj["metadata"]["importDate"] = Common().formatEpochDatetime(obj["metadata"]["importDate"]["$date"])

        return objects
