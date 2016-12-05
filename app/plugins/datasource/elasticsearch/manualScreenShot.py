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


class ManualScreenShot:

    def __init__(self):
        self.esIndex = Common().getIndexName()
        self.manualScreenShotDocType = "manualscreenshot"
        self.resultSize = Common().getSizeToReturn()

    def importManualScreenShot(self, jsonObjects):
        es = Elasticsearch()
        es.indices.create(index=self.esIndex, ignore=400)
        insertedCount = 0
        for json in jsonObjects:
            result = es.index(index=self.esIndex, doc_type=self.manualScreenShotDocType, body=json)
            insertedCount += result["_shards"]["successful"]
        return insertedCount

    # select data by date range of the 'start' column
    def selectManualScreenShotData(self, startDate, endDate, techNames, eventNames, eventTechNames):
        select = Common().generateSelectQuery(startDate, endDate, techNames, eventNames, eventTechNames, True, False)
        data = Elasticsearch().search(index=self.esIndex, doc_type=self.manualScreenShotDocType, size=self.resultSize, body=select)
        return Common().fixAllTheData(data)

    # select single data point
    def selectManualScreenShotDataById(self, dataId):
        data = Elasticsearch().get(index=self.esIndex, doc_type=self.manualScreenShotDocType, id=dataId)
        return Common().fixOneData(data)

    # add or edits a fixedData record to this data point
    def modifyFixedManualScreenShotData(self, dataId, manualscreen_id, content, className, start, title, typeManualScreenShot, comment, isDeleted):
        updateFixed = {"doc": {
            "fixedData": {"manualscreen_id": manualscreen_id, "content": content, "className": className, "start": start,
                          "title": title, "type": typeManualScreenShot, "comment": comment, "isDeleted": isDeleted}}}
        result = Elasticsearch().update(index=self.esIndex, doc_type=self.manualScreenShotDocType, body=updateFixed, id = dataId)
        return Common().getModfiedCount(result)

    # delete the fixedData
    def deleteFixedManualScreenShotData(self, dataId):
        deleteFixed = {"script" : "ctx._source.remove(\"fixedData\")"}
        result = Elasticsearch().update(index=self.esIndex, doc_type=self.manualScreenShotDocType, body=deleteFixed, id = dataId)
        return Common().getModfiedCount(result)

    # add an annotation for the dataId
    def addAnnotationManualScreenShot(self, dataId, annotationText):
        return Annotations().addAnnotation(self.manualScreenShotDocType, dataId, annotationText)

    # add an annotation for the dataId
    def addAnnotationToArrayManualScreenShot(self, dataId, annotationText):
        return Annotations().addAnnotationToArray(self.manualScreenShotDocType, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationManualScreenShot(self, dataId, oldAnnotationText, newAnnotationText):
        return Annotations().editAnnotation(self.manualScreenShotDocType, dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation for the dataId
    def deleteAnnotationManualScreenShot(self, dataId, annotationText):
        return Annotations().deleteAnnotation(self.manualScreenShotDocType, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForManualScreenShot(self, dataId):
        return Annotations().deleteAllAnnotationsForData(self.manualScreenShotDocType, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToManualScreenShotTimeline(self, manualScreenShot, annotationText):
        return Annotations().addAnnotationToTimeline(self.manualScreenShotDocType, manualScreenShot, annotationText)

    # def getDistinctTechNamesForEvents(self, eventNames):
    #     collection = self.getManualScreenShotCollection()
    #     return TechAndEventNames().getDistinctTechNamesForEvents(collection, eventNames)
    #
    # def getDistinctEventNames(self):
    #     collection = self.getManualScreenShotCollection()
    #     return TechAndEventNames().getDistinctEventNames(collection)
    #
    # def getDistinctTechAndEventNames(self):
    #     collection = self.getManualScreenShotCollection()
    #     return TechAndEventNames().getDistinctTechAndEventNames(collection)