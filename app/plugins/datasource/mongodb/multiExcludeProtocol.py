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
from datetime import datetime
from plugins.datasource.mongodb.annotations import Annotations
from plugins.datasource.mongodb.common import Common
from pprint import pprint


class MultiExcludeProtocol:
    def getMultiExcludeProtocolCollection(self):
        return Common().getDatabase().multiExcludeProtocol

    def importMultiExcludeProtocolData(self, json):
        collection = self.getMultiExcludeProtocolCollection()
        result = collection.insert_many(json)
        Common().addIndex(collection, True)
        return len(result.inserted_ids)

    # select data by date range of the 'start' column
    def selectMultiExcludeProtocolData(self, startDate, endDate, techName, eventName, eventTechList):
        collection = self.getMultiExcludeProtocolCollection()
        findJson = Common().getSelectJsonQuery(startDate, endDate, techName, eventName, eventTechList, True, False)
        cursor = collection.find(findJson)
        return Common().formatOutput(cursor)

    # select single data point
    def selectMultiExcludeProtocolDataById(self, dataId):
        collection = self.getMultiExcludeProtocolCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return Common().formatOutput(cursor)

    # add or edits a fixedData record to this data point
    def modifyFixedMultiExcludeProtocolData(self, dataId, traffic_all_id, content, className, title, startDate,  isDeleted):
        collection = self.getMultiExcludeProtocolCollection()
        updateId = {"_id": ObjectId(dataId)}
        updateText = {"$set": {
            "fixedData": {"traffic_all_id": traffic_all_id, "content": content, "className": className, "title": title,
                          "start": startDate, "isDeleted": isDeleted}}}
        result = collection.update_one(updateId, updateText)
        return result.modified_count

    # delete the fixedData
    def deleteFixedMultiExcludeProtocolData(self, dataId):
        collection = self.getMultiExcludeProtocolCollection()
        deleteId = {"_id": ObjectId(dataId)}
        deleteText = {"$unset": {"fixedData": ""}}
        result = collection.update_one(deleteId, deleteText)
        return result.modified_count

    # add an annotation for the dataId
    def modifyAnnotationMultiExcludeProtocol(self, dataId, annotationText):
        collection = self.getMultiExcludeProtocolCollection()
        return Annotations().modifyAnnotation(collection, dataId, annotationText)

    # add an annotation for the dataId
    def addAnnotationToArrayMultiExcludeProtocol(self, dataId, annotationText):
        collection = self.getMultiExcludeProtocolCollection()
        return Annotations().addAnnotationToArray(collection, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationInArrayMultiExcludeProtocol(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getMultiExcludeProtocolCollection()
        return Annotations().editAnnotationInArray(collection, dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation for the dataId
    def deleteAnnotationFromArrayMultiExcludeProtocol(self, dataId, annotationText):
        collection = self.getMultiExcludeProtocolCollection()
        return Annotations().deleteAnnotationFromArray(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForMultiExcludeProtocol(self, dataId):
        collection = self.getMultiExcludeProtocolCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToMultiExcludeProtocolTimeline(self, multiExclude, annotationText):
        collection = self.getMultiExcludeProtocolCollection()
        return Annotations().addAnnotationToTimeline(collection, multiExclude, annotationText)
