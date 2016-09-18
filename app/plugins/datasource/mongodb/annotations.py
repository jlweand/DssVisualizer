from pymongo import MongoClient

class Annotations:

    # get all annotations for the dataObjectId
    def getAnnotations(self, dataObjectId):
        return 0;

    # add an annotation for the dataObjectId
    def addAnnotation(self, dataObjectId):
        # return new annotationObjectId
        return 0;

    # edit an annotation for the annotationObjectId
    # i'm not sure if you'll need the dataObjectId for this,
    # so feel free to take it out if need be.
    def editAnnotation(self, dataObjectId, annotationObjectId):
        # return the annotationObjectId that was updated
        return 0;

    # delete an annotation for the annotationObjectId
    def deleteAnnotation(self, annotationObjectId):
        # reutrn the number of documents deleted
        return 0;

    # deletes all annotations for the dataObjectId
    def deleteAllAnnotationsForData(self, dataObjectId):
        # reutrn the number of documents deleted
        return 0;
