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


class TsharkProtocol:
    """TsharkProtocol API.  Most of these methods must be overwritten in your plugin.
    Datasource plugin must have a file named tsharkProtocol.py with a class name of TsharkProtocol
    """

    def getPlugin(self):
        """Internal method to get an instance of the active plugin"""
        return ConfigReader().getInstanceOfDatasourcePlugin("TsharkProtocol")

    def importTsharkProtocol(self, jsonData):
        """Override: Imports all records from a JSON file. Dates are in UTC time.

        :param jsonData: The JSON data with the metadata added.
        :type jsonData: Parsed JSON
        :return: number of records inserted
        """
        tsharkProtocol = self.getPlugin()
        insertedCount = tsharkProtocol.importTsharkProtocolData(jsonData)
        return insertedCount

    def selectTsharkProtocolData(self, startDate, endDate, techNames, eventNames, eventTechList):
        """Override: Select the data by start and end date.

        :param startDate: The datetime to return data
        :type startDate: str
        :param endDate: The datatime to return data
        :type endDate: str
        :param techNames: A list of technician names to return data
        :type techNames: list
        :param eventNames: A list of event names to return data
        :type eventNames: list
        :param eventTechList: A list of a combination of event and tech names to return data
        :type eventTechList: list
        :returns: JSON object
        """
        tsharkProtocolPlugin = self.getPlugin()
        jsonData = tsharkProtocolPlugin.selectTsharkProtocolData(Common().formatDateStringToUTC(startDate),
                                                                 Common().formatDateStringToUTC(endDate), techNames,
                                                                 eventNames, eventTechList)
        return Common().removeDeletedData(jsonData)

    def selectTsharkProtocolDataById(self, dataId):
        """Override: Select the TsharkProtocol data by its ID

        :param dataId: The ID of the Data point
        :type dataId: str
        :returns: JSON object
        """
        tsharkProtocolPlugin = self.getPlugin()
        jsonData = tsharkProtocolPlugin.selectTsharkProtocolDataById(dataId)
        return jsonData

    def insertFixedTsharkProtocolData(self, dataId, oldDataId, content, className, title, startDate, isDeleted):
        """Override: Inserts a new attribute called 'fixedData' which has all the attributes of the data. Does not overwrite the original data.

        :param dataId: The key of the original data
        :type dataId: str
        :param oldDataId: The key of the original ManualScreenShot data
        :type oldDataId: str
        :param content: The updated content
        :type content: str
        :param className: The updated class name
        :type className: str
        :param title: The updated title
        :type title: str
        :param startDate: The datetime to return data
        :type startDate: str
        :param isDeleted: indicator if this data point should never be shown on the screen
        :type isDeleted: bool
        :returns: The modified count.
        """
        tsharkProtocolPlugin = self.getPlugin()
        result = tsharkProtocolPlugin.insertFixedTsharkProtocolData(dataId, oldDataId, content, className, title,
                                                                    Common().formatDateStringToUTC(startDate), isDeleted)
        return result

    def updateFixedTsharkProtocolData(self, dataId, oldDataId, content, className, title, startDate, isDeleted):
        """Override: Updates the fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :param oldDataId: The key of the original ManualScreenShot data
        :type oldDataId: str
        :param content: The updated content
        :type content: str
        :param className: The updated class name
        :type className: str
        :param title: The updated title
        :type title: str
        :param startDate: The datetime to return data
        :type startDate: str
        :param isDeleted: indicator if this data point should never be shown on the screen
        :type isDeleted: bool
        :returns: The modified count.
        """
        tsharkProtocolPlugin = self.getPlugin()
        result = tsharkProtocolPlugin.updateFixedTsharkProtocolData(dataId, oldDataId, content, className, title,
                                                                    Common().formatDateStringToUTC(startDate), isDeleted)
        return result

    def deleteFixedTsharkProtocolData(self, dataId):
        """Override: Deletes the fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :returns: The modified count.
        """
        tsharkProtocolPlugin = self.getPlugin()
        result = tsharkProtocolPlugin.deleteFixedTsharkProtocolData(dataId)
        return result

    def addAnnotationTsharkProtocol(self, dataId, annotationText):
        """Override: Add an annotation to the TsharkProtocol object.

        :param dataId: The ID of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The annotation text
        :type annotationText: str
        :returns: The modified count.
        """
        tsharkPlugin = self.getPlugin()
        return tsharkPlugin.addAnnotationTsharkProtocol(dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationTsharkProtocol(self, dataId, oldAnnotationText, newAnnotationText):
        """Override: Edit an annotation on the TsharkProtocol object.

        :param dataId: The ID of the data to edit the annotation of.
        :type dataId: str
        :param oldAnnotationText: The old annotation text
        :type oldAnnotationText: str
        :param newAnnotationText: The new annotation text
        :type newAnnotationText: str
        :returns: The modified count.
        """
        tsharkPlugin = self.getPlugin()
        return tsharkPlugin.editAnnotationTsharkProtocol(dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation for the dataId
    def deleteAnnotationTsharkProtocol(self, dataId, annotationText):
        """Override: Delete one annotation from the TsharkProtocol object.

        :param dataId: The ID of the data to remove the annotation from.
        :type dataId: str
        :param annotationText: The annotation text to remove.
        :type annotationText: str
        :returns: The modified count.
        """
        tsharkPlugin = self.getPlugin()
        return tsharkPlugin.deleteAnnotationTsharkProtocol(dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForTsharkProtocol(self, dataId):
        """Override: Delete all annotations from the TsharkProtocol object.

        :param dataId: The ID of the data to remove all annotations from.
        :type dataId: str
        :returns: The modified count.
        """
        tsharkPlugin = self.getPlugin()
        return tsharkPlugin.deleteAllAnnotationsForTsharkProtocol(dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToTsharkProtocolTimeline(self, startTime, annotationText, techName, eventName):
        """Override: Ands an annotation to the timeline (not a data point)

        :param startTime: The datetime to add the annotation to
        :type startTime: str
        :param annotationText: The annotation text to add.
        :type annotationText: str
        :param techName: The technician name to add to the metadata
        :type techName: str
        :param eventName: The name of the event to add to the metadata
        :type eventName: str
        :returns: The modified count.
         """

        tsharkPlugin = self.getPlugin()
        metadata = Common().createMetadataForTimelineAnnotations(techName, eventName)

        tshark = {}
        tshark["className"] = "annotation"
        tshark["content"] = ""
        tshark["type"] = ""
        tshark["title"] = ""
        tshark["start"] = Common().formatDateStringToUTC(startTime)
        tshark["metadata"] = metadata

        return tsharkPlugin.addAnnotationToTsharkProtocolTimeline(tshark, annotationText)
