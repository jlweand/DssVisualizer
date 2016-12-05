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


class MultiExcludeThroughput:
    """MultiExcludeThroughput API.  Most of these methods must be overwritten in your plugin.
    Datasource plugin must have a file named multiExcludeThroughput.py with a class name of MultiExcludeThroughput
    """

    def getPlugin(self):
        """Internal method to get an instance of the active plugin"""
        return ConfigReader().getInstanceOfDatasourcePlugin("MultiExcludeThroughput")

    def importMultiExcludeThroughput(self, jsonData):
        """Override: Imports all records from a JSON file. Dates are in UTC time.

        :param jsonData: The JSON data with the metadata added.
        :type jsonData: Parsed JSON
        :return: number of records inserted
        """
        multiExcludeThroughput = self.getPlugin()
        insertedCount = multiExcludeThroughput.importMultiExcludeThroughputData(jsonData)
        return insertedCount

    def selectMultiExcludeThroughputData(self, startDate, endDate, techNames, eventNames, eventTechList):
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
        multiExcludePlugin = self.getPlugin()
        jsonData = multiExcludePlugin.selectMultiExcludeThroughputData(Common().formatDateStringToUTC(startDate),
                                                                       Common().formatDateStringToUTC(endDate),
                                                                       techNames, eventNames, eventTechList)
        return Common().removeDeletedData(jsonData)

    def selectMultiExcludeThroughputDataById(self, dataId):
        """Override: Select the MultiExcludeThroughput data by its ID

        :param dataId: The ID of the Data point
        :type dataId: str
        :returns: JSON object
        """
        multiExcludePlugin = self.getPlugin()
        jsonData = multiExcludePlugin.selectMultiExcludeThroughputDataById(dataId)
        return jsonData

    def modifyFixedMultiExcludeThroughputData(self, dataId, traffic_xy_id, className, x, y, isDeleted):
        """Override: Inserts or Updates the fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :param traffic_xy_id: the traffic_xy_id.
        :type traffic_xy_id: int
        :param className: The updated class name
        :type className: str
        :param x: The string value of the updated datetime of the event, datetime UTC will be passed to the plugin.
        :type x: str
        :param y: The number of protocols being used
        :type y: int
        :param isDeleted: indicator if this data point should never be shown on the screen
        :type isDeleted: bool
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        result = multiExcludePlugin.modifyFixedMultiExcludeThroughputData(dataId, traffic_xy_id, className, Common().formatDateStringToUTC(x), y, isDeleted)
        return result

    def deleteFixedMultiExcludeThroughputData(self, dataId):
        """Override: Deletes the fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        result = multiExcludePlugin.deleteFixedMultiExcludeThroughputData(dataId)
        return result

    def modifyAnnotationMultiExcludeThroughput(self, dataId, annotationText):
        """Override: Add or edit an annotation to the object.  This will add a single 'annotation' attribute
        to the object.

        :param dataId: The ID of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The annotation text
        :type annotationText: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        return multiExcludePlugin.modifyAnnotationMultiExcludeThroughput(dataId, annotationText)

    def addAnnotationToArrayMultiExcludeThroughput(self, dataId, annotationText):
        """Override: Add an annotation as an array of annotations to the object.

        :param dataId: The ID of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The annotation text
        :type annotationText: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        return multiExcludePlugin.addAnnotationToArrayMultiExcludeThroughput(dataId, annotationText)

    def editAnnotationInArrayMultiExcludeThroughput(self, dataId, oldAnnotationText, newAnnotationText):
        """Override: Edit an annotation in the array of annotations.

        :param dataId: The ID of the data to edit the annotation of.
        :type dataId: str
        :param oldAnnotationText: The old annotation text
        :type oldAnnotationText: str
        :param newAnnotationText: The new annotation text
        :type newAnnotationText: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        return multiExcludePlugin.editAnnotationInArrayMultiExcludeThroughput(dataId, oldAnnotationText, newAnnotationText)

    def deleteAnnotationFromArrayMultiExcludeThroughput(self, dataId, annotationText):
        """Override: Delete one annotation from the array of annotations.

        :param dataId: The ID of the data to remove the annotation from.
        :type dataId: str
        :param annotationText: The annotation text to remove.
        :type annotationText: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        return multiExcludePlugin.deleteAnnotationFromArrayMultiExcludeThroughput(dataId, annotationText)

    def deleteAllAnnotationsForMultiExcludeThroughput(self, dataId):
        """Override: Delete all annotations from the ManualScreenShot object.  It should delete all annotations
        that are in an 'annotations' array as well as the 'annotation' attribute.

        :param dataId: The ID of the data to remove all annotations from.
        :type dataId: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        return multiExcludePlugin.deleteAllAnnotationsForMultiExcludeThroughput(dataId)

    def addAnnotationToMultiExcludeThroughputTimeline(self, x, annotationText, techName, eventName):
        """Override: Adds an annotation to the timeline (not a data point). The annotation becomes a
        brand new data point.

        :param x: The datetime string in local time to add the annotation to.  Will be converted to UTC before passing on to plugin
        :type x: str
        :param annotationText: The annotation text to add.
        :type annotationText: str
        :param techName: The technician name to add to the metadata
        :type techName: str
        :param eventName: The name of the event to add to the metadata
        :type eventName: str
        :returns: The modified count.
         """

        multiExcludePlugin = self.getPlugin()
        metadata = Common().createMetadataForTimelineAnnotations(techName, eventName)

        multiExclude = {}
        multiExclude["className"] = "annotation"
        multiExclude["x"] = Common().formatDateStringToUTC(x)
        multiExclude["y"] = ""
        multiExclude["metadata"] = metadata

        return multiExcludePlugin.addAnnotationToMultiExcludeThroughputTimeline(multiExclude, annotationText)

    def getDistinctTechNames(self):
        """Override: Get a list of distinct technician names. used for the UI when searching by technician name.

        :return: a collection of distinct technician names in the data source.
        """
        return self.getPlugin().getDistinctTechName()

    def getDistinctEventNames(self):
        """Override: Get a list of distinct event names. used for the UI when searching by event name.

        :return: a collection of distinct event names in the data source.
        """
        return self.getPlugin().getDistinctEventName()
