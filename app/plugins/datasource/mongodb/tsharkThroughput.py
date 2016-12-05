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

class TsharkThroughput:

    def getTsharkThroughputCollection(self):
        return Common().getDatabase().tsharkThroughput

    def importTsharkThroughputData(self, json):
        collection = self.getTsharkThroughputCollection()
        result = collection.insert_many(json)
        Common().addIndex(collection, False)
        return len(result.inserted_ids)

    # select data by date range of the 'start' column
    def selectTsharkThroughputData(self, startDate, endDate, techName, eventName, eventTechList):
        collection = self.getTsharkThroughputCollection()
        findJson = Common().getSelectJsonQuery(startDate, endDate, techName, eventName, eventTechList, False, True)
        cursor = collection.find(findJson)
        return Common().formatOutput(cursor)

    # select single data point
    def selectTsharkThroughputDataById(self, dataId):
        collection = self.getTsharkThroughputCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return Common().formatOutput(cursor)

    # add or edits a fixedData record to this data point
    def modifyFixedTsharkThroughputData(self, dataId, traffic_xy_id, className, x, y, isDeleted):
        collection = self.getTsharkThroughputCollection()
        updateId = {"_id": ObjectId(dataId)}
        fixedData = {"$set": {"fixedData": {"traffic_xy_id": traffic_xy_id, "className": className, "x": x, "y": y, "isDeleted": isDeleted}}}

        result = collection.update_one(updateId, fixedData)
        return result.modified_count

    # delete the fixedData
    def deleteFixedTsharkThroughputData(self, dataId):
        collection = self.getTsharkThroughputCollection()
        updateId = {"_id": ObjectId(dataId)}
        fixedData = {"$unset": {"fixedData": ""}}
        result = collection.update_one(updateId, fixedData)
        return result.modified_count

    # add an annotation for the dataId
    def addAnnotationTsharkThroughput(self, dataId, annotationText):
        collection = self.getTsharkThroughputCollection()
        return Annotations().addAnnotation(collection, dataId, annotationText)

    # add an annotation for the dataId
    def addAnnotationToArrayTsharkThroughput(self, dataId, annotationText):
        collection = self.getTsharkThroughputCollection()
        return Annotations().addAnnotationToArray(collection, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationTsharkThroughput(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getTsharkThroughputCollection()
        return Annotations().editAnnotation(collection, dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation for the dataId
    def deleteAnnotationTsharkThroughput(self, dataId, annotationText):
        collection = self.getTsharkThroughputCollection()
        return Annotations().deleteAnnotation(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForTsharkThroughput(self, dataId):
        collection = self.getTsharkThroughputCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToTsharkThroughputTimeline(self, tshark, annotationText):
        collection = self.getTsharkThroughputCollection()
        return Annotations().addAnnotationToTimeline(collection, tshark, annotationText)


    def getDistinctTechNamesForEvents(self, eventNames):
        collection = self.getTsharkThroughputCollection()
        return TechAndEventNames().getDistinctTechNamesForEvents(collection, eventNames)

    def getDistinctEventNames(self):
        collection = self.getTsharkThroughputCollection()
        return TechAndEventNames().getDistinctEventNames(collection)

    def getDistinctTechAndEventNames(self):
        collection = self.getTsharkThroughputCollection()
        return TechAndEventNames().getDistinctTechAndEventNames(collection)
