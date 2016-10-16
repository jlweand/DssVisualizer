from core.config.configReader import ConfigReader


class MultiExcludeProtocol:
    """MultiExcludeProtocol API.  Most of these methods must be overwritten in your plugin.
    Datasource plugin must have a file named multiExcludeProtocol.py with a class name of MultiExcludeProtocol
    """


    def getPlugin(self):
        """Internal method to get an instance of the active plugin"""
        return ConfigReader().getInstanceOfDatasourcePlugin("MultiExcludeProtocol")


    def selectMultiExcludeProtocolData(self, startDate, endDate):
        """Override: Select the data by start and end date.

        :param startDate: The datetime to return data
        :type startDate: datetime
        :param endDate: The datatime to return data
        :type endDate: datetime
        :returns: JSON object
        """
        multiExcludePlugin = self.getPlugin()
        jsonData = multiExcludePlugin.selectMultiExcludeProtocolData(startDate, endDate)
        return jsonData


    def selectMultiExcludeProtocolDataById(self, dataId):
        """Override: Select the MultiExcludeProtocol data by its ID

        :param dataId: The ID of the Data point
        :type dataId: str
        :returns: JSON object
        """
        multiExcludePlugin = self.getPlugin()
        jsonData = multiExcludePlugin.selectMultiExcludeProtocolDataById(dataId)
        return jsonData


    def insertFixedMultiExcludeProtocolData(self, dataId, oldDataId, content, className, title, start):
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
        result = multiExcludePlugin.insertFixedMultiExcludeProtocolData(dataId, oldDataId, content, className, title, start)
        return result


    def updateFixedMultiExcludeProtocolData(self, dataId, oldDataId, content, className, title, start):
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
        result = multiExcludePlugin.updateFixedMultiExcludeProtocolData(dataId, oldDataId, content, className, title, start)
        return result


    def deleteFixedMultiExcludeProtocolData(self, dataId):
        """Override: Deletes the fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        result = multiExcludePlugin.deleteFixedMultiExcludeProtocolData(dataId)
        return result
