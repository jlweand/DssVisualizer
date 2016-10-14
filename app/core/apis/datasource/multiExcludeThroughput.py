from core.config.configReader import ConfigReader


class MultiExcludeThroughput:
    """MultiExcludeThroughput API.  Most of these methods must be overwritten in your plugin.
    Datasource plugin must have a file named multiExcludeThroughput.py with a class name of MultiExcludeThroughput
    """


    def getPlugin(self):
        """Internal method to get an instance of the active plugin"""
        return ConfigReader().getInstanceOfDatasourcePlugin("MultiExcludeThroughput")


    def selectMultiExcludeThroughputData(self, startDate, endDate):
        """Override: Select the timed data by start and end date.

        :param startDate: The datetime to return data
        :type startDate: datetime
        :param endDate: The datatime to return data
        :type endDate: datetime
        :returns: JSON object
        """
        multiExcludePlugin = self.getPlugin()
        jsonData = multiExcludePlugin.selectMultiExcludeThroughputData(startDate, endDate)
        return jsonData


    def selectMultiExcludeThroughputDataById(self, dataId):
        """Override: Select the MultiExcludeThroughput data by its ID

        :param dataId: The ID of the Data point
        :type dataId: str
        :returns: JSON object
        """
        multiExcludePlugin = self.getPlugin()
        jsonData = multiExcludePlugin.selectMultiExcludeThroughputDataById(dataId)
        return jsonData


    def insertFixedMultiExcludeThroughputData(self, dataId, x, y):
        """Override: Inserts a fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :param x: x is the Datetime
        :type x: datetime
        :param y: The number of protocols being used
        :type y: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        result = multiExcludePlugin.insertFixedMultiExcludeThroughputData(dataId, x, y)
        return result


    def updateFixedMultiExcludeThroughputData(self, dataId, x, y):
        """Override: Updates the fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :param x: x is the Datetime
        :type x: datetime
        :param y: The number of protocols being used
        :type y: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        result = multiExcludePlugin.updateFixedMultiExcludeThroughputData(dataId, x, y)
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


    def addAnnotationMultiExcludeThroughput(self, dataId, annotationText):
        """Override: Add an annotation to the MultiExcludeThroughput object.

        :param dataId: The ID of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The annotation text
        :type annotationText: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        return multiExcludePlugin.addAnnotationMultiExcludeThroughput(dataId, annotationText)


    # edit an annotation for the dataId
    def editAnnotationMultiExcludeThroughput(self, dataId, oldAnnotationText, newAnnotationText):
        """Override: Edit an annotation on the MultiExcludeThroughput object.

        :param dataId: The ID of the data to edit the annotation of.
        :type dataId: str
        :param oldAnnotationText: The old annotation text
        :type oldAnnotationText: str
        :param newAnnotationText: The new annotation text
        :type newAnnotationText: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        return multiExcludePlugin.editAnnotationMultiExcludeThroughput(dataId, oldAnnotationText, newAnnotationText)


    # delete an annotation for the dataId
    def deleteAnnotationMultiExcludeThroughput(self, dataId, annotationText):
        """Override: Delete one annotation from the MultiExcludeThroughput object.

        :param dataId: The ID of the data to remove the annotation from.
        :type dataId: str
        :param annotationText: The annotation text to remove.
        :type annotationText: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        return multiExcludePlugin.deleteAnnotationMultiExcludeThroughput(dataId, annotationText)


    # deletes all annotations for the dataId
    def deleteAllAnnotationsForMultiExcludeThroughput(self, dataId):
        """Override: Delete all annotations from the MultiExcludeThroughput object.

        :param dataId: The ID of the data to remove all annotations from.
        :type dataId: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        return multiExcludePlugin.deleteAllAnnotationsForMultiExcludeThroughput(dataId)


    # add an annotation to the timeline, not a datapoint
    def addAnnotationToMultiExcludeThroughputTimeline(self, startTime, annotationText):
        """Override: Ands an annotation to the timeline (not a data point)

        :param startTime: The datetime to add the annotation to
        :type startTime: datetime
        :param annotationText: The annotation text to add.
        :type annotationText: str
        :returns: The modified count.
         """

        multiExcludePlugin = self.getPlugin()
        return multiExcludePlugin.addAnnotationToMultiExcludeThroughputTimeline(startTime, annotationText)
