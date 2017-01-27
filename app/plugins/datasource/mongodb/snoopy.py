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

class Snoopy:

    def getSnoopyCollection(self):
        return Common().getDatabase().snoopyData

    def importSnoopyData(self, json):
        collection = self.getSnoopyCollection()
        result = collection.insert_many(json)
        Common().addIndex(collection, True)
        return len(result.inserted_ids)

    # select data by date range of the 'start' column
    def selectSnoopyData(self, startDate, endDate, techName, eventName, eventTechList):
        collection = self.getSnoopyCollection()
        findJson = Selecting().getSelectJsonQuery(startDate, endDate, techName, eventName, eventTechList, True, False)
        cursor = collection.find(findJson)
        return Selecting().formatOutput(cursor)

    # select single data point
    def selectSnoopyDataById(self, dataId):
        collection = self.getSnoopyCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return Selecting().formatOutput(cursor)

    # add or edits a fixedData record to this data point
    def modifyFixedSnoopyData(self, dataId, keypress_id, content, className, start, isDeleted):
        collection = self.getSnoopyCollection()
        updateId = {"_id" : ObjectId(dataId)}
        push = { "$set": {"fixedData": {"keypress_id": keypress_id, "content": content, "className": className,"start": start, "isDeleted": isDeleted}}}
        result = collection.update_one(updateId, push)
        return result.modified_count

    # delete the fixedData
    def deleteFixedSnoopyData(self, dataId):
        collection = self.getSnoopyCollection()
        deleteId = {"_id" : ObjectId(dataId)}
        push = {"$unset": {"fixedData": ""}}
        result = collection.update_one(deleteId, push)
        return result.modified_count

    # Add or edit an annotation to the object.  This will add a single 'annotation' attribute to the object.
    def modifyAnnotationSnoopy(self, dataId, annotationText):
        collection = self.getSnoopyCollection()
        return Annotations().modifyAnnotation(collection, dataId, annotationText)

    # add an annotation to an array of annotations for the dataId
    def addAnnotationToArraySnoopy(self, dataId, annotationText):
        collection = self.getSnoopyCollection()
        return Annotations().addAnnotationToArray(collection, dataId, annotationText)

    # edit an annotation in the array of annotations.
    def editAnnotationInArraySnoopy(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getSnoopyCollection()
        return Annotations().editAnnotationInArray(collection, dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation from array for the dataId
    def deleteAnnotationFromArraySnoopy(self, dataId, annotationText):
        collection = self.getSnoopyCollection()
        return Annotations().deleteAnnotationFromArray(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForSnoopy(self, dataId):
        collection = self.getSnoopyCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToSnoopyTimeline(self, snoopy, annotationText):
        collection = self.getSnoopyCollection()
        return Annotations().addAnnotationToTimeline(collection, snoopy, annotationText)


    def getDistinctTechNamesForEvents(self, eventNames):
        collection = self.getSnoopyCollection()
        return TechAndEventNames().getDistinctTechNamesForEvents(collection, eventNames)

    def getDistinctEventNames(self):
        collection = self.getSnoopyCollection()
        return TechAndEventNames().getDistinctEventNames(collection)

    def getDistinctTechAndEventNames(self):
        collection = self.getSnoopyCollection()
        return TechAndEventNames().getDistinctTechAndEventNames(collection)
