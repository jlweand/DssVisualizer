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


class MultiIncludeThroughput:

    def __init__(self):
        self.esIndex = Common().getIndexName()
        self.multiIncludeThroughputDocType = "multiincludethroughput"
        self.resultSize = Common().getSizeToReturn()

    def importMultiIncludeThroughputData(self, jsonObjects):
        es = Elasticsearch()
        es.indices.create(index=self.esIndex, ignore=400)
        insertedCount = 0
        for json in jsonObjects:
            result = es.index(index=self.esIndex, doc_type=self.multiIncludeThroughputDocType, body=json)
            insertedCount += result["_shards"]["successful"]
        return insertedCount

    # select data by date range of the 'start' column
    def selectMultiIncludeThroughputData(self, startDate, endDate, techNames, eventNames, eventTechNames):
        select = Common().generateSelectQuery(startDate, endDate, techNames, eventNames, eventTechNames, False, True)
        data = Elasticsearch().search(index=self.esIndex, doc_type=self.multiIncludeThroughputDocType, size=self.resultSize, body=select)
        return Common().fixAllTheData(data)

    # select single data point
    def selectMultiIncludeThroughputDataById(self, dataId):
        data = Elasticsearch().get(index=self.esIndex, doc_type=self.multiIncludeThroughputDocType, id=dataId)
        return Common().fixOneData(data)

    # add a fixedData record to this data point
    def insertFixedMultiIncludeThroughputData(self, dataId, traffic_xy_id, className, x, y, isDeleted):
        insertFixed = {"doc": {"fixedData": {"traffic_xy_id": traffic_xy_id, "className": className, "x": x, "y": y, "isDeleted": isDeleted}}}
        result = Elasticsearch().update(index=self.esIndex, doc_type=self.multiIncludeThroughputDocType, body=insertFixed, id = dataId)
        return Common().getModfiedCount(result)

    # update a previously 'fixed' record.
    def updateFixedMultiIncludeThroughputData(self, dataId, traffic_xy_id, className, x, y, isDeleted):
        updateFixed = {"doc": {"fixedData": {"traffic_xy_id": traffic_xy_id, "className": className, "x": x, "y": y, "isDeleted": isDeleted}}}
        result = Elasticsearch().update(index=self.esIndex, doc_type=self.multiIncludeThroughputDocType, body=updateFixed, id = dataId)
        return Common().getModfiedCount(result)

    # delete the fixedData
    def deleteFixedMultiIncludeThroughputData(self, dataId):
        deleteFixed = {"script" : "ctx._source.remove(\"fixedData\")"}
        result = Elasticsearch().update(index=self.esIndex, doc_type=self.multiIncludeThroughputDocType, body=deleteFixed, id = dataId)
        return Common().getModfiedCount(result)

    # add an annotation for the dataId
    def addAnnotationMultiIncludeThroughput(self, dataId, annotationText):
        return Annotations().addAnnotation(self.multiIncludeThroughputDocType, dataId, annotationText)

    # add an annotation for the dataId
    def addAnnotationToArrayMultiIncludeThroughput(self, dataId, annotationText):
        return Annotations().addAnnotationToArray(self.multiIncludeThroughputDocType, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationMultiIncludeThroughput(self, dataId, oldAnnotationText, newAnnotationText):
        return Annotations().editAnnotation(self.multiIncludeThroughputDocType, dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation for the dataId
    def deleteAnnotationMultiIncludeThroughput(self, dataId, annotationText):
        return Annotations().deleteAnnotation(self.multiIncludeThroughputDocType, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForMultiIncludeThroughput(self, dataId):
        return Annotations().deleteAllAnnotationsForData(self.multiIncludeThroughputDocType, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToMultiIncludeThroughputTimeline(self, multiExclude, annotationText):
        return Annotations().addAnnotationToTimeline(self.multiIncludeThroughputDocType, multiExclude, annotationText)

    def getDistinctTechNamesForEvents(self, eventNames):
        collection = self.getMultiIncludeThroughputCollection()
        return TechAndEventNames().getDistinctTechNamesForEvents(collection, eventNames)

    def getDistinctEventNames(self):
        collection = self.getMultiIncludeThroughputCollection()
        return TechAndEventNames().getDistinctEventNames(collection)

    def getDistinctTechAndEventNames(self):
        collection = self.getMultiIncludeThroughputCollection()
        return TechAndEventNames().getDistinctTechAndEventNames(collection)
