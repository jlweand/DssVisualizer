from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
from datetime import datetime

class Annotations:

    def getCollection(self):
        client = MongoClient()
        db = client.dssvisualizer
        return db.annotations

    # get all annotations for the dataObjectId
    def getAnnotations(self, dataId):
        #connect2DB
        collection = self.getCollection()
        findJson = {"dataObjectId": dataId}

        #SQL Equivalent: Select * from t_annotations where dataObjectId = dataObjectId
        annotations = collection.find(findJson)
        
        # dump it into a JSON string from a MongoDB cursor
        return dumps(annotations)

    # add an annotation for the dataObjectId
    def addAnnotation(self, dataId, annotationText):
        #connect2DB
        collection = self.getCollection()

        #build json
        insertJson = {"annotationText": annotationText, "addedDate": datetime.utcnow()}
        insertJson["dataObjectId"] = dataId

        #SQL Equivalent: Insert into t_annotations ("annotationText") values (annotationText) where dataObjectId = dataObjectId
        result = collection.insert_one(insertJson)
        # return new annotationObjectId
        return str(result.inserted_id)

    # edit an annotation for the annotationObjectId
    def editAnnotation(self, annotationObjectId, annotationText):
        #connect2DB
        collection = self.getCollection()
        updateId = {"_id" : ObjectId(annotationObjectId)}
        updateText = {"$set": {"annotationText":annotationText},
                      "$currentDate": {"lastModified": True}}

        #SQL Equivalent: Update t_annotations set ("annotationText" = annotationText) where dataObjectId = dataObjectId
        result = collection.update_one(updateId, updateText)

        # return the annotationObjectId that was updated
        return result.modified_count;

    #delete an annotation for the annotationObjectId
    def deleteAnnotation(self, annotationObjectId):
        #connect2DB
        collection = self.getCollection()
        deleteJson = {"_id" : ObjectId(annotationObjectId)}
        result = collection.delete_one(deleteJson)

        # reutrn the number of documents deleted
        return result.deleted_count

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForData(self, dataId):
       #connect2DB
        collection = self.getCollection()
        deleteJson = {"dataObjectId": dataId}
        result = collection.delete_many(deleteJson)

        # reutrn the number of documents deleted
        return result.deleted_count

#BELOW IS FOR TESGING
# obj = Annotations()
# #1)Find
# dataId = "20160927"
# #print (obj.getAnnotation(dataId))
# #2)Insert
# annotationText = "Testing annotation text"
# insertJson = {"dataObjectId":dataId, "annotationText":annotationText}
# #print (obj.addAnnotation(dataId, insertJson))
# #3)Update
# annotationObjectId = "57eb06fd231bad1b6c195e16"
# annotationText = "UPDATED annotation text"
# print (obj.editAnnotation(annotationObjectId, annotationText))
# #4)Delete by annObjId
# #print (obj.deleteAnnotation(annotationObjectId))
# #5)Delete by dataId
# #print (obj.deleteAllAnnotationsForData(dataId))
