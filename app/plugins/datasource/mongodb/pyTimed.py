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


class PyTimed:
    def getTimedCollection(self):
        return Common().getDatabase().timed

    def importTimed(self, json):
        collection = self.getTimedCollection()
        result = collection.insert_many(json)
        Common().addIndex(collection, True)
        return len(result.inserted_ids)

    # select data by date range of the 'start' column
    def selectTimedData(self, startDate, endDate, techName, eventName):
        collection = self.getTimedCollection()
        findJson = Common().updateTechAndEventNames(startDate, endDate, techName, eventName, True, False)
        cursor = collection.find(findJson)
        return Common().formatOutput(cursor)

    # select single data point
    def selectTimedDataById(self, dataId):
        collection = self.getTimedCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return Common().formatOutput(cursor)

    # add a fixedData record to this data point
    def insertFixedTimedData(self, dataId, timed_id, content, className, start, title, typeTimed):
        collection = self.getTimedCollection()
        insertId = {"_id": ObjectId(dataId)}
        push = {"$set": {"fixedData": {"timed_id": timed_id, "content": content, "className": className, "start": start,
                                       "title": title, "type": typeTimed}}}
        result = collection.update_one(insertId, push)
        return result.modified_count

    # update a previously 'fixed' record.
    def updateFixedTimedData(self, dataId, timed_id, content, className, start, title, typeTimed):
        collection = self.getTimedCollection()
        updateId = {"_id": ObjectId(dataId)}
        push = {"$set": {"fixedData": {"timed_id": timed_id, "content": content, "className": className, "start": start,
                                       "title": title, "type": typeTimed}}}
        result = collection.update_one(updateId, push)
        return result.modified_count

    # delete the fixedData
    def deleteFixedTimedData(self, dataId):
        collection = self.getTimedCollection()
        deleteId = {"_id": ObjectId(dataId)}
        push = {"$unset": {"fixedData": ""}}
        result = collection.update_one(deleteId, push)
        return result.modified_count

    # add an annotation for the dataId
    def addAnnotationTimed(self, dataId, annotationText):
        collection = self.getTimedCollection()
        return Annotations().addAnnotation(collection, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationTimed(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getTimedCollection()
        return Annotations().editAnnotation(collection, dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation for the dataId
    def deleteAnnotationTimed(self, dataId, annotationText):
        collection = self.getTimedCollection()
        return Annotations().deleteAnnotation(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForTimed(self, dataId):
        collection = self.getTimedCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToTimedTimeline(self, startTime, annotationText, techName, eventName):
        collection = self.getTimedCollection()
        metadata = Common().createMetadataForTimelineAnnotations(techName, eventName)

        timed = {}
        timed["className"] = ""
        timed["content"] = ""
        timed["type"] = ""
        timed["title"] = ""
        timed["start"] = startTime
        timed["metadata"] = metadata

        return Annotations().addAnnotationToTimeline(collection, timed, annotationText)
