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
from pprint import pprint


class PyClick:

    def __init__(self):
        self.size = Common().getSizeToReturn()
        self.clickDocType = "click"
        self.esIndex = Common().getIndexName()

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
        selectJson = Common().generateSelectQuery(startDate, endDate, techNames, eventNames, eventTechNames, True, False)
        data = Elasticsearch().search(index=self.esIndex, doc_type=self.clickDocType, size=self.size, body=selectJson)
        return Common().fixAllTheData(data)

    # select single data point
    def selectClickDataById(self, dataId):
        data = Elasticsearch().get(index=self.esIndex, doc_type=self.clickDocType, id=dataId)
        return Common().fixOneData(data)

    # add a fixedData record to this data point
    def insertFixedClickData(self, dataId, clicks_id, content, className, start, title, typeClick):
        body = {"doc": {
            "fixedData": {"clicks_id": clicks_id, "content": content, "className": className, "start": start,
                          "title": title, "type": typeClick}}}
        result = Elasticsearch().update(index=self.esIndex, doc_type=self.clickDocType, body=body, id = dataId)
        return Common().getModfiedCount(result)

    # update a previously 'fixed' record.
    def updateFixedClickData(self, dataId, clicks_id, content, className, start, title, typeClick):
        body = {"doc": {
            "fixedData": {"clicks_id": clicks_id, "content": content, "className": className, "start": start,
                          "title": title, "type": typeClick}}}
        result = Elasticsearch().update(index=self.esIndex, doc_type=self.clickDocType, body=body, id = dataId)
        return Common().getModfiedCount(result)

    # delete the fixedData
    def deleteFixedClickData(self, dataId):
        body = {"script" : "ctx._source.remove(\"fixedData\")"}
        result = Elasticsearch().update(index=self.esIndex, doc_type=self.clickDocType, body=body, id = dataId)
        return Common().getModfiedCount(result)

    # add an annotation for the dataId
    def addAnnotationClick(self, dataId, annotationText):
        return Annotations().addAnnotation(self.clickDocType, dataId, annotationText)

    # # edit an annotation for the dataId
    # def editAnnotationClick(self, dataId, oldAnnotationText, newAnnotationText):
    #     collection = self.getClickCollection()
    #     return Annotations().editAnnotation(collection, dataId, oldAnnotationText, newAnnotationText)

    # # delete an annotation for the dataId
    # def deleteAnnotationClick(self, dataId, annotationText):
    #     collection = self.getClickCollection()
    #     return Annotations().deleteAnnotation(collection, dataId, annotationText)

    # # deletes all annotations for the dataId
    # def deleteAllAnnotationsForClick(self, dataId):
    #     collection = self.getClickCollection()
    #     return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # # add an annotation to the timeline, not a datapoint
    # def addAnnotationToClickTimeline(self, click, annotationText):
    #     collection = self.getClickCollection()
    #     return Annotations().addAnnotationToTimeline(collection, click, annotationText)
