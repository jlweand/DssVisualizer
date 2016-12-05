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
from plugins.datasource.mongodb.selecting import Selecting
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
        findJson = Selecting().getSelectJsonQuery(startDate, endDate, techName, eventName, eventTechList, False, True)
        cursor = collection.find(findJson)
        return Selecting().formatOutput(cursor)

    # select single data point
    def selectMultiExcludeThroughputDataById(self, dataId):
        collection = self.getMultiExcludeThroughputCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return Selecting().formatOutput(cursor)

    # add or edits a fixedData record to this data point
    def modifyFixedMultiExcludeThroughputData(self, dataId, traffic_xy_id, className, x, y, isDeleted):
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

    # Add or edit an annotation to the object.  This will add a single 'annotation' attribute to the object.
    def modifyAnnotationMultiExcludeThroughput(self, dataId, annotationText):
        collection = self.getMultiExcludeThroughputCollection()
        return Annotations().modifyAnnotation(collection, dataId, annotationText)

    # add an annotation to an array of annotations for the dataId
    def addAnnotationToArrayMultiExcludeThroughput(self, dataId, annotationText):
        collection = self.getMultiExcludeThroughputCollection()
        return Annotations().addAnnotationToArray(collection, dataId, annotationText)

    # edit an annotation in the array of annotations.
    def editAnnotationInArrayMultiExcludeThroughput(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getMultiExcludeThroughputCollection()
        return Annotations().editAnnotationInArray(collection, dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation from array for the dataId
    def deleteAnnotationFromArrayMultiExcludeThroughput(self, dataId, annotationText):
        collection = self.getMultiExcludeThroughputCollection()
        return Annotations().deleteAnnotationFromArray(collection, dataId, annotationText)

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
