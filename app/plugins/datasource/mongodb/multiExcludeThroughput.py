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
from plugins.datasource.mongodb.annotations import Annotations
from plugins.datasource.mongodb.common import Common
from plugins.datasource.mongodb.techAndEventNames import TechAndEventNames

class MultiExcludeThroughput:

    def getMultiExcludeThroughputCollection(self):
        return Common().getDatabase().multiExcludeThroughput

    def importMultiExcludeThroughputData(self, json):
        collection = self.getMultiExcludeThroughputCollection()
        result = collection.insert_many(json)
        Common().addIndex(collection, False)
        return len(result.inserted_ids)

    # select data by date range of the 'start' column
    def selectMultiExcludeThroughputData(self, startDate, endDate, techName, eventName, eventTechList):
        collection = self.getMultiExcludeThroughputCollection()
        findJson = Common().getSelectJsonQuery(startDate, endDate, techName, eventName, eventTechList, False, True)
        cursor = collection.find(findJson)
        return Common().formatOutput(cursor)

    # select single data point
    def selectMultiExcludeThroughputDataById(self, dataId):
        collection = self.getMultiExcludeThroughputCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return Common().formatOutput(cursor)

    # add a fixedData record to this data point
    def insertFixedMultiExcludeThroughputData(self, dataId, traffic_xy_id, className, x, y, isDeleted):
        collection = self.getMultiExcludeThroughputCollection()
        updateId = {"_id": ObjectId(dataId)}
        fixedData = {"$set": {"fixedData": {"traffic_xy_id": traffic_xy_id, "className": className, "x": x, "y": y, "isDeleted": isDeleted}}}
        result = collection.update_one(updateId, fixedData)
        return result.modified_count

    # update a previously 'fixed' record.
    def updateFixedMultiExcludeThroughputData(self, dataId, traffic_xy_id, className, x, y, isDeleted):
        collection = self.getMultiExcludeThroughputCollection()
        updateId = {"_id": ObjectId(dataId)}
        fixedData = {"$set": {"fixedData": {"traffic_xy_id": traffic_xy_id, "className": className, "x": x, "y": y, "isDeleted": isDeleted}}}

        result = collection.update_one(updateId, fixedData)
        return result.modified_count

    # delete the fixedData
    def deleteFixedMultiExcludeThroughputData(self, dataId):
        collection = self.getMultiExcludeThroughputCollection()
        updateId = {"_id": ObjectId(dataId)}
        fixedData = {"$unset": {"fixedData": ""}}
        result = collection.update_one(updateId, fixedData)
        return result.modified_count

    # add an annotation for the dataId
    def addAnnotationMultiExcludeThroughput(self, dataId, annotationText):
        collection = self.getMultiExcludeThroughputCollection()
        return Annotations().addAnnotation(collection, dataId, annotationText)

    # add an annotation for the dataId
    def addAnnotationToArrayMultiExcludeThroughput(self, dataId, annotationText):
        collection = self.getMultiExcludeThroughputCollection()
        return Annotations().addAnnotationToArray(collection, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationMultiExcludeThroughput(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getMultiExcludeThroughputCollection()
        return Annotations().editAnnotation(collection, dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation for the dataId
    def deleteAnnotationMultiExcludeThroughput(self, dataId, annotationText):
        collection = self.getMultiExcludeThroughputCollection()
        return Annotations().deleteAnnotation(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForMultiExcludeThroughput(self, dataId):
        collection = self.getMultiExcludeThroughputCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToMultiExcludeThroughputTimeline(self, multiExclude, annotationText):
        collection = self.getMultiExcludeThroughputCollection()
        return Annotations().addAnnotationToTimeline(collection, multiExclude, annotationText)


    def getDistinctTechNamesForEvents(self, eventNames):
        collection = self.getMultiExcludeThroughputCollection()
        return TechAndEventNames().getDistinctTechNamesForEvents(collection, eventNames)

    def getDistinctEventNames(self):
        collection = self.getMultiExcludeThroughputCollection()
        return TechAndEventNames().getDistinctEventNames(collection)

    def getDistinctTechAndEventNames(self):
        collection = self.getMultiExcludeThroughputCollection()
        return TechAndEventNames().getDistinctTechAndEventNames(collection)
