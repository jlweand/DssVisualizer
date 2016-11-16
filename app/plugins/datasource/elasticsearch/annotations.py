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

from plugins.datasource.elasticsearch.common import Common
from elasticsearch import Elasticsearch

from pprint import pprint

class Annotations:
    """This class holds the logic to adding an annotation to any data point.
    Each method must be passed the collection of the data that is being modified."""

    def __init__(self):
        self.esIndex = Common().getIndexName()

    # add an annotation for the dataId
    def addAnnotation(self, doc_type, dataId, annotationText):
        """Adds an annotation to a data point. If the annotation already exists nothing is done.
        If the annotation does not exist, this one is added to the list.

        :param doc_type: The doc_type in which the data lives.
        :type doc_type: str
        :param dataId: The ObjectId of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The text of the annotation.
        :type annotationText: str
        :returns: modified_count
        """
        document = Elasticsearch().get(index=self.esIndex, doc_type=doc_type, id=dataId)
        doc = document["_source"]
        hasSameAnnotation = False

        try:
            # if the data already has the annotation attribute
            annotations = doc["annotations"]
            # check to see if there exists an attribute with the same text
            for annotation in annotations:
                if annotation["annotation"] == annotationText:
                    hasSameAnnotation = True
                    break
            # if no attribute exists with the same 'annotationText', add it.
            if not hasSameAnnotation:
                doc["annotations"].append({"annotation": annotationText})

        except KeyError:
            # the data doesn't have any annotations, so add it.
            doc["annotations"] = []
            doc["annotations"].append({"annotation": annotationText })

        if hasSameAnnotation:
            # we did nothing to the data, so return 0 for modified count
            return 0
        else:
            # update the document.
            updateDoc = { "doc": doc }
            result = Elasticsearch().update(index=self.esIndex, doc_type=doc_type, id=dataId, body=updateDoc)
            return Common().getModfiedCount(result)

    # edit an annotation for the dataId
    def editAnnotation(self, doc_type, dataId, oldAnnotationText, newAnnotationText):
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
        document = Elasticsearch().get(index=self.esIndex, doc_type=doc_type, id=dataId)
        doc = document["_source"]
        hasSameAnnotation = False

        annotations = doc["annotations"]
        # check to see if there exists an attribute with the same text
        for annotation in annotations:
            if annotation["annotation"] == oldAnnotationText:
                annotation["annotation"] = newAnnotationText
                hasSameAnnotation = True
                break

        if hasSameAnnotation:
            # update the document.
            updateDoc = { "doc": doc }
            result = Elasticsearch().update(index=self.esIndex, doc_type=doc_type, id=dataId, body=updateDoc)
            return Common().getModfiedCount(result)
        else:
            # we did nothing to the data, so return 0 for modified count
            return 0

    #delete an annotation for the dataId
    def deleteAnnotation(self, doc_type, dataId, annotationText):
        """Removes an annotation from a data point.

        :param collection: The collection in which the data lives.
        :type collection: MongoDb collection
        :param dataId: The ObjectId of the data to delete the annotation from.
        :type dataId: str
        :param annotationText: The text of the annotation to remove.
        :type annotationText: str
        :returns: modified_count
        """
        document = Elasticsearch().get(index=self.esIndex, doc_type=doc_type, id=dataId)
        doc = document["_source"]
        hasSameAnnotation = False

        annotations = doc["annotations"]
        # check to see if there exists an attribute with the same text
        for annotation in annotations:
            if annotation["annotation"] == annotationText:
                annotation["annotation"] = ""
                hasSameAnnotation = True
                break

        if hasSameAnnotation:
            # update the document.
            updateDoc = { "doc": doc }
            result = Elasticsearch().update(index=self.esIndex, doc_type=doc_type, id=dataId, body=updateDoc)
            return Common().getModfiedCount(result)
        else:
            # we did nothing to the data, so return 0 for modified count
            return 0

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForData(self, doc_type, dataId):
        """Deletes all annotations from a data point.

        :param collection: The collection in which the data lives.
        :type collection: MongoDb collection
        :param dataId: The ObjectId of the data to remove the annotations from.
        :type dataId: str
        :returns: modified_count
        """
        document = Elasticsearch().get(index=self.esIndex, doc_type=doc_type, id=dataId)
        doc = document["_source"]
        hasSameAnnotation = False

        try:
            # if the data already has the annotation attribute
            annotations = doc["annotations"]
            deleteText = {"script" : "ctx._source.remove(\"annotations\")"}
            result = Elasticsearch().update(index=self.esIndex, doc_type=doc_type, id=dataId, body=deleteText)
            return Common().getModfiedCount(result)

        except KeyError:
            # the data doesn't have any annotations.
            doc["annotations"] = []
            # we did nothing to the data, so return 0 for modified count
            return 0

    # # add an annotation to the timeline, not a datapoint
    # def addAnnotationToTimeline(self, doc_type, annotationText):
    #     """Adds an annotation to the collection as a new 'data point'.  This is not tied to any imported data.

    #     :param collection: The collection in which the data lives.
    #     :type collection: MongoDb collection
    #     :param jsonObject: The jsonObject to add the annotation to.
    #     :type jsonObject: JSON string
    #     :param annotationText: The text of the annotation.
    #     :type annotationText: str
    #     :returns: inserted_id
    #     """
    #     ##########################################################################################
    #     # update the document.
    #     jsonObject = {"annotation": annotationText}

    #     # pprint("jsonObject")
    #     # pprint(jsonObject)

    #     result = Elasticsearch().index(index=self.esIndex, doc_type=doc_type, body=jsonObject)
    #     return Common().getModfiedCount(result)
    #     ##########################################################################################

    #     # jsonObject["annotations"] = {"annotation": annotationText}
    #     # result = collection.insert_one(jsonObject)
    #     # return result.inserted_id
