from pprint import pprint
from core.config.configReader import ConfigReader
from datetime import datetime

class PyKeyLogger:

    def getPlugin(self):
        return ConfigReader().getInstanceOfDatasourcePlugin("PyKeyLogger")

#Keypress#
    def selectKeyPressData(self, startDate, endDate):
        pyKeyLogger = getPlugin()
        jsonData = pyKeyLogger.selectKeyPressData(startDate, endDate)
        return jsonData

    def insertFixedKeyPressData(self, oldDataId, content, className, start):
        pyKeyLogger = getPlugin()
        result = pyKeyLogger.insertFixedKeyPressData(oldDataId, content, className, start)
        return result.inserted_id

    def updateFixedKeyPressData(self, dataId, content, className, start):
        pyKeyLogger = getPlugin()
        result = pyKeyLogger.updateFixedKeyPressData(dataId, content, className, start)
        return result.updated_id

    def deleteFixedKeyPressData(self, dataId):
        pyKeyLogger = getPlugin()
        result = pyKeyLogger.deleteFixedKeyPressData(dataId)
        return result.updated_id

#Click#
    def selectClickData(self, startDate, endDate):
        pyKeyLogger = getPlugin()
        jsonData = pyKeyLogger.selectClickData(startDate, endDate)
        return jsonData

    def insertFixedClickData(self, oldDataId, content, _type, classname, title, start, end):
        pyKeyLogger = getPlugin()
        result = pyKeyLogger.insertFixedClickData(oldDataId, content, _type, classname, title, start, end)
        return result.inserted_id

    def updateFixedClickData(self, dataId, content, _type, classname, title, start, end):
        pyKeyLogger = getPlugin()
        result = pyKeyLogger.updateFixedClickData(dataId, content, _type, classname, title, start, end)
        return result.updated_id

    def deleteFixedClickData(self, dataId):
        pyKeyLogger = getPlugin()
        result = pyKeyLogger.deleteFixedClickData(dataId)
        return result.updated_id

#Timed#
    def selectTimedData(self, startDate, endDate):
        pyKeyLogger = getPlugin()
        jsonData = pyKeyLogger.selectTimedData(startDate, endDate)
        return jsonData

    def insertFixedTimedData(self, oldDataId, content, _type, classname, title, start, end):
        pyKeyLogger = getPlugin()
        result = pyKeyLogger.insertFixedTimedData(oldDataId, content, _type, classname, title, start, end)
        return result.inserted_id

    def updateFixedTimedData(self, dataId, content, _type, classname, title, start, end):
        pyKeyLogger = getPlugin()
        result = pyKeyLogger.updateFixedTimedData(dataId, content, _type, classname, title, start, end)
        return result.updated_id

    def deleteFixedTimedData(self, dataId):
        pyKeyLogger = getPlugin()
        result = pyKeyLogger.deleteFixedTimedData(dataId)
        return result.updated_id
