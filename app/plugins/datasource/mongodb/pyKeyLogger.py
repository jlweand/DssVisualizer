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
        return 0

    # update a previously 'fixed' record. Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def updateFixedKeyPressData(self, dataId, content, className, start):
        return 0

    # delete a record.  Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def deleteFixedKeyPressData(self, dataId):
        return 0

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
    def insertFixedClickData(self, oldDataId, content, _type, classname, title, start, end):
        return 0

    # update a previously 'fixed' record. Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def updateFixedClickData(self, dataId, content, _type, classname, title, start, end):
        return 0

    # delete a record.  Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def deleteFixedClickData(self, dataId):
        return 0

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
    def insertFixedTimedData(self, oldDataId, content, _type, classname, title, start, end):
        return 0

    # update a previously 'fixed' record. Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def updateFixedTimedData(self, dataId, content, _type, classname, title, start, end):
        return 0

    # delete a record.  Make sure that this record has a value in the sourceId.
    # ORIGINAL DATA SHOULD NEVER BE UPDATED OR DELETED.
    def deleteFixedTimedData(self, dataId):
        return 0

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
