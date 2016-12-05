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


class TsharkProtocol:
    def getTsharkProtocolCollection(self):
        return Common().getDatabase().tsharkProtocol

    def importTsharkProtocolData(self, json):
        collection = self.getTsharkProtocolCollection()
        result = collection.insert_many(json)
        Common().addIndex(collection, True)
        return len(result.inserted_ids)

    # select data by date range of the 'start' column
    def selectTsharkProtocolData(self, startDate, endDate, techName, eventName, eventTechList):
        collection = self.getTsharkProtocolCollection()
        findJson = Common().getSelectJsonQuery(startDate, endDate, techName, eventName, eventTechList, True, False)
        cursor = collection.find(findJson)
        return Common().formatOutput(cursor)

    # select single data point
    def selectTsharkProtocolDataById(self, dataId):
        collection = self.getTsharkProtocolCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return Common().formatOutput(cursor)

    # add or edits a fixedData record to this data point
    def modifyFixedTsharkProtocolData(self, dataId, traffic_all_id, content, className, title, startDate, isDeleted):
        collection = self.getTsharkProtocolCollection()
        updateId = {"_id": ObjectId(dataId)}
        updateText = {"$set": {
            "fixedData": {"traffic_all_id": traffic_all_id, "content": content, "className": className, "title": title,
                          "start": startDate, "isDeleted": isDeleted}}}
        result = collection.update_one(updateId, updateText)
        return result.modified_count

    # delete the fixedData
    def deleteFixedTsharkProtocolData(self, dataId):
        collection = self.getTsharkProtocolCollection()
        deleteId = {"_id": ObjectId(dataId)}
        deleteText = {"$unset": {"fixedData": ""}}
        result = collection.update_one(deleteId, deleteText)
        return result.modified_count

    # Add or edit an annotation to the object.  This will add a single 'annotation' attribute to the object.
    def modifyAnnotationTsharkProtocol(self, dataId, annotationText):
        collection = self.getTsharkProtocolCollection()
        return Annotations().modifyAnnotation(collection, dataId, annotationText)

    # add an annotation to an array of annotations for the dataId
    def addAnnotationToArrayTsharkProtocol(self, dataId, annotationText):
        collection = self.getTsharkProtocolCollection()
        return Annotations().addAnnotationToArray(collection, dataId, annotationText)

    # edit an annotation in the array of annotations.
    def editAnnotationInArrayTsharkProtocol(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getTsharkProtocolCollection()
        return Annotations().editAnnotationInArray(collection, dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation from array for the dataId
    def deleteAnnotationFromArrayTsharkProtocol(self, dataId, annotationText):
        collection = self.getTsharkProtocolCollection()
        return Annotations().deleteAnnotationFromArray(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForTsharkProtocol(self, dataId):
        collection = self.getTsharkProtocolCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToTsharkProtocolTimeline(self, tshark, annotationText):
        collection = self.getTsharkProtocolCollection()
        return Annotations().addAnnotationToTimeline(collection, tshark, annotationText)
