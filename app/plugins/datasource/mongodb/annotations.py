from bson import ObjectId
from pprint import pprint

class Annotations:
    """This class holds the logic to adding an annotation to any data point.
    Each method must be passed the collection of the data that is being modified."""

    # add an annotation for the dataId
    def addAnnotation(self, collection, dataId, annotationText):
        """Adds an annotation to a data point. If the annotation already exists nothing is done.
        If the annotation does not exist, this one is added to the list.

        :param collection: The collection in which the data lives.
        :type collection: MongoDb collection
        :param dataId: The ObjectId of the data to add the anotation to.
        :type dataId: str
        :param annotationText: The text of the annotation.
        :type annotationText: str
        :returns: modified_count
        """
        updateId = {"_id" : ObjectId(dataId)}
        push = { "$addToSet": { "annotations": { "annotation": annotationText } } }

        result = collection.update_one(updateId, push)
        return result.modified_count

    # edit an annotation for the dataId
    def editAnnotation(self, collection, dataId, oldAnnotationText, newAnnotationText):
        """Edits an annotation on a data point.

        :param collection: The collection in which the data lives.
        :type collection: MongoDb collection
        :param dataId: The ObjectId of the data to edit the anotation.
        :type dataId: str
        :param oldAnnotationText: The old version of the text of the annotation.
        :type oldAnnotationText: str
        :param newAnnotationText: The new annotation text.
        :type newAnnotationText: str
        :returns: modified_count
        """
        updateId = {"_id" : ObjectId(dataId), "annotations.annotation" : oldAnnotationText}
        updateText = {"$set": { "annotations.$": {"annotation":  newAnnotationText} } }

        result = collection.update_one(updateId, updateText)
        return result.modified_count;

    #delete an annotation for the dataId
    def deleteAnnotation(self, collection, dataId, annotationText):
        """Removes an annotation from a data point.

        :param collection: The collection in which the data lives.
        :type collection: MongoDb collection
        :param dataId: The ObjectId of the data to delete the anotation from.
        :type dataId: str
        :param annotationText: The text of the annotation to remove.
        :type annotationText: str
        :returns: modified_count
        """
        deleteId = {"_id" : ObjectId(dataId)}
        deleteText = {"$pull" : { "annotations": { "annotation" : annotationText } } }
        result = collection.update_one(deleteId, deleteText)
        return result.modified_count

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForData(self, collection, dataId):
        """Deletes all annotations from a data point.

        :param collection: The collection in which the data lives.
        :type collection: MongoDb collection
        :param dataId: The ObjectId of the data to remove the anotations from.
        :type dataId: str
        :returns: modified_count
        """
        deleteId = {"_id" : ObjectId(dataId)}
        deleteText = {"$set" : {"annotations": [] } }
        result = collection.update_one(deleteId, deleteText)
        return result.modified_count

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToTimeline(self, collection, jsonObject, annotationText):
        """Adds an annotation to the collection as a new 'data point'.  This is not tied to any imported data.

        :param collection: The collection in which the data lives.
        :type collection: MongoDb collection
        :param jsonObject: The jsonObject to add the annotation to.
        :type jsonObject: JSON string
        :param annotationText: The text of the annotation.
        :type annotationText: str
        :returns: inserted_id
        """
        jsonObject["annotations"] = {"annotation": annotationText}
        result = collection.insert_one(jsonObject)
        return result.inserted_id
