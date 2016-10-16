from core.config.configReader import ConfigReader


class TsharkProtocol:
    """TsharkProtocol API.  Most of these methods must be overwritten in your plugin.
    Datasource plugin must have a file named tsharkProtocol.py with a class name of TsharkProtocol
    """


    def getPlugin(self):
        """Internal method to get an instance of the active plugin"""
        return ConfigReader().getInstanceOfDatasourcePlugin("TsharkProtocol")


    def selectTsharkProtocolData(self, startDate, endDate):
        """Override: Select the data by start and end date.

        :param startDate: The datetime to return data
        :type startDate: datetime
        :param endDate: The datatime to return data
        :type endDate: datetime
        :returns: JSON object
        """
        tsharkProtocolPlugin = self.getPlugin()
        jsonData = tsharkProtocolPlugin.selectTsharkProtocolData(startDate, endDate)
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


    def insertFixedTsharkProtocolData(self, dataId, oldDataId, content, className, title, start):
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
        result = tsharkProtocolPlugin.insertFixedTsharkProtocolData(dataId, oldDataId, content, className, title, start)
        return result


    def updateFixedTsharkProtocolData(self, dataId, oldDataId, content, className, title, start):
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
        result = tsharkProtocolPlugin.updateFixedTsharkProtocolData(dataId, oldDataId, content, className, title, start)
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
