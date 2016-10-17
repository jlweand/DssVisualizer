from core.config.configReader import ConfigReader


class MultiIncludeProtocol:
    """MultiIncludeProtocol API.  Most of these methods must be overwritten in your plugin.
    Datasource plugin must have a file named multiIncludeProtocol.py with a class name of MultiIncludeProtocol
    """


    def getPlugin(self):
        """Internal method to get an instance of the active plugin"""
        return ConfigReader().getInstanceOfDatasourcePlugin("MultiIncludeProtocol")


    def selectMultiIncludeProtocolData(self, startDate, endDate):
        """Override: Select the data by start and end date.

        :param startDate: The datetime to return data
        :type startDate: datetime
        :param endDate: The datatime to return data
        :type endDate: datetime
        :returns: JSON object
        """
        multiIncludePlugin = self.getPlugin()
        jsonData = multiIncludePlugin.selectMultiIncludeProtocolData(startDate, endDate)
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


    def insertFixedMultiIncludeProtocolData(self, dataId, oldDataId, content, className, title, start):
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
        result = multiIncludePlugin.insertFixedMultiIncludeProtocolData(dataId, oldDataId, content, className, title, start)
        return result


    def updateFixedMultiIncludeProtocolData(self, dataId, oldDataId, content, className, title, start):
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
        result = multiIncludePlugin.updateFixedMultiIncludeProtocolData(dataId, oldDataId, content, className, title, start)
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
    def addAnnotationToMultiIncludeProtocolTimeline(self, startTime, annotationText):
        """Override: Ands an annotation to the timeline (not a data point)

        :param startTime: The datetime to add the annotation to
        :type startTime: datetime
        :param annotationText: The annotation text to add.
        :type annotationText: str
        :returns: The modified count.
         """

        multiIncludePlugin = self.getPlugin()
        return multiIncludePlugin.addAnnotationToMultiIncludeProtocolTimeline(startTime, annotationText)
