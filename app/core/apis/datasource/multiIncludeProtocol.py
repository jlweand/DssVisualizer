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

    def modifyFixedMultiIncludeProtocolData(self, dataId, oldDataId, content, className, title, startDate, isDeleted):
        """Override: Inserts or Updates the fixedData attribute.

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
        multiIncludePlugin = self.getPlugin()
        result = multiIncludePlugin.modifyFixedMultiIncludeProtocolData(dataId, oldDataId, content, className, title,
                                                                        Common().formatDateStringToUTC(startDate), isDeleted)
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

    def modifyAnnotationMultiIncludeProtocol(self, dataId, annotationText):
        """Override: Add or edit an annotation to the object.  This will add a single 'annotation' attribute
        to the object.

        :param dataId: The ID of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The annotation text
        :type annotationText: str
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        return multiIncludePlugin.modifyAnnotationMultiIncludeProtocol(dataId, annotationText)

    def addAnnotationToArrayMultiIncludeProtocol(self, dataId, annotationText):
        """Override: Add an annotation as an array of annotations to the object.

        :param dataId: The ID of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The annotation text
        :type annotationText: str
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        return multiIncludePlugin.addAnnotationToArrayMultiIncludeProtocol(dataId, annotationText)

    def editAnnotationInArrayMultiIncludeProtocol(self, dataId, oldAnnotationText, newAnnotationText):
        """Override: Edit an annotation in the array of annotations.

        :param dataId: The ID of the data to edit the annotation of.
        :type dataId: str
        :param oldAnnotationText: The old annotation text
        :type oldAnnotationText: str
        :param newAnnotationText: The new annotation text
        :type newAnnotationText: str
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        return multiIncludePlugin.editAnnotationInArrayMultiIncludeProtocol(dataId, oldAnnotationText, newAnnotationText)

    def deleteAnnotationFromArrayMultiIncludeProtocol(self, dataId, annotationText):
        """Override: Delete one annotation from the array of annotations.

        :param dataId: The ID of the data to remove the annotation from.
        :type dataId: str
        :param annotationText: The annotation text to remove.
        :type annotationText: str
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        return multiIncludePlugin.deleteAnnotationFromArrayMultiIncludeProtocol(dataId, annotationText)

    def deleteAllAnnotationsForMultiIncludeProtocol(self, dataId):
        """Override: Delete all annotations from the ManualScreenShot object.  It should delete all annotations
        that are in an 'annotations' array as well as the 'annotation' attribute.

        :param dataId: The ID of the data to remove all annotations from.
        :type dataId: str
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        return multiIncludePlugin.deleteAllAnnotationsForMultiIncludeProtocol(dataId)

    def addAnnotationToMultiIncludeProtocolTimeline(self, startTime, annotationText, techName, eventName):
        """Override: Adds an annotation to the timeline (not a data point). The annotation becomes a
        brand new data point.

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
