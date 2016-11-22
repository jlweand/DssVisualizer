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


class PyClick:
    """PyClick API.  Most of these methods must be overwritten in your plugin.
    Datasource plugin must have a file named pyClick.py with a class name of PyClick
    """

    def getPlugin(self):
        """Internal method to get an instance of the active plugin"""
        return ConfigReader().getInstanceOfDatasourcePlugin("PyClick")

    def importClick(self, jsonData):
        """Override: Imports all records from a JSON file. Dates are in UTC time.

        :param jsonData: The JSON data with the metadata added.
        :type jsonData: Parsed JSON
        :return: number of records inserted
        """
        pyClick = self.getPlugin()
        insertedCount = pyClick.importClick(jsonData)
        return insertedCount

    def selectClickData(self, startDate, endDate, techNames, eventNames, eventTechList):
        """Override: Select the click data by start and end date. The input here will be strings, datetimes will be passed to the plugin.

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
        pyClick = self.getPlugin()
        jsonData = pyClick.selectClickData(Common().formatDateStringToUTC(startDate),
                                           Common().formatDateStringToUTC(endDate), techNames, eventNames, eventTechList)
        return Common().removeDeletedData(jsonData)

    def selectClickDataById(self, dataId):
        """Override: Select the Click data by its ID

        :param dataId: The ID of the Data point
        :type dataId: str
        :returns: JSON object
        """
        pyClick = self.getPlugin()
        jsonData = pyClick.selectClickDataById(dataId)
        return jsonData

    def insertFixedClickData(self, dataId, clicks_id, content, className, startDate, title, typeClick, isDeleted):
        """Override: Inserts a new attribute called 'fixedData' which has all the attributes of the data. Does not overwrite the original data.

        :param dataId: The ID of the Data point
        :type dataId: str
        :param clicks_id: The key of the original click data
        :type clicks_id: str
        :param content: The updated content
        :type content: str
        :param typeClick: The updated type
        :type typeClick: str
        :param className: The updated class name
        :type className: str
        :param title: The updated title
        :type title: str
        :param startDate: The string value of the updated datetime of the event, datetime UTC will be passed to the plugin.
        :type startDate: str
        :param isDeleted: indicator if this data point should never be shown on the screen
        :type isDeleted: bool
        :returns: newly created id.
        """
        pyClick = self.getPlugin()
        result = pyClick.insertFixedClickData(dataId, clicks_id, content, className,
                                              Common().formatDateStringToUTC(startDate), title, typeClick, isDeleted)
        return result

    def updateFixedClickData(self, dataId, clicks_id, content, className, startDate, title, typeClick, isDeleted):
        """Override: Updates the record of the 'fixed' click data.

        :param dataId: The ID of the Data point
        :type dataId: str
        :param clicks_id: The key of the original click data
        :type clicks_id: str
        :param content: The updated content
        :type content: str
        :param typeClick: The updated type
        :type typeClick: str
        :param className: The updated class name
        :type className: str
        :param title: The updated title
        :type title: str
        :param startDate: The string value of the updated datetime of the event, datetime UTC will be passed to the plugin.
        :type startDate: str
        :param isDeleted: indicator if this data point should never be shown on the screen
        :type isDeleted: bool
        :returns: newly created id.
        """
        pyClick = self.getPlugin()
        result = pyClick.updateFixedClickData(dataId, clicks_id, content, className,
                                              Common().formatDateStringToUTC(startDate), title, typeClick, isDeleted)
        return result

    def deleteFixedClickData(self, dataId):
        """Override: Delete a 'fixed' click data.

        :param dataId: The ID of the 'fixed' data to delete
        :type dataId: str
        :returns: The deleted count.
        """
        pyClick = self.getPlugin()
        result = pyClick.deleteFixedClickData(dataId)
        return result

    def addAnnotationClick(self, dataId, annotationText):
        """Override: Add an annotation to the Click object.

        :param dataId: The ID of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The annotation text
        :type annotationText: str
        :returns: The modified count.
        """
        pyClick = self.getPlugin()
        return pyClick.addAnnotationClick(dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationClick(self, dataId, oldAnnotationText, newAnnotationText):
        """Override: Edit an annotation on the Click object.

        :param dataId: The ID of the data to edit the annotation of.
        :type dataId: str
        :param oldAnnotationText: The old annotation text
        :type oldAnnotationText: str
        :param newAnnotationText: The new annotation text
        :type newAnnotationText: str
        :returns: The modified count.
        """
        pyClick = self.getPlugin()
        return pyClick.editAnnotationClick(dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation for the dataId
    def deleteAnnotationClick(self, dataId, annotationText):
        """Override: Delete one annotation from the Click object.

        :param dataId: The ID of the data to remove the annotation from.
        :type dataId: str
        :param annotationText: The annotation text to remove.
        :type annotationText: str
        :returns: The modified count.
        """
        pyClick = self.getPlugin()
        return pyClick.deleteAnnotationClick(dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForClick(self, dataId):
        """Override: Delete all annotations from the Click object.

        :param dataId: The ID of the data to remove all annotations from.
        :type dataId: str
        :returns: The modified count.
        """
        pyClick = self.getPlugin()
        return pyClick.deleteAllAnnotationsForClick(dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToClickTimeline(self, startTime, annotationText, techName, eventName):
        """Override: Ands an annotation to the timeline (not a data point)

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

        pyClick = self.getPlugin()
        metadata = Common().createMetadataForTimelineAnnotations(techName, eventName)

        click = {}
        click["className"] = "annotation"
        click["content"] = ""
        click["type"] = ""
        click["title"] = ""
        click["start"] = Common().formatDateStringToUTC(startTime)
        click["metadata"] = metadata

        return pyClick.addAnnotationToClickTimeline(click, annotationText)
