from bson import ObjectId
from plugins.datasource.mongodb.common import Common

class Annotations:

    # add an annotation for the dataId
    def addAnnotation(self, collection, dataId, annotationText):
        updateId = {"_id" : ObjectId(dataId)}
        push = { "$addToSet": { "annotations": { "annotation": annotationText } } }

        result = collection.update_one(updateId, push)
        return result.modified_count

    # edit an annotation for the dataId
    def editAnnotation(self, collection, dataId, oldAnnotationText, newAnnotationText):
        updateId = {"_id" : ObjectId(dataId), "annotations.annotation" : oldAnnotationText}
        updateText = {"$set": { "annotations.$": {"annotation":  newAnnotationText} } }

        result = collection.update_one(updateId, updateText)
        return result.modified_count;

    #delete an annotation for the dataId
    def deleteAnnotation(self, collection, dataId, annotationText):
        deleteId = {"_id" : ObjectId(dataId)}
        deleteText = {"$pull" : { "annotations": { "annotation" : annotationText } } }
        result = collection.update_one(deleteId, deleteText)
        return result.modified_count

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForData(self, collection, dataId):
        deleteId = {"_id" : ObjectId(dataId)}
        deleteText = {"$set" : {"annotations": [] } }
        result = collection.update_one(deleteId, deleteText)
        return result.modified_count
