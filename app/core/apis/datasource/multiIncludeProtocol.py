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


class MultiIncludeProtocol:
    """MultiIncludeProtocol API.  Most of these methods must be overwritten in your plugin.
    Datasource plugin must have a file named multiIncludeProtocol.py with a class name of MultiIncludeProtocol
    """

    def getPlugin(self):
        """Internal method to get an instance of the active plugin"""
        return ConfigReader().getInstanceOfDatasourcePlugin("MultiIncludeProtocol")

    def importMultiIncludeProtocol(self, jsonData):
        """Override: Imports all records from a JSON file. Dates are in UTC time.

        :param jsonData: The JSON data with the metadata added.
        :type jsonData: Parsed JSON
        :return: number of records inserted
        """
        multiIncludeProtocol = self.getPlugin()
        insertedCount = multiIncludeProtocol.importMultiIncludeProtocolData(jsonData)
        return insertedCount

    def selectMultiIncludeProtocolData(self, startDate, endDate, techNames, eventNames, eventTechList):
        """Override: Select the data by start and end date.

        :param startDate: The datetime to return data
        :type startDate: datetime
        :param endDate: The datatime to return data
        :type endDate: datetime
        :param techNames: A list of technician names to return data
        :type techNames: list
        :param eventNames: A list of event names to return data
        :type eventNames: list
        :param eventTechList: A list of a combination of event and tech names to return data
        :type eventTechList: list
        :returns: JSON object
        """
        multiIncludePlugin = self.getPlugin()
        jsonData = multiIncludePlugin.selectMultiIncludeProtocolData(Common().formatDateStringToUTC(startDate),
                                                                     Common().formatDateStringToUTC(endDate), techNames,
                                                                     eventNames, eventTechList)
        return jsonData

    def selectMultiIncludeProtocolDataById(self, dataId):
        """Override: Select the MultiIncludeProtocol data by its ID

        :param dataId: The ID of the Data point
        :type dataId: str
        :returns: JSON object
        """
        multiIncludePlugin = self.getPlugin()
        jsonData = multiIncludePlugin.selectMultiIncludeProtocolDataById(dataId)
        return jsonData

    def insertFixedMultiIncludeProtocolData(self, dataId, oldDataId, content, className, title, startDate):
        """Override: Inserts a fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :param x: x is the Datetime
        :type x: datetime
        :param y: The number of protocols being used
        :type y: str
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        result = multiIncludePlugin.insertFixedMultiIncludeProtocolData(dataId, oldDataId, content, className, title,
                                                                        Common().formatDateStringToUTC(startDate))
        return result

    def updateFixedMultiIncludeProtocolData(self, dataId, oldDataId, content, className, title, startDate):
        """Override: Updates the fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :param x: x is the Datetime
        :type x: datetime
        :param y: The number of protocols being used
        :type y: str
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        result = multiIncludePlugin.updateFixedMultiIncludeProtocolData(dataId, oldDataId, content, className, title,
                                                                        Common().formatDateStringToUTC(startDate))
        return result

    def deleteFixedMultiIncludeProtocolData(self, dataId):
        """Override: Deletes the fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        result = multiIncludePlugin.deleteFixedMultiIncludeProtocolData(dataId)
        return result

    def addAnnotationMultiIncludeProtocol(self, dataId, annotationText):
        """Override: Add an annotation to the MultiIncludeProtocol object.

        :param dataId: The ID of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The annotation text
        :type annotationText: str
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        return multiIncludePlugin.addAnnotationMultiIncludeProtocol(dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationMultiIncludeProtocol(self, dataId, oldAnnotationText, newAnnotationText):
        """Override: Edit an annotation on the MultiIncludeProtocol object.

        :param dataId: The ID of the data to edit the annotation of.
        :type dataId: str
        :param oldAnnotationText: The old annotation text
        :type oldAnnotationText: str
        :param newAnnotationText: The new annotation text
        :type newAnnotationText: str
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        return multiIncludePlugin.editAnnotationMultiIncludeProtocol(dataId, oldAnnotationText, newAnnotationText)

    # delete an annotation for the dataId
    def deleteAnnotationMultiIncludeProtocol(self, dataId, annotationText):
        """Override: Delete one annotation from the MultiIncludeProtocol object.

        :param dataId: The ID of the data to remove the annotation from.
        :type dataId: str
        :param annotationText: The annotation text to remove.
        :type annotationText: str
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        return multiIncludePlugin.deleteAnnotationMultiIncludeProtocol(dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForMultiIncludeProtocol(self, dataId):
        """Override: Delete all annotations from the MultiIncludeProtocol object.

        :param dataId: The ID of the data to remove all annotations from.
        :type dataId: str
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        return multiIncludePlugin.deleteAllAnnotationsForMultiIncludeProtocol(dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToMultiIncludeProtocolTimeline(self, startTime, annotationText, techName, eventName):
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

        multiIncludePlugin = self.getPlugin()
        metadata = Common().createMetadataForTimelineAnnotations(techName, eventName)

        multiInclude = {}
        multiInclude["className"] = "annotation"
        multiInclude["content"] = ""
        multiInclude["type"] = ""
        multiInclude["title"] = ""
        multiInclude["start"] = Common().formatDateStringToUTC(startTime)
        multiInclude["metadata"] = metadata

        return multiIncludePlugin.addAnnotationToMultiIncludeProtocolTimeline(multiInclude, annotationText)
