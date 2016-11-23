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

class ManualScreenShot:

    def getManualScreenShotCollection(self):
        return Common().getDatabase().manualScreenShot

    def importManualScreenShot(self, json):
        collection = self.getManualScreenShotCollection()
        result = collection.insert_many(json)
        Common().addIndex(collection, True)
        return len(result.inserted_ids)

    # select data by date range of the 'start' column
    def selectManualScreenShotData(self, startDate, endDate, techName, eventName, eventTechList):
        collection = self.getManualScreenShotCollection()
        findJson = Common().getSelectJsonQuery(startDate, endDate, techName, eventName, eventTechList, True, False)
        cursor = collection.find(findJson)
        return Common().formatOutput(cursor)

    # select single data point
    def selectManualScreenShotDataById(self, dataId):
        collection = self.getManualScreenShotCollection()
        cursor = collection.find({"_id": ObjectId(dataId)})
        return Common().formatOutput(cursor)

    # add a fixedData record to this data point
    def insertFixedManualScreenShotData(self, dataId, manualscreen_id, content, className, start, title, typeManualScreenShot, comment, isDeleted):
        collection = self.getManualScreenShotCollection()
        insertId = {"_id": ObjectId(dataId)}
        push = {"$set": {
            "fixedData": {"manualscreen_id": manualscreen_id, "content": content, "className": className, "start": start,
                          "title": title, "type": typeManualScreenShot, "isDeleted": isDeleted, "comment": comment}}}
        result = collection.update_one(insertId, push)
        return result.modified_count

    # update a previously 'fixed' record.
    def updateFixedManualScreenShotData(self, dataId, manualscreen_id, content, className, start, title, typeManualScreenShot, comment, isDeleted):
        collection = self.getManualScreenShotCollection()
        updateId = {"_id": ObjectId(dataId)}
        push = {"$set": {
            "fixedData": {"manualscreen_id": manualscreen_id, "content": content, "className": className, "start": start,
                          "title": title, "type": typeManualScreenShot, "isDeleted": isDeleted, "comment": comment}}}
        result = collection.update_one(updateId, push)
        return result.modified_count

    # delete the fixedData
    def deleteFixedManualScreenShotData(self, dataId):
        collection = self.getManualScreenShotCollection()
        deleteId = {"_id": ObjectId(dataId)}
        push = {"$unset": {"fixedData": ""}}
        result = collection.update_one(deleteId, push)
        return result.modified_count

    # add an annotation for the dataId
    def addAnnotationManualScreenShot(self, dataId, annotationText):
        collection = self.getManualScreenShotCollection()
        return Annotations().addAnnotation(collection, dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationManualScreenShot(self, dataId, oldAnnotationText, newAnnotationText):
        collection = self.getManualScreenShotCollection()
        return Annotations().editAnnotation(collection, dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation for the dataId
    def deleteAnnotationManualScreenShot(self, dataId, annotationText):
        collection = self.getManualScreenShotCollection()
        return Annotations().deleteAnnotation(collection, dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForManualScreenShot(self, dataId):
        collection = self.getManualScreenShotCollection()
        return Annotations().deleteAllAnnotationsForData(collection, dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToManualScreenShotTimeline(self, manualScreenShot, annotationText):
        collection = self.getManualScreenShotCollection()
        return Annotations().addAnnotationToTimeline(collection, manualScreenShot, annotationText)


    def getDistinctTechNamesForEvents(self, eventNames):
        collection = self.getManualScreenShotCollection()
        return TechAndEventNames().getDistinctTechNamesForEvents(collection, eventNames)

    def getDistinctEventNames(self):
        collection = self.getManualScreenShotCollection()
        return TechAndEventNames().getDistinctEventNames(collection)

    def getDistinctTechAndEventNames(self):
        collection = self.getManualScreenShotCollection()
        return TechAndEventNames().getDistinctTechAndEventNames(collection)
