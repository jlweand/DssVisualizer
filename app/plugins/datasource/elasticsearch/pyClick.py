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


class PyClick:

    def __init__(self):
        self.esIndex = Common().getIndexName()
        self.clickDocType = "click"
        self.resultSize = Common().getSizeToReturn()

    def importClick(self, jsonObjects):
        es = Elasticsearch()
        es.indices.create(index=self.esIndex, ignore=400)
        insertedCount = 0
        for json in jsonObjects:
            result = es.index(index=self.esIndex, doc_type=self.clickDocType, body=json)
            insertedCount += result["_shards"]["successful"]
        return insertedCount

    # select data by date range of the 'start' column
    def selectClickData(self, startDate, endDate, techNames, eventNames, eventTechNames):
        select = Selecting().generateSelectQuery(startDate, endDate, techNames, eventNames, eventTechNames, True, False)
        data = Elasticsearch().search(index=self.esIndex, doc_type=self.clickDocType, size=self.resultSize, body=select)
        return Selecting().fixAllTheData(data)

    # select single data point
    def selectClickDataById(self, dataId):
        data = Elasticsearch().get(index=self.esIndex, doc_type=self.clickDocType, id=dataId)
        return Selecting().fixOneData(data)

    # add or edits a fixedData record to this data point
    def modifyFixedClickData(self, dataId, clicks_id, content, className, start, title, typeClick, isDeleted):
        updateFixed = {"doc": {
            "fixedData": {"clicks_id": clicks_id, "content": content, "className": className, "start": start,
                          "title": title, "type": typeClick, "isDeleted": isDeleted}}}
        result = Elasticsearch().update(index=self.esIndex, doc_type=self.clickDocType, body=updateFixed, id = dataId)
        return Common().getModfiedCount(result)

    # delete the fixedData
    def deleteFixedClickData(self, dataId):
        deleteFixed = {"script" : "ctx._source.remove(\"fixedData\")"}
        result = Elasticsearch().update(index=self.esIndex, doc_type=self.clickDocType, body=deleteFixed, id = dataId)
        return Common().getModfiedCount(result)

    # add or edit an annotation to the object.  This will add a single 'annotation' attribute to the object.
    def modifyAnnotationClick(self, dataId, annotationText):
        return Annotations().modifyAnnotation(self.clickDocType, dataId, annotationText)

    # add an annotation to an array of annotations for the dataId
    def addAnnotationToArrayClick(self, dataId, annotationText):
        return Annotations().addAnnotationToArray(self.clickDocType, dataId, annotationText)

    # edit an annotation in the array of annotations.
    def editAnnotationInArrayClick(self, dataId, oldAnnotationText, newAnnotationText):
        return Annotations().editAnnotationInArray(self.clickDocType, dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation from array for the dataId
    def deleteAnnotationFromArrayClick(self, dataId, annotationText):
        return Annotations().deleteAnnotationFromArray(self.clickDocType, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForClick(self, dataId):
        return Annotations().deleteAllAnnotationsForData(self.clickDocType, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToClickTimeline(self, click, annotationText):
        return Annotations().addAnnotationToTimeline(self.clickDocType, click, annotationText)
