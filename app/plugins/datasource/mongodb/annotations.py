from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps

class Annotations:

    def getCollection(self):
        client = MongoClient()
        db = client.dssvisualizer
        return db.annotations

    # get all annotations for the dataObjectId
    def getAnnotation(self, dataId):
        #connect2DB
        collection = self.getCollection()
        findJson = {"dataObjectId":dataId}

        #SQL Equivalent: Select * from t_annotations where dataObjectId = dataObjectId
        annotation = collection.find(findJson)

        # dump it into a JSON string from a MongoDB cursor
        return dumps(annotation)

    # add an annotation for the dataObjectId
    def addAnnotation(self, dataId, annotationText):
        #connect2DB
        collection = self.getCollection()

        # need to make the objectId match what MongoDB uses. ElasticSearch will be different.
        #build json
        insertJson = {"annotationText":annotationText}
        insertJson["dataObjectId"] = ObjectId(dataId)

        #SQL Equivalent: Insert into t_annotations ("annotationText") values (annotationText) where dataObjectId = dataObjectId
        result = collection.insert_one(insertJson)
        # return new annotationObjectId
        return result.inserted_id;

    # edit an annotation for the annotationObjectId
    def editAnnotation(self, annotationObjectId, annotationText):
        #connect2DB
        collection = self.getCollection()
        upAnnObjId = annotationObjectId
        updateJson1 = {"_id" : ObjectId(annotationObjectId)}
        updateJson2 = {"$set": {"annotationText":annotationText}}

        #SQL Equivalent: Update t_annotations set ("annotationText" = annotationText) where dataObjectId = dataObjectId
        collection.update (updateJson1, updateJson2)
       
        # return the annotationObjectId that was updated
        return upAnnObjId;

    #delete an annotation for the annotationObjectId
    def deleteAnnotation(self, annotationObjectId):
        #connect2DB
        collection = self.getCollection()
        deleteJson = {"_id" : ObjectId(annotationObjectId)}
        
        delByAnnObjIdCount = 0
        #For each time select statement finds the annotationObjectId, it will delete that from the collection
        for each in collection.find(deleteJson):
            #SQL Equivalent: delete from t_annotations where (annotationObjectId = annotationObjectId)
            collection.remove (deleteJson)
            delByAnnObjIdCount += 1

        # reutrn the number of documents deleted
        return delByAnnObjIdCount

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForData(self, dataId):
       #connect2DB
        collection = self.getCollection()
        deleteJson = {"dataObjectId":dataId}

        delByDataIdCount = 0
        #For each time select statement finds the DataId, it will delete that from the collection
        for each in collection.find(deleteJson):
            #SQL Equivalent: delete from t_annotations where (annotationObjectId = annotationObjectId)
            collection.remove (deleteJson)
            delByDataIdCount += 1
        
        # reutrn the number of documents deleted
        return delByDataIdCount

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