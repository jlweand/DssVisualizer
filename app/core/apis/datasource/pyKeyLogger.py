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
        newData = {}
        newData["content"] = content
        newData["className"] = className
        newData["start"] = start
        newData["addedDate"] = datetime.datetime.now().time()

        pyKeyLogger = getPlugin()
        result = pyKeyLogger.insertFixedKeyPressData(oldDataId, newData)
        return result.inserted_id

    def updateFixedKeyPressData(self, dataId, content, className, start):
        data = {}
        data["content"] = content
        data["className"] = className
        data["start"] = start
        data["updatedDate"] = datetime.datetime.now().time()

        pyKeyLogger = getPlugin()
        result = pyKeyLogger.updateFixedKeyPressData(dataId, data)
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
        newData = {}
        newData["content"] = content
        newData["type"] = _type
        newData["classname"] = classname
        newData["title"] = title
        newData["start"] = start
        newData["end"] = end
        newData["addedDate"] = datetime.datetime.now().time()

        pyKeyLogger = getPlugin()
        result = pyKeyLogger.insertFixedClickData(oldDataId, newData)
        return result.inserted_id

    def updateFixedClickData(self, dataId, content, type, classname, title, start, end):
        data = {}
        data["content"] = content
        data["type"] = _type
        data["classname"] = classname
        data["title"] = title
        data["start"] = start
        data["end"] = end
        data["updatedDate"] = datetime.datetime.now().time()

        pyKeyLogger = getPlugin()
        result = pyKeyLogger.updateFixedClickData(dataId, data)
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

    def insertFixedTimedData(self, oldDataId, content, type, classname, title, start, end):
        newData = {}
        newData["content"] = content
        newData["type"] = _type
        newData["classname"] = classname
        newData["title"] = title
        newData["start"] = start
        newData["end"] = end
        newData["addedDate"] = datetime.datetime.now().time()

        pyKeyLogger = getPlugin()
        result = pyKeyLogger.insertFixedTimedData(oldDataId, newData)
        return result.inserted_id

    def updateFixedTimedData(self, dataId, content, type, classname, title, start, end):
        data = {}
        data["content"] = content
        data["type"] = _type
        data["classname"] = classname
        data["title"] = title
        data["start"] = start
        data["end"] = end
        data["updatedDate"] = datetime.datetime.now().time()

        pyKeyLogger = getPlugin()
        result = pyKeyLogger.updateFixedTimedData(dataId, data)
        return result.updated_id

    def deleteFixedTimedData(self, dataId):
        pyKeyLogger = getPlugin()
        result = pyKeyLogger.deleteFixedTimedData(dataId)
        return result.updated_id
