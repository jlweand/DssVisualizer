from bson import ObjectId
from datetime import datetime
from plugins.datasource.mongodb.annotations import Annotations
from plugins.datasource.mongodb.common import Common
from pprint import pprint

class PyKeyLogger:

    def getKeyPressCollection(self):
        return Common().getDatabase().keypressData

    def getClickCollection(self):
        return Common().getDatabase().click

    def getTimedCollection(self):
        return Common().getDatabase().timed

    def importKeypressData(self, json):
        collection = self.getKeyPressCollection()
        result = collection.insert_many(json)
        return len(result.inserted_ids)

    def importClick(self, json):
        collection = self.getClickCollection()
        result = collection.insert_many(json)
        return len(result.inserted_ids)

    def importTimed(self, json):
        collection = self.getTimedCollection()
        result = collection.insert_many(json)
        return len(result.inserted_ids)

# Keypress #
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

    # insert a new record.  This record must be tied to the original record.
    # the oldDataId will be a new 'column' called sourceId. it is of type ObjectId
    def insertFixedKeyPressData(self, dataId, keypress_id, content, className, start):
        collection = self.getKeyPressCollection()
        insertId = {"_id" : ObjectId(dataId)}
        push = { "$set": {"fixedData": {"keypress_id": keypress_id, "content": content, "className": className,"start": start}}}
        result = collection.update_one(insertId, push)
        return result.modified_count

    # update a previously 'fixed' record. Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def updateFixedKeyPressData(self, dataId, keypress_id, content, className, start):
        collection = self.getKeyPressCollection()
        updateId = {"_id" : ObjectId(dataId)}
        push = { "$set": {"fixedData": {"keypress_id": keypress_id, "content": content, "className": className,"start": start}}}
        result = collection.update_one(updateId, push)
        return result.modified_count

    # delete a record.  Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
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

# Click #
    # select data by date range of the 'start' column
    def selectClickData(self, startDate, endDate):
        collection = self.getClickCollection()
        findJson = { "start": {"$gte" : startDate, "$lte": endDate}}
        cursor = collection.find(findJson)
        return self.fixTheDates(cursor)

    # select single data point
    def selectClickDataById(self, dataId):
        collection = self.getClickCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return self.fixTheDates(cursor)

    # insert a new record.  This record must be tied to the original record.
    # the oldDataId will be a new 'column' called sourceId. it is of type ObjectId
    def insertFixedClickData(self, dataId, clicks_id, content, className, start, title, typeClick):
        collection = self.getClickCollection()
        insertId = {"_id" : ObjectId(dataId)}
        push = { "$set": {"fixedData": {"clicks_id": clicks_id, "content": content, "className": className,"start": start, "title": title, "type": typeClick}}}
        result = collection.update_one(insertId, push)
        return result.modified_count

    # update a previously 'fixed' record. Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def updateFixedClickData(self, dataId, clicks_id, content, className, start, title, typeClick):
        collection = self.getClickCollection()
        updateId = {"_id" : ObjectId(dataId)}
        push = { "$set": {"fixedData": {"clicks_id": clicks_id, "content": content, "className": className,"start": start, "title": title, "type": typeClick}}}
        result = collection.update_one(updateId, push)
        return result.modified_count

    # delete a record.  Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
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
        # click["start"] = datetime.strptime(startTime, Common().getDatetimeFormatString())
        click["start"] = startTime
        click["metadata"] = metadata

        return Annotations().addAnnotationToTimeline(collection, click, annotationText)

# Timed #
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

    # insert a new record.  This record must be tied to the original record.
    # the oldDataId will be a new 'column' called sourceId. it is of type ObjectId
    def insertFixedTimedData(self, dataId, timed_id, content, className, start, title, typeTimed):
        collection = self.getTimedCollection()
        insertId = {"_id" : ObjectId(dataId)}
        push = { "$set": {"fixedData": {"timed_id": timed_id, "content": content, "className": className,"start": start, "title": title, "type": typeTimed}}}
        result = collection.update_one(insertId, push)
        return result.modified_count

    # update a previously 'fixed' record. Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def updateFixedTimedData(self, dataId, timed_id, content, className, start, title, typeTimed):
        collection = self.getTimedCollection()
        updateId = {"_id" : ObjectId(dataId)}
        push = { "$set": {"fixedData": {"timed_id": timed_id, "content": content, "className": className,"start": start, "title": title, "type": typeTimed}}}
        result = collection.update_one(updateId, push)
        return result.modified_count

    # delete a record.  Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
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
        # timed["start"] = datetime.strptime(startTime, Common().getDatetimeFormatString())
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
