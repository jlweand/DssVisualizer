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

class PyClick:
    def getClickCollection(self):
        return Common().getDatabase().click

    def importClick(self, json):
        collection = self.getClickCollection()
        result = collection.insert_many(json)
        Common().addIndex(collection, True)
        return len(result.inserted_ids)

    # select data by date range of the 'start' column
    def selectClickData(self, startDate, endDate, techName, eventName, eventTechList):
        collection = self.getClickCollection()
        findJson = Selecting().getSelectJsonQuery(startDate, endDate, techName, eventName, eventTechList, True, False)
        cursor = collection.find(findJson)
        return Selecting().formatOutput(cursor)

    # select single data point
    def selectClickDataById(self, dataId):
        collection = self.getClickCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return Selecting().formatOutput(cursor)

    # add or edits a fixedData record to this data point
    def modifyFixedClickData(self, dataId, clicks_id, content, className, start, title, typeClick, isDeleted):
        collection = self.getClickCollection()
        updateId = {"_id": ObjectId(dataId)}
        push = {"$set": {
            "fixedData": {"clicks_id": clicks_id, "content": content, "className": className, "start": start,
                          "title": title, "type": typeClick, "isDeleted": isDeleted}}}
        result = collection.update_one(updateId, push)
        return result.modified_count

    # delete the fixedData
    def deleteFixedClickData(self, dataId):
        collection = self.getClickCollection()
        deleteId = {"_id": ObjectId(dataId)}
        push = {"$unset": {"fixedData": ""}}
        result = collection.update_one(deleteId, push)
        return result.modified_count

    # Add or edit an annotation to the object.  This will add a single 'annotation' attribute to the object.
    def modifyAnnotationClick(self, dataId, annotationText):
        collection = self.getClickCollection()
        return Annotations().modifyAnnotation(collection, dataId, annotationText)

    # add an annotation to an array of annotations for the dataId
    def addAnnotationToArrayClick(self, dataId, annotationText):
        collection = self.getClickCollection()
        return Annotations().addAnnotationToArray(collection, dataId, annotationText)

    # edit an annotation in the array of annotations.
    def editAnnotationInArrayClick(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getClickCollection()
        return Annotations().editAnnotationInArray(collection, dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation from array for the dataId
    def deleteAnnotationFromArrayClick(self, dataId, annotationText):
        collection = self.getClickCollection()
        return Annotations().deleteAnnotationFromArray(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForClick(self, dataId):
        collection = self.getClickCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToClickTimeline(self, click, annotationText):
        collection = self.getClickCollection()
        return Annotations().addAnnotationToTimeline(collection, click, annotationText)
