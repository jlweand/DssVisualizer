#  Copyright (C) 2016  Jamie Acosta, Jennifer Weand, Juan Soto, Mark Eby, Mark Smith, Andres Olivas
#
# This file is part of DssVisualizer.
#
# DssVisualizer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DssVisualizer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DssVisualizer.  If not, see <http://www.gnu.org/licenses/>.

from bson import ObjectId

class Annotations:
    """This class holds the logic to adding an annotation to any data point.
    Each method must be passed the collection of the data that is being modified."""

    # add an annotation for the dataId
    def addAnnotation(self, collection, dataId, annotationText):
        """Adds an annotation to a data point. If the annotation already exists nothing is done.
        If the annotation does not exist, this one is added to the list.

        :param collection: The collection in which the data lives.
        :type collection: MongoDb collection
        :param dataId: The ObjectId of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The text of the annotation.
        :type annotationText: str
        :returns: modified_count
        """
        updateId = {"_id" : ObjectId(dataId)}
        #if you want to have an array of annotations:
        # push = { "$addToSet": { "annotations": { "annotation": annotationText } } }
        #but it wasn't working with the UI so we only have one annotation
        push = { "$set": { "annotation": annotationText } }

        result = collection.update_one(updateId, push)
        return result.modified_count

    # edit an annotation for the dataId
    def editAnnotation(self, collection, dataId, oldAnnotationText, newAnnotationText):
        """Edits an annotation on a data point.

        :param collection: The collection in which the data lives.
        :type collection: MongoDb collection
        :param dataId: The ObjectId of the data to edit the annotation.
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
        :param dataId: The ObjectId of the data to delete the annotation from.
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
        :param dataId: The ObjectId of the data to remove the annotations from.
        :type dataId: str
        :returns: modified_count
        """
        deleteId = {"_id" : ObjectId(dataId)}
        deleteText = {"$unset" : {"annotations": "" } }
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
        jsonObject["content"] = annotationText
        result = collection.insert_one(jsonObject)
        return result.inserted_id
