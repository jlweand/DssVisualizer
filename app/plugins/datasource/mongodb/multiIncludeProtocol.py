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


class MultiIncludeProtocol:
    def getMultiIncludeProtocolCollection(self):
        return Common().getDatabase().multiIncludeProtocol

    def importMultiIncludeProtocolData(self, json):
        collection = self.getMultiIncludeProtocolCollection()
        result = collection.insert_many(json)
        Common().addIndex(collection, True)
        return len(result.inserted_ids)

    # select data by date range of the 'start' column
    def selectMultiIncludeProtocolData(self, startDate, endDate, techName, eventName):
        collection = self.getMultiIncludeProtocolCollection()
        findJson = Common().updateTechAndEventNames(startDate, endDate, techName, eventName, True, False)
        cursor = collection.find(findJson)
        return self.fixTheData(cursor)

    # select single data point
    def selectMultiIncludeProtocolDataById(self, dataId):
        collection = self.getMultiIncludeProtocolCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return self.fixTheData(cursor)

    # add a fixedData record to this data point
    def insertFixedMultiIncludeProtocolData(self, dataId, traffic_all_id, content, className, title, startDate):
        collection = self.getMultiIncludeProtocolCollection()
        insertId = {"_id": ObjectId(dataId)}
        insertText = {"$set": {
            "fixedData": {"traffic_all_id": traffic_all_id, "content": content, "className": className, "title": title,
                          "start": startDate}}}
        result = collection.update_one(insertId, insertText)
        return result.modified_count

    # update a previously 'fixed' record.
    def updateFixedMultiIncludeProtocolData(self, dataId, traffic_all_id, content, className, title, startDate):
        collection = self.getMultiIncludeProtocolCollection()
        updateId = {"_id": ObjectId(dataId)}
        updateText = {"$set": {
            "fixedData": {"traffic_all_id": traffic_all_id, "content": content, "className": className, "title": title,
                          "start": startDate}}}
        result = collection.update_one(updateId, updateText)
        return result.modified_count

    # delete the fixedData
    def deleteFixedMultiIncludeProtocolData(self, dataId):
        collection = self.getMultiIncludeProtocolCollection()
        deleteId = {"_id": ObjectId(dataId)}
        deleteText = {"$unset": {"fixedData": ""}}
        result = collection.update_one(deleteId, deleteText)
        return result.modified_count

    # add an annotation for the dataId
    def addAnnotationMultiIncludeProtocol(self, dataId, annotationText):
        collection = self.getMultiIncludeProtocolCollection()
        return Annotations().addAnnotation(collection, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationMultiIncludeProtocol(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getMultiIncludeProtocolCollection()
        return Annotations().editAnnotation(collection, dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation for the dataId
    def deleteAnnotationMultiIncludeProtocol(self, dataId, annotationText):
        collection = self.getMultiIncludeProtocolCollection()
        return Annotations().deleteAnnotation(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForMultiIncludeProtocol(self, dataId):
        collection = self.getMultiIncludeProtocolCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToMultiIncludeProtocolTimeline(self, startTime, annotationText):
        collection = self.getMultiIncludeProtocolCollection()
        metadata = Common().createMetadataForTimelineAnnotations()

        multiInclude = {}
        multiInclude["className"] = ""
        multiInclude["content"] = ""
        multiInclude["type"] = ""
        multiInclude["title"] = ""
        multiInclude["start"] = startTime
        multiInclude["metadata"] = metadata

        return Annotations().addAnnotationToTimeline(collection, multiInclude, annotationText)

    def fixTheData(self, cursor):
        objects = Common().formatOutput(cursor)
        for obj in objects:
            obj["id"] = obj["_id"]["$oid"]
            obj["start"] = Common().formatEpochDatetime(obj["start"]["$date"])
            obj["metadata"]["importDate"] = Common().formatEpochDatetime(obj["metadata"]["importDate"]["$date"])

        return objects
