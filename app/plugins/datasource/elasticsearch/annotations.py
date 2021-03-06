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
    def modifyAnnotation(self, doc_type, dataId, annotationText):
        """Adds or updates an annotation to a data point. Using this method will allow only one annotation per data point.
        If the annotation already exists it will be updated. If the annotation does not exist, it will be added.

        :param doc_type: The collection in which the data lives.
        :type doc_type: str
        :param dataId: The ObjectId of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The text of the annotation.
        :type annotationText: str
        :returns: modified_count
        """
        insertFixed = {"doc": { "annotation": annotationText } }
        result = Elasticsearch().update(index=self.esIndex, doc_type=doc_type, body=insertFixed, id = dataId)
        return Common().getModfiedCount(result)

    def addAnnotationToArray(self, doc_type, dataId, annotationText):
        """Adds an annotation to a data point in an array. If the annotation already exists nothing is done.
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
    def editAnnotationInArray(self, doc_type, dataId, oldAnnotationText, newAnnotationText):
        """Edits an annotation in the array of annotations on a data point.

        :param doc_type: The doc_type in which the data lives.
        :type doc_type: str
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
    def deleteAnnotationFromArray(self, doc_type, dataId, annotationText):
        """Removes an annotation from the array of annotations on a data point.

        :param doc_type: The doc_type in which the data lives.
        :type doc_type: str
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
                doc["annotations"].remove({"annotation": annotationText})
                hasSameAnnotation = True
                break

        if hasSameAnnotation:
            #update the document.
            updateDoc = { "doc": doc }
            result = Elasticsearch().update(index=self.esIndex, doc_type=doc_type, id=dataId, body=updateDoc)
            return Common().getModfiedCount(result)
        else:
            # we did nothing to the data, so return 0 for modified count
            return 0

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForData(self, doc_type, dataId):
        """Deletes all annotations from a data point.

        :param doc_type: The doc_type in which the data lives.
        :type doc_type: str
        :param dataId: The ObjectId of the data to remove the annotations from.
        :type dataId: str
        :returns: modified_count
        """
        esIndex = Common().getIndexName()
        doc = { "script" : "ctx._source.remove(\"annotations\")" }
        result = Elasticsearch().update(index=esIndex, doc_type=doc_type, id=dataId, body=doc)
        doc = { "script" : "ctx._source.remove(\"annotation\")" }
        result = Elasticsearch().update(index=esIndex, doc_type=doc_type, id=dataId, body=doc)
        return Common().getModfiedCount(result)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToTimeline(self, doc_type, jsonObject, annotationText):
        """Adds an annotation to the collection as a new 'data point'.  This is not tied to any imported data.

        :param doc_type: The doc_type in which the data lives.
        :type doc_type: str
        :param jsonObject: The jsonObject to add the annotation to.
        :type jsonObject: JSON string
        :param annotationText: The text of the annotation.
        :type annotationText: str
        :returns: inserted_id
        """
        jsonObject["content"] = annotationText
        result = Elasticsearch().index(index=self.esIndex, doc_type=doc_type, body=jsonObject)
        return Common().getInsertedId(result)