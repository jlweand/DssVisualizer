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
