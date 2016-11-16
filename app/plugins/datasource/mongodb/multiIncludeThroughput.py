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

class MultiIncludeThroughput:

    def getMultiIncludeThroughputCollection(self):
        return Common().getDatabase().multiIncludeThroughput

    def importMultiIncludeThroughputData(self, json):
        collection = self.getMultiIncludeThroughputCollection()
        result = collection.insert_many(json)
        Common().addIndex(collection, False)
        return len(result.inserted_ids)

    # select data by date range of the 'start' column
    def selectMultiIncludeThroughputData(self, startDate, endDate, techName, eventName, eventTechList):
        collection = self.getMultiIncludeThroughputCollection()
        findJson = Common().getSelectJsonQuery(startDate, endDate, techName, eventName, eventTechList, False, True)
        cursor = collection.find(findJson)
        return Common().formatOutput(cursor)

    # select single data point
    def selectMultiIncludeThroughputDataById(self, dataId):
        collection = self.getMultiIncludeThroughputCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return Common().formatOutput(cursor)

    # add a fixedData record to this data point
    def insertFixedMultiIncludeThroughputData(self, dataId, traffic_xy_id, x, y):
        collection = self.getMultiIncludeThroughputCollection()
        updateId = {"_id": ObjectId(dataId)}
        fixedData = {"$set": {"fixedData": {"traffic_xy_id": traffic_xy_id, "x": x, "y": y}}}
        result = collection.update_one(updateId, fixedData)
        return result.modified_count

    # update a previously 'fixed' record.
    def updateFixedMultiIncludeThroughputData(self, dataId, traffic_xy_id, x, y):
        collection = self.getMultiIncludeThroughputCollection()
        updateId = {"_id" : ObjectId(dataId)}
        fixedData = {"$set": {"fixedData": {"traffic_xy_id": traffic_xy_id, "x": x, "y": y}}}

        result = collection.update_one(updateId, fixedData)
        return result.modified_count

    # delete the fixedData
    def deleteFixedMultiIncludeThroughputData(self, dataId):
        collection = self.getMultiIncludeThroughputCollection()
        updateId = {"_id" : ObjectId(dataId)}
        fixedData = {"$unset": {"fixedData": "" }}
        result = collection.update_one(updateId, fixedData)
        return result.modified_count

    # add an annotation for the dataId
    def addAnnotationMultiIncludeThroughput(self, dataId, annotationText):
        collection = self.getMultiIncludeThroughputCollection()
        return Annotations().addAnnotation(collection, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationMultiIncludeThroughput(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getMultiIncludeThroughputCollection()
        return Annotations().editAnnotation(collection, dataId, oldAnnotationText, newAnnotationText)

    #delete an annotation for the dataId
    def deleteAnnotationMultiIncludeThroughput(self, dataId, annotationText):
        collection = self.getMultiIncludeThroughputCollection()
        return Annotations().deleteAnnotation(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForMultiIncludeThroughput(self, dataId):
        collection = self.getMultiIncludeThroughputCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToMultiIncludeThroughputTimeline(self, multiInclude, annotationText):
        collection = self.getMultiIncludeThroughputCollection()
        return Annotations().addAnnotationToTimeline(collection, multiInclude, annotationText)

    def getDistinctTechNamesForEvents(self, eventNames):
        collection = self.getMultiIncludeThroughputCollection()
        return TechAndEventNames().getDistinctTechNamesForEvents(collection, eventNames)

    def getDistinctEventNames(self):
        collection = self.getMultiIncludeThroughputCollection()
        return TechAndEventNames().getDistinctEventNames(collection)

    def getDistinctTechAndEventNames(self):
        collection = self.getMultiIncludeThroughputCollection()
        return TechAndEventNames().getDistinctTechAndEventNames(collection)
