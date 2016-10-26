from core.config.configReader import ConfigReader
from core.apis.datasource.common import Common

class MultiIncludeThroughput:
    """MultiIncludeThroughput API.  Most of these methods must be overwritten in your plugin.
    Datasource plugin must have a file named multiIncludeThroughput.py with a class name of MultiIncludeThroughput
    """


    def getPlugin(self):
        """Internal method to get an instance of the active plugin"""
        return ConfigReader().getInstanceOfDatasourcePlugin("MultiIncludeThroughput")


    def selectMultiIncludeThroughputData(self, startDate, endDate, techName, eventName):
        """Override: Select the timed data by start and end date. The input here will be strings, datetimes will be passed to the plugin.

        :param startDate: The a string value of the local datetime to begin search on
        :type startDate: str
        :param endDate: The a string value of the local datetime to end search on
        :type endDate: str
        :param techName: The technician name to return data
        :type: str
        :param: eventName: The name of the event to return data
        :type: str
        :returns: JSON object
        """
        multiIncludePlugin = self.getPlugin()
        jsonData = multiIncludePlugin.selectMultiIncludeThroughputData(Common().formatDateStringToUTC(startDate), Common().formatDateStringToUTC(endDate), techName, eventName)
        return jsonData


    def selectMultiIncludeThroughputDataById(self, dataId):
        """Override: Select the MultiIncludeThroughput data by its ID

        :param dataId: The ID of the Data point
        :type dataId: str
        :returns: JSON object
        """
        multiIncludePlugin = self.getPlugin()
        jsonData = multiIncludePlugin.selectMultiIncludeThroughputDataById(dataId)
        return jsonData


    def insertFixedMultiIncludeThroughputData(self, dataId, x, y):
        """Override: Inserts a fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :param x: The string value of the updated datetime of the event, datetime UTC will be passed to the plugin.
        :type x: str
        :param y: The number of protocols being used
        :type y: int
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        result = multiIncludePlugin.insertFixedMultiIncludeThroughputData(dataId, Common().formatDateStringToUTC(x), y)
        return result


    def updateFixedMultiIncludeThroughputData(self, dataId, x, y):
        """Override: Updates the fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :param x: The string value of the updated datetime of the event, datetime UTC will be passed to the plugin.
        :type x: str
        :param y: The number of protocols being used
        :type y: int
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        result = multiIncludePlugin.updateFixedMultiIncludeThroughputData(dataId, Common().formatDateStringToUTC(x), y)
        return result


    def deleteFixedMultiIncludeThroughputData(self, dataId):
        """Override: Deletes the fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        result = multiIncludePlugin.deleteFixedMultiIncludeThroughputData(dataId)
        return result


    def addAnnotationMultiIncludeThroughput(self, dataId, annotationText):
        """Override: Add an annotation to the MultiIncludeThroughput object.

        :param dataId: The ID of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The annotation text
        :type annotationText: str
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        return multiIncludePlugin.addAnnotationMultiIncludeThroughput(dataId, annotationText)


    # edit an annotation for the dataId
    def editAnnotationMultiIncludeThroughput(self, dataId, oldAnnotationText, newAnnotationText):
        """Override: Edit an annotation on the MultiIncludeThroughput object.

        :param dataId: The ID of the data to edit the annotation of.
        :type dataId: str
        :param oldAnnotationText: The old annotation text
        :type oldAnnotationText: str
        :param newAnnotationText: The new annotation text
        :type newAnnotationText: str
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        return multiIncludePlugin.editAnnotationMultiIncludeThroughput(dataId, oldAnnotationText, newAnnotationText)


    # delete an annotation for the dataId
    def deleteAnnotationMultiIncludeThroughput(self, dataId, annotationText):
        """Override: Delete one annotation from the MultiIncludeThroughput object.

        :param dataId: The ID of the data to remove the annotation from.
        :type dataId: str
        :param annotationText: The annotation text to remove.
        :type annotationText: str
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        return multiIncludePlugin.deleteAnnotationMultiIncludeThroughput(dataId, annotationText)


    # deletes all annotations for the dataId
    def deleteAllAnnotationsForMultiIncludeThroughput(self, dataId):
        """Override: Delete all annotations from the MultiIncludeThroughput object.

        :param dataId: The ID of the data to remove all annotations from.
        :type dataId: str
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        return multiIncludePlugin.deleteAllAnnotationsForMultiIncludeThroughput(dataId)


    # add an annotation to the timeline, not a datapoint
    def addAnnotationToMultiIncludeThroughputTimeline(self, x, annotationText):
        """Override: Ands an annotation to the timeline (not a data point)

        :param x: The datetime string in local time to add the annotation to.  Will be converted to UTC before passing on to plugin
        :type x: str
        :param annotationText: The annotation text to add.
        :type annotationText: str
        :returns: The modified count.
         """

        multiIncludePlugin = self.getPlugin()
        return multiIncludePlugin.addAnnotationToMultiIncludeThroughputTimeline(Common().formatDateStringToUTC(x), annotationText)
