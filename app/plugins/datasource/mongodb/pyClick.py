from bson import ObjectId
from plugins.datasource.mongodb.annotations import Annotations
from plugins.datasource.mongodb.common import Common

class PyClick:

    def getClickCollection(self):
        return Common().getDatabase().click

    def importClick(self, json):
        collection = self.getClickCollection()
        result = collection.insert_many(json)
        return len(result.inserted_ids)

    # select data by date range of the 'start' column
    def selectClickData(self, startDate, endDate, techName, eventName):
        collection = self.getClickCollection()
        findJson = Common().updateTechAndEventNames(startDate, endDate, techName, eventName, True, False)
        cursor = collection.find(findJson)
        return self.fixTheDates(cursor)

    # select single data point
    def selectClickDataById(self, dataId):
        collection = self.getClickCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return self.fixTheDates(cursor)

    # add a fixedData record to this data point
    def insertFixedClickData(self, dataId, clicks_id, content, className, start, title, typeClick):
        collection = self.getClickCollection()
        insertId = {"_id" : ObjectId(dataId)}
        push = { "$set": {"fixedData": {"clicks_id": clicks_id, "content": content, "className": className,"start": start, "title": title, "type": typeClick}}}
        result = collection.update_one(insertId, push)
        return result.modified_count

    # update a previously 'fixed' record.
    def updateFixedClickData(self, dataId, clicks_id, content, className, start, title, typeClick):
        collection = self.getClickCollection()
        updateId = {"_id" : ObjectId(dataId)}
        push = { "$set": {"fixedData": {"clicks_id": clicks_id, "content": content, "className": className,"start": start, "title": title, "type": typeClick}}}
        result = collection.update_one(updateId, push)
        return result.modified_count

    # delete the fixedData
    def deleteFixedClickData(self, dataId):
        collection = self.getClickCollection()
        deleteId = {"_id" : ObjectId(dataId)}
        push = {"$unset": {"fixedData": ""}}
        result = collection.update_one(deleteId, push)
        return result.modified_count

    # add an annotation for the dataId
    def addAnnotationClick(self, dataId, annotationText):
        collection = self.getClickCollection()
        return Annotations().addAnnotation(collection, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationClick(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getClickCollection()
        return Annotations().editAnnotation(collection, dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation for the dataId
    def deleteAnnotationClick(self, dataId, annotationText):
        collection = self.getClickCollection()
        return Annotations().deleteAnnotation(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForClick(self, dataId):
        collection = self.getClickCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToClickTimeline(self, startTime, annotationText):
        collection = self.getClickCollection()
        metadata = Common().createMetadataForTimelineAnnotations()

        click = {}
        click["className"] = ""
        click["content"] = ""
        click["type"] = ""
        click["title"] = ""
        click["start"] = startTime
        click["metadata"] = metadata

        return Annotations().addAnnotationToTimeline(collection, click, annotationText)

    def fixTheDates(self, cursor):
        objects = Common().formatOutput(cursor)
        for obj in objects:
            obj["id"] = obj["_id"]["$oid"]
            obj["start"] = Common().formatEpochDatetime(obj["start"]["$date"])
            obj["metadata"]["importDate"] = Common().formatEpochDatetime(obj["metadata"]["importDate"]["$date"])

        return objects
