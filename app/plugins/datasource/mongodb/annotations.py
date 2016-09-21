from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
#json as parameter

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
    def addAnnotation(self, dataId, insertJson):
        #connect2DB
        collection = self.getCollection()

        # need to make the objectId match what MongoDB uses. ElasticSearch will be different.
        # insertJson["dataObjectId"] = ObjectId(dataId)
        insertJson["dataObjectId"] = dataId

        #SQL Equivalent: Insert into t_annotations ("annotationText") values (annotationText) where dataObjectId = dataObjectId
        #newAnnObjId = db.annotations.insert ({"dataObjectId":dataObjectId, "annotationText":annotationText})
        result = collection.insert_one(insertJson)
        # return new annotationObjectId
        return result.inserted_id;

    # # edit an annotation for the annotationObjectId
    # # i'm not sure if you'll need the dataObjectId for this,
    # # so feel free to take it out if need be.
    # def editAnnotation(self, annotationObjectId, annotationText):
    #     #connect2DB
    #     import pymongo
    #     client = pymongo.MongoClient()
    #     db = client.test
    #     #SQL Equivalent: Update t_annotations set ("annotationText" = annotationText) where dataObjectId = dataObjectId
    #     upAnnObjId = annotationObjectId
    #     db.annotations.update ({"_id" : ObjectId(annotationObjectId)}, {"annotationText":annotationText}, False, False)
    #     #disconnectFromDB
    #     db = client.close()
    #     print ("UPDATING DONE")
    #     print (" ")
    #     # return the annotationObjectId that was updated
    #     return upAnnObjId;

    # # delete an annotation for the annotationObjectId
    # def deleteAnnotation(self, annotationObjectId):
    #     #connect2DB
    #     import pymongo
    #     client = pymongo.MongoClient()
    #     db = client.test
    #     delByAnnObjIdCount = 0
    #     #SQL Equivalent: delete from t_annotations where (annotationObjectId = annotationObjectId)
    #     for each in db.annotations.remove ({"_id" : ObjectId(annotationObjectId)}):
    #         delByAnnObjIdCount = delByAnnObjIdCount + 1
    #     #disconnectFromDB
    #     db = client.close()
    #     print ("DELETION BY ANNOTATION OBJECT ID DONE")
    #     print (" ")
    #     # reutrn the number of documents deleted
    #     return delByAnnObjIdCount;

    # # deletes all annotations for the dataObjectId
    # def deleteAllAnnotationsForData(self, dataObjectId):
    #     #connect2DB
    #     import pymongo
    #     client = pymongo.MongoClient()
    #     db = client.test
    #     delByDataObjIdCount = 0
    #     #SQL Equivalent: delete from t_annotations where (annotationObjectId = annotationObjectId)
    #     for each in db.annotations.remove ({"dataObjectId":dataObjectId}):
    #         delByDataObjIdCount = delByDataObjIdCount + 1
    #     #disconnectFromDB
    #     db = client.close()
    #     print ("DELETION BY DATA OBJECT ID DONE")
    #     print (" ")
    #     # reutrn the number of documents deleted
    #     return delByDataObjIdCount;

# obj = CAnnotations()
#1)
# dataObjectId = "19950915"
# findJson1 = {"dataObjectId":dataObjectId}
# findJson2 = {"_id":0, "dataObjectId":1, "annotationText":1}
# obj.getAnnotation(findJson1, findJson2)
#2)
# annotationText = "This is a test for Practicum Class"
# insertJson = {"dataObjectId":dataObjectId, "annotationText":annotationText}
# newAnnObjId = obj.addAnnotation(insertJson)
# print (newAnnObjId)
#3)
# annotationObjectId = "57e1ec72231bad0fd891816e"
# annotationText = "Once again, test for Practicum Course"
# upAnnObjId = obj.editAnnotation(annotationObjectId, annotationText)
# print (upAnnObjId)
# #4)
# delByAnnObjIdCount = obj.deleteAnnotation(annotationObjectId)
# print (delByAnnObjIdCount)
#5)
# delByDataObjIdCount = obj.deleteAllAnnotationsForData(dataObjectId)
# print (delByDataObjIdCount)
