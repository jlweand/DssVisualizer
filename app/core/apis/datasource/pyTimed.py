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

from core.config.configReader import ConfigReader
from core.apis.datasource.common import Common

class PyTimed:
    """PyTimed API.  Most of these methods must be overwritten in your plugin.
    Datasource plugin must have a file named pyTimed.py with a class name of PyTimed
    """

    def getPlugin(self):
        """Internal method to get an instance of the active plugin"""
        return ConfigReader().getInstanceOfDatasourcePlugin("PyTimed")

    def importTimed(self, jsonData):
        """Override: Imports all records from a JSON file. Dates are in UTC time.

        :param jsonData: The JSON data with the metadata added.
        :type jsonData: Parsed JSON
        :return: number of records inserted
        """
        pyTimed = self.getPlugin()
        insertedCount = pyTimed.importTimed(jsonData)
        return insertedCount

    def selectTimedData(self, startDate, endDate, techNames, eventNames, eventTechList):
        """Override: Select the timed data by start and end date. The input here will be strings, datetimes will be passed to the plugin.

        :param startDate: The a string value of the local datetime to begin search on
        :type startDate: str
        :param endDate: The a string value of the local datetime to end search on
        :type endDate: str
        :param techNames: A list of technician names to return data
        :type techNames: list
        :param eventNames: A list of event names to return data
        :type eventNames: list
        :param eventTechList: A list of a combination of event and tech names to return data
        :type eventTechList: list
        :returns: JSON object
        """
        pyTimed = self.getPlugin()
        jsonData = pyTimed.selectTimedData(Common().formatDateStringToUTC(startDate), Common().formatDateStringToUTC(endDate), techNames, eventNames, eventTechList)
        return Common().removeDeletedData(jsonData)

    def selectTimedDataById(self, dataId):
        """Override: Select the Timed data by its ID

        :param dataId: The ID of the Data point
        :type dataId: str
        :returns: JSON object
        """
        pyTimed = self.getPlugin()
        jsonData = pyTimed.selectTimedDataById(dataId)
        return jsonData

    def modifyFixedTimedData(self, dataId, timed_id, content, className, startDate, title, typeTimed, isDeleted):
        """Override: Insert Updates the record of the 'fixed' timed data.

        :param dataId: The ID of the 'fixed' timed data to edit.
        :type dataId: str
        :param timed_id: The key of the original timed data
        :type timed_id: str
        :param content: The updated content
        :type content: str
        :param typeTimed: The updated type
        :type typeTimed: str
        :param className: The updated class name
        :type className: str
        :param title: The updated title
        :type title: str
        :param startDate: The string value of the updated datetime of the event, datetime UTC will be passed to the plugin.
        :type startDate: str
        :param isDeleted: indicator if this data point should never be shown on the screen
        :type isDeleted: bool
        :returns: The modified count.
        """
        pyTimed = self.getPlugin()
        result = pyTimed.modifyFixedTimedData(dataId, timed_id, content, className, Common().formatDateStringToUTC(startDate), title, typeTimed, isDeleted)
        return result

    def deleteFixedTimedData(self, dataId):
        """Override: Delete a 'fixed' timed data.

        :param dataId: The ID of the 'fixed' data to delete
        :type dataId: str
        :returns: The deleted count.
        """
        pyTimed = self.getPlugin()
        result = pyTimed.deleteFixedTimedData(dataId)
        return result

    def modifyAnnotationTimed(self, dataId, annotationText):
        """Override: Add or edit an annotation to the object.  This will add a single 'annotation' attribute
        to the object.

        :param dataId: The ID of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The annotation text
        :type annotationText: str
        :returns: The modified count.
        """
        pyTimed = self.getPlugin()
        return pyTimed.modifyAnnotationTimed(dataId, annotationText)

    def addAnnotationToArrayTimed(self, dataId, annotationText):
        """Override: Add an annotation as an array of annotations to the object.

        :param dataId: The ID of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The annotation text
        :type annotationText: str
        :returns: The modified count.
        """
        pyTimed = self.getPlugin()
        return pyTimed.addAnnotationToArrayTimed(dataId, annotationText)

    def editAnnotationInArrayTimed(self, dataId, oldAnnotationText, newAnnotationText):
        """Override: Edit an annotation in the array of annotations.

        :param dataId: The ID of the data to edit the annotation of.
        :type dataId: str
        :param oldAnnotationText: The old annotation text
        :type oldAnnotationText: str
        :param newAnnotationText: The new annotation text
        :type newAnnotationText: str
        :returns: The modified count.
        """
        pyTimed = self.getPlugin()
        return pyTimed.editAnnotationInArrayTimed(dataId, oldAnnotationText, newAnnotationText)

    def deleteAnnotationFromArrayTimed(self, dataId, annotationText):
        """Override: Delete one annotation from the array of annotations.

        :param dataId: The ID of the data to remove the annotation from.
        :type dataId: str
        :param annotationText: The annotation text to remove.
        :type annotationText: str
        :returns: The modified count.
        """
        pyTimed = self.getPlugin()
        return pyTimed.deleteAnnotationFromArrayTimed(dataId, annotationText)

    def deleteAllAnnotationsForTimed(self, dataId):
        """Override: Delete all annotations from the ManualScreenShot object.  It should delete all annotations
        that are in an 'annotations' array as well as the 'annotation' attribute.

        :param dataId: The ID of the data to remove all annotations from.
        :type dataId: str
        :returns: The modified count.
        """
        pyTimed = self.getPlugin()
        return pyTimed.deleteAllAnnotationsForTimed(dataId)

    def addAnnotationToTimedTimeline(self, startTime, annotationText, techName, eventName):
        """Override: Adds an annotation to the timeline (not a data point). The annotation becomes a
        brand new data point.

        :param startTime: The datetime string in local time to add the annotation to.  Will be converted to UTC before passing on to plugin
        :type startTime: str
        :param annotationText: The annotation text to add.
        :type annotationText: str
        :param techName: The technician name to add to the metadata
        :type techName: str
        :param eventName: The name of the event to add to the metadata
        :type eventName: str
        :returns: The modified count.
         """

        pyTimed = self.getPlugin()
        metadata = Common().createMetadataForTimelineAnnotations(techName, eventName)

        timed = {}
        timed["className"] = "annotation"
        timed["content"] = ""
        timed["type"] = ""
        timed["title"] = ""
        timed["start"] = Common().formatDateStringToUTC(startTime)
        timed["metadata"] = metadata

        return pyTimed.addAnnotationToTimedTimeline(timed, annotationText)
