from core.config.configReader import ConfigReader

class PyKeyLogger:
    """PyKeyLogger API.  Most of these methods must be overwritten in your plugin.
        Datasource plugin must have a filenamed pyKeyLogger.py with a class name of PyKeyLogger
    """

    def getPlugin(self):
        """Internal method to get an instance of the active plugin"""
        return ConfigReader().getInstanceOfDatasourcePlugin("PyKeyLogger")

#Keypress#
    def selectKeyPressData(self, startDate, endDate):
        """Override: Select the key press data by start and end date.

        :param startDate: The datetime to return data
        :type startDate: datetime
        :param endDate: The datatime to return data
        :type endDate: datetime
        :returns: JSON object
        """
        pyKeyLogger = self.getPlugin()
        jsonData = pyKeyLogger.selectKeyPressData(startDate, endDate)
        return jsonData

    def insertFixedKeyPressData(self, oldDataId, content, className, start):
        """Override: Inserts a new record of the data. Does not overrite the original key press.

        :param oldDataId: The key of the original key press data
        :type name: str
        :param content: The updated content
        :type content: str
        :param className: The updtaed class name
        :type content: str
        :param start: The updated datetime of the event.
        :type content: datetime
        :returns: newly created id.
        """
        pyKeyLogger = self.getPlugin()
        result = pyKeyLogger.insertFixedKeyPressData(oldDataId, content, className, start)
        return result

    def updateFixedKeyPressData(self, dataId, content, className, start):
        """Override: Updates the record of the 'fixed' key press data.

        :param dataId: The ID of the 'fixed' key press data to edit.
        :type name: str
        :param content: The updated content
        :type content: str
        :param className: The updtaed class name
        :type content: str
        :param start: The updated datetime of the event.
        :type content: datetime
        :returns: The modified count.
        """
        pyKeyLogger = self.getPlugin()
        result = pyKeyLogger.updateFixedKeyPressData(dataId, content, className, start)
        return result

    def deleteFixedKeyPressData(self, dataId):
        """Override: Delete a 'fixed' key press data.

        :param dataId: The ID of the 'fixed' data to delete
        :type content: str
        :returns: The deleted count.
        """
        pyKeyLogger = self.getPlugin()
        result = pyKeyLogger.deleteFixedKeyPressData(dataId)
        return result

#Click#
    def selectClickData(self, startDate, endDate):
        """Override: Select the click data by start and end date.

        :param startDate: The datetime to return data
        :type startDate: datetime
        :param endDate: The datatime to return data
        :type endDate: datetime
        :returns: JSON object
        """
        pyKeyLogger = self.getPlugin()
        jsonData = pyKeyLogger.selectClickData(startDate, endDate)
        return jsonData

    def insertFixedClickData(self, oldDataId, content, _type, classname, title, start, end):
        """Override: Inserts a new record of the data. Does not overrite the original key press.

        :param oldDataId: The key of the original click data
        :type name: str
        :param content: The updated content
        :type content: str
        :param _type: The updtaed type
        :type content: str
        :param className: The updtaed class name
        :type content: str
        :param title: The updtaed title
        :type content: str
        :param start: The updated start datetime of the event.
        :type content: datetime
        :param end: The updated end datetime of the event.
        :type content: datetime
        :returns: newly created id.
        """
        pyKeyLogger = self.getPlugin()
        result = pyKeyLogger.insertFixedClickData(oldDataId, content, _type, classname, title, start, end)
        return result

    def updateFixedClickData(self, dataId, content, _type, classname, title, start, end):
        """Override: Updates the record of the 'fixed' click data.

        :param dataId: The ID of the 'fixed' click data to edit.
        :type name: str
        :param content: The updated content
        :type content: str
        :param _type: The updtaed type
        :type content: str
        :param className: The updtaed class name
        :type content: str
        :param title: The updtaed title
        :type content: str
        :param start: The updated start datetime of the event.
        :type content: datetime
        :param end: The updated end datetime of the event.
        :type content: datetime
        :returns: The modified count.
        """
        pyKeyLogger = self.getPlugin()
        result = pyKeyLogger.updateFixedClickData(dataId, content, _type, classname, title, start, end)
        return result

    def deleteFixedClickData(self, dataId):
        """Override: Delete a 'fixed' click data.

        :param dataId: The ID of the 'fixed' data to delete
        :type content: str
        :returns: The deleted count.
        """
        pyKeyLogger = self.getPlugin()
        result = pyKeyLogger.deleteFixedClickData(dataId)
        return result

#Timed#
    def selectTimedData(self, startDate, endDate):
        """Override: Select the timed data by start and end date.

        :param startDate: The datetime to return data
        :type startDate: datetime
        :param endDate: The datatime to return data
        :type endDate: datetime
        :returns: JSON object
        """
        pyKeyLogger = self.getPlugin()
        jsonData = pyKeyLogger.selectTimedData(startDate, endDate)
        return jsonData

    def insertFixedTimedData(self, oldDataId, content, _type, classname, title, start, end):
        """Override: Inserts a new record of the data. Does not overrite the original key press.

        :param oldDataId: The key of the original timmed data
        :type name: str
        :param content: The updated content
        :type content: str
        :param _type: The updtaed type
        :type content: str
        :param className: The updtaed class name
        :type content: str
        :param title: The updtaed title
        :type content: str
        :param start: The updated start datetime of the event.
        :type content: datetime
        :param end: The updated end datetime of the event.
        :type content: datetime
        :returns: newly created id.
        """
        pyKeyLogger = self.getPlugin()
        result = pyKeyLogger.insertFixedTimedData(oldDataId, content, _type, classname, title, start, end)
        return result

    def updateFixedTimedData(self, dataId, content, _type, classname, title, start, end):
        """Override: Updates the record of the 'fixed' timmed data.

        :param dataId: The ID of the 'fixed' timmed data to edit.
        :type name: str
        :param content: The updated content
        :type content: str
        :param _type: The updtaed type
        :type content: str
        :param className: The updtaed class name
        :type content: str
        :param title: The updtaed title
        :type content: str
        :param start: The updated start datetime of the event.
        :type content: datetime
        :param end: The updated end datetime of the event.
        :type content: datetime
        :returns: The modified count.
        """
        pyKeyLogger = self.getPlugin()
        result = pyKeyLogger.updateFixedTimedData(dataId, content, _type, classname, title, start, end)
        return result

    def deleteFixedTimedData(self, dataId):
        """Override: Delete a 'fixed' timmed data.

        :param dataId: The ID of the 'fixed' data to delete
        :type content: str
        :returns: The deleted count.
        """
        pyKeyLogger = self.getPlugin()
        result = pyKeyLogger.deleteFixedTimedData(dataId)
        return result
