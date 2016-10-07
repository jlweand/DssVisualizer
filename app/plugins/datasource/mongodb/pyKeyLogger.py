from bson import ObjectId
from datetime import datetime
from plugins.datasource.mongodb.annotations import Annotations
from plugins.datasource.mongodb.common import Common

class PyKeyLogger:

    def getKeyPressCollection(self):
        return Common().getDatabase().keypressData

    def getClickCollection(self):
        return Common().getDatabase().click

    def getTimedCollection(self):
        return Common().getDatabase().timed

    def importKeypressData(self, json):
        collection = self.getKeyPressCollection()
        collection.delete_many({})
        result = collection.insert_many(json)
        return len(result.inserted_ids)

    def importClick(self, json):
        collection = self.getClickCollection()
        collection.delete_many({})
        result = collection.insert_many(json)
        return len(result.inserted_ids)

    def importTimed(self, json):
        collection = self.getTimedCollection()
        collection.delete_many({})
        result = collection.insert_many(json)
        return len(result.inserted_ids)

# Keypress #
    # select data by date range of the 'start' column
    def selectKeyPressData(self, startDate, endDate):
        collection = self.getKeyPressCollection()
        findJson = { "start": {"$gte" : datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S'), "$lt": datetime.strptime(endDate, '%Y-%m-%d %H:%M:%S')}}
        cursor = collection.find(findJson)
        return self.fixTheDates(cursor, False)

    # select single data point
    def selectKeyPressDataById(self, dataId):
        collection = self.getKeyPressCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return self.fixTheDates(cursor, False)

    # insert a new record.  This record must be tied to the original record.
    # the oldDataId will be a new 'column' called sourceId. it is of type ObjectId
    def insertFixedKeyPressData(self, oldDataId, content, className, start):
        collection = self.getDatabase().keypressData
        insertJson = {"oldDataId": oldDataId, "content": content, "className": className,"start": start}
        result = collection.insert_one(insertJson)
        return result.inserted_id

    # update a previously 'fixed' record. Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def updateFixedKeyPressData(self, dataId, oldDataId, content, start):
        collection = self.getDatabase().keypressData
        updateId = {"$and":[{ "_id" : ObjectId(dataId)}, { "oldDataId" : oldDataId}]}
        updateText = {"$set": {"content": content ,"start": start}}
        result = collection.update_one(updateId, updateText)
        return result.modified_count

    # delete a record.  Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def deleteFixedKeyPressData(self, dataId, oldDataId):
        collection = self.getDatabase().keypressData
        deleteJson = {"$and":[{ "_id" : ObjectId(dataId)}, { "oldDataId" : oldDataId}]}
        result = collection.delete_one(deleteJson)
        return result.deleted_count

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

# Click #
    # select data by date range of the 'start' column
    def selectClickData(self, startDate, endDate):
        collection = self.getClickCollection()
        findJson = { "start": {"$gte" : datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S'), "$lt": datetime.strptime(endDate, '%Y-%m-%d %H:%M:%S')}}
        cursor = collection.find(findJson)
        return self.fixTheDates(cursor, True)

    # select single data point
    def selectClickDataById(self, dataId):
        collection = self.getClickCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return self.fixTheDates(cursor, False)

    # insert a new record.  This record must be tied to the original record.
    # the oldDataId will be a new 'column' called sourceId. it is of type ObjectId
    def insertFixedClickData(self, oldDataId, content, className, start, end, title, typeClick):
        collection = self.getDatabase().click
        insertJson = {"oldDataId": oldDataId, "content": content, "className": className,"start": start, "end": end, "title": title, "type": typeClick}
        result = collection.insert_one(insertJson)
        return result.inserted_id

    # update a previously 'fixed' record. Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def updateFixedClickData(self, dataId, oldDataId, content, start, end, title, typeClick):
        collection = self.getDatabase().click
        updateId = {"$and":[{ "_id" : ObjectId(dataId)}, { "oldDataId" : oldDataId}]}
        updateText = {"$set": {"content": content ,"start": start, "end": end, "title": title, "type": typeClick}}
        result = collection.update_one(updateId, updateText)
        return result.modified_count

    # delete a record.  Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def deleteFixedClickData(self, dataId, oldDataId):
        collection = self.getDatabase().click
        deleteJson = {"$and":[{ "_id" : ObjectId(dataId)}, { "oldDataId" : oldDataId}]}
        result = collection.delete_one(deleteJson)
        return result.deleted_count

    # add an annotation for the dataId
    def addAnnotationClick(self, dataId, annotationText):
        collection = self.getClickCollection()
        return Annotations().addAnnotation(collection, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationClick(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getClickCollection()
        return Annotations().editAnnotation(collection, dataId, oldAnnotationText, newAnnotationText)

    #delete an annotation for the dataId
    def deleteAnnotationClick(self, dataId, annotationText):
        collection = self.getClickCollection()
        return Annotations().deleteAnnotation(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForClick(self, dataId):
        collection = self.getClickCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

# Timed #
    # select data by date range of the 'start' column
    def selectTimedData(self, startDate, endDate):
        collection = self.getTimedCollection()
        findJson = { "start": {"$gte" : datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S'), "$lt": datetime.strptime(endDate, '%Y-%m-%d %H:%M:%S')}}
        cursor = collection.find(findJson)
        return self.fixTheDates(cursor, True)

    # select single data point
    def selectTimedDataById(self, dataId):
        collection = self.getTimedCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return self.fixTheDates(cursor, False)

    # insert a new record.  This record must be tied to the original record.
    # the oldDataId will be a new 'column' called sourceId. it is of type ObjectId
    def insertFixedTimedData(self, oldDataId, content, className, start, end, title, typeTimed):
        collection = self.getDatabase().timed
        insertJson = {"oldDataId": oldDataId, "content": content, "className": className,"start": start, "end": end, "title": title, "type": typeTimed}
        result = collection.insert_one(insertJson)
        return result.inserted_id

    # update a previously 'fixed' record. Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def updateFixedTimedData(self, dataId, oldDataId, content, start, end, title, typeTimed):
        collection = self.getDatabase().timed
        updateId = {"$and":[{ "_id" : ObjectId(dataId)}, { "oldDataId" : oldDataId}]}
        updateText = {"$set": {"content": content ,"start": start, "end": end, "title": title, "type": typeTimed}}
        result = collection.update_one(updateId, updateText)
        return result.modified_count

    # delete a record.  Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def deleteFixedTimedData(self, dataId, oldDataId):
        collection = self.getDatabase().timed
        deleteJson = {"$and":[{ "_id" : ObjectId(dataId)}, { "oldDataId" : oldDataId}]}
        result = collection.delete_one(deleteJson)
        return result.deleted_count

    # add an annotation for the dataId
    def addAnnotationTimed(self, dataId, annotationText):
        collection = self.getTimedCollection()
        return Annotations().addAnnotation(collection, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationTimed(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getTimedCollection()
        return Annotations().editAnnotation(collection, dataId, oldAnnotationText, newAnnotationText)

    #delete an annotation for the dataId
    def deleteAnnotationTimed(self, dataId, annotationText):
        collection = self.getTimedCollection()
        return Annotations().deleteAnnotation(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForTimed(self, dataId):
        collection = self.getTimedCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)


    def fixTheDates(self, cursor, hasEndDate):
        objects = Common().formatOutput(cursor)
        for obj in objects:
            obj["start"] = Common().formatDatetime(obj["start"]["$date"])
            obj["metadata"]["importDate"] = Common().formatDatetime(obj["metadata"]["importDate"]["$date"])

            if(hasEndDate):
                obj["end"] = Common().formatDatetime(obj["end"]["$date"])

        return objects