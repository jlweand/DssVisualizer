from core.config.configReader import ConfigReader


class MultiIncludeThroughput:
    """MultiIncludeThroughput API.  Most of these methods must be overwritten in your plugin.
    Datasource plugin must have a file named multiIncludeThroughput.py with a class name of MultiIncludeThroughput
    """


    def getPlugin(self):
        """Internal method to get an instance of the active plugin"""
        return ConfigReader().getInstanceOfDatasourcePlugin("MultiIncludeThroughput")


    def selectMultiIncludeThroughputData(self, startDate, endDate):
        """Override: Select the timed data by start and end date.

        :param startDate: The datetime to return data
        :type startDate: datetime
        :param endDate: The datatime to return data
        :type endDate: datetime
        :returns: JSON object
        """
        multiIncludePlugin = self.getPlugin()
        jsonData = multiIncludePlugin.selectMultiIncludeThroughputData(startDate, endDate)
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
        :param x: x is the Datetime
        :type x: datetime
        :param y: The number of protocols being used
        :type y: str
        :returns: The modified count.
        """
        multiIncludePlugin = self.getPlugin()
        result = multiIncludePlugin.insertFixedMultiIncludeThroughputData(dataId, x, y)
        return result


    def updateFixedMultiIncludeThroughputData(self, dataId, x, y):
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
        result = multiIncludePlugin.updateFixedMultiIncludeThroughputData(dataId, x, y)
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
    def addAnnotationToMultiIncludeThroughputTimeline(self, startTime, annotationText):
        """Override: Ands an annotation to the timeline (not a data point)

        :param startTime: The datetime to add the annotation to
        :type startTime: datetime
        :param annotationText: The annotation text to add.
        :type annotationText: str
        :returns: The modified count.
         """

        multiIncludePlugin = self.getPlugin()
        return multiIncludePlugin.addAnnotationToMultiIncludeThroughputTimeline(startTime, annotationText)
