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

from plugins.datasource.elasticsearch.annotations import Annotations
from plugins.datasource.elasticsearch.common import Common
from elasticsearch import Elasticsearch
from plugins.datasource.elasticsearch.selecting import Selecting


class MultiIncludeProtocol:

    def __init__(self):
        self.esIndex = Common().getIndexName()
        self.multiIncludeProtocolDocType = "multiincludeprotocol"
        self.resultSize = Common().getSizeToReturn()

    def importMultiIncludeProtocolData(self, jsonObjects):
        es = Elasticsearch()
        es.indices.create(index=self.esIndex, ignore=400)
        insertedCount = 0
        for json in jsonObjects:
            result = es.index(index=self.esIndex, doc_type=self.multiIncludeProtocolDocType, body=json)
            insertedCount += result["_shards"]["successful"]
        return insertedCount

    # select data by date range of the 'start' column
    def selectMultiIncludeProtocolData(self, startDate, endDate, techNames, eventNames, eventTechNames):
        select = Selecting().generateSelectQuery(startDate, endDate, techNames, eventNames, eventTechNames, True, False)
        data = Elasticsearch().search(index=self.esIndex, doc_type=self.multiIncludeProtocolDocType, size=self.resultSize, body=select)
        return Selecting().fixAllTheData(data)

    # select single data point
    def selectMultiIncludeProtocolDataById(self, dataId):
        data = Elasticsearch().get(index=self.esIndex, doc_type=self.multiIncludeProtocolDocType, id=dataId)
        return Selecting().fixOneData(data)

    # add or edits a fixedData record to this data point
    def modifyFixedMultiIncludeProtocolData(self, dataId, traffic_all_id, content, className, title, startDate, isDeleted):
        updateFixed = {"doc": {
            "fixedData": {"traffic_all_id": traffic_all_id, "content": content, "className": className, "title": title,
                          "start": startDate, "isDeleted": isDeleted}}}
        result = Elasticsearch().update(index=self.esIndex, doc_type=self.multiIncludeProtocolDocType, body=updateFixed, id = dataId)
        return Common().getModfiedCount(result)

    # delete the fixedData
    def deleteFixedMultiIncludeProtocolData(self, dataId):
        deleteFixed = {"script" : "ctx._source.remove(\"fixedData\")"}
        result = Elasticsearch().update(index=self.esIndex, doc_type=self.multiIncludeProtocolDocType, body=deleteFixed, id = dataId)
        return Common().getModfiedCount(result)

    # add or edit an annotation to the object.  This will add a single 'annotation' attribute to the object.
    def modifyAnnotationMultiIncludeProtocol(self, dataId, annotationText):
        return Annotations().modifyAnnotation(self.multiIncludeProtocolDocType, dataId, annotationText)

    # add an annotation to an array of annotations for the dataId
    def addAnnotationToArrayMultiIncludeProtocol(self, dataId, annotationText):
        return Annotations().addAnnotationToArray(self.multiIncludeProtocolDocType, dataId, annotationText)

    # edit an annotation in the array of annotations.
    def editAnnotationInArrayMultiIncludeProtocol(self, dataId, oldAnnotationText, newAnnotationText):
        return Annotations().editAnnotationInArray(self.multiIncludeProtocolDocType, dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation from array for the dataId
    def deleteAnnotationFromArrayMultiIncludeProtocol(self, dataId, annotationText):
        return Annotations().deleteAnnotationFromArray(self.multiIncludeProtocolDocType, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForMultiIncludeProtocol(self, dataId):
        return Annotations().deleteAllAnnotationsForData(self.multiIncludeProtocolDocType, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToMultiIncludeProtocolTimeline(self, multiIncludeProtocol, annotationText):
        return Annotations().addAnnotationToTimeline(self.multiIncludeProtocolDocType, multiIncludeProtocol, annotationText)
