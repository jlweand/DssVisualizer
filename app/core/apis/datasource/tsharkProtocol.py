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

    def selectTsharkProtocolData(self, startDate, endDate, techName, eventName):
        """Override: Select the data by start and end date.

        :param startDate: The datetime to return data
        :type startDate: datetime
        :param endDate: The datatime to return data
        :type endDate: datetime
        :param techName: The technician name to return data
        :type: str
        :param: eventName: The name of the event to return data
        :type: str
        :returns: JSON object
        """
        tsharkProtocolPlugin = self.getPlugin()
        jsonData = tsharkProtocolPlugin.selectTsharkProtocolData(Common().formatDateStringToUTC(startDate),
                                                                 Common().formatDateStringToUTC(endDate), techName,
                                                                 eventName)
        return jsonData

    def selectTsharkProtocolDataById(self, dataId):
        """Override: Select the TsharkProtocol data by its ID

        :param dataId: The ID of the Data point
        :type dataId: str
        :returns: JSON object
        """
        tsharkProtocolPlugin = self.getPlugin()
        jsonData = tsharkProtocolPlugin.selectTsharkProtocolDataById(dataId)
        return jsonData

    def insertFixedTsharkProtocolData(self, dataId, oldDataId, content, className, title, startDate):
        """Override: Inserts a fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :param x: x is the Datetime
        :type x: datetime
        :param y: The number of protocols being used
        :type y: str
        :returns: The modified count.
        """
        tsharkProtocolPlugin = self.getPlugin()
        result = tsharkProtocolPlugin.insertFixedTsharkProtocolData(dataId, oldDataId, content, className, title,
                                                                    Common().formatDateStringToUTC(startDate))
        return result

    def updateFixedTsharkProtocolData(self, dataId, oldDataId, content, className, title, startDate):
        """Override: Updates the fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :param x: x is the Datetime
        :type x: datetime
        :param y: The number of protocols being used
        :type y: str
        :returns: The modified count.
        """
        tsharkProtocolPlugin = self.getPlugin()
        result = tsharkProtocolPlugin.updateFixedTsharkProtocolData(dataId, oldDataId, content, className, title,
                                                                    Common().formatDateStringToUTC(startDate))
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
    def addAnnotationToTsharkProtocolTimeline(self, startTime, annotationText):
        """Override: Ands an annotation to the timeline (not a data point)

        :param startTime: The datetime to add the annotation to
        :type startTime: datetime
        :param annotationText: The annotation text to add.
        :type annotationText: str
        :returns: The modified count.
         """

        tsharkPlugin = self.getPlugin()
        return tsharkPlugin.addAnnotationToTsharkProtocolTimeline(Common().formatDateStringToUTC(startTime),
                                                                  annotationText)
