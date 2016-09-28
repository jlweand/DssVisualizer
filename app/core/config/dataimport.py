import ujson
from datetime import datetime
from pprint import pprint
from .configReader import ConfigReader

class DataImport:

    def __init__(self):
        self.keypressFile = "json/keypressData.json"
        self.clickFile = "json/click.json"
        self.timedFile = "json/timed.json"

    def addExtraData(self, json, techName, eventName, comments, importDate, hasEndDate):
        for data in json:
            #create the metadata
            metadata = {}
            metadata["techName"] = techName
            metadata["eventName"] = eventName
            metadata["comments"] = comments
            metadata["importDate"] = importDate
            data["metadata"] = metadata

            # todo get the date parsing working
            data["start"] = datetime.strptime(data["start"], '%Y-%m-%d %H:%M:%S')

            if(hasEndDate):
                data["end"] = datetime.strptime(data["end"], '%Y-%m-%d %H:%M:%S')

        return json

    def importJson(self, fileName):
        with open(fileName, 'r') as jsonFile:
            jsonStr = jsonFile.read()
            data = ujson.loads(jsonStr)
        return data


    def importKeypressData(self, techName, eventName, comments, importDate):
        # get the JSON data
        data = self.importJson(self.keypressFile)

        # add the new values to it and format dates
        data = self.addExtraData(data, techName, eventName, comments, importDate, False)

        # get the datasource plugin.
        pyKeyLogger = ConfigReader().getInstanceOfDatasourcePlugin("PyKeyLogger")

        # call the insert method.
        insertedCount = pyKeyLogger.importKeypressData(data)
        return insertedCount

    def importClick(self, techName, eventName, comments, importDate):
        data = self.importJson(self.clickFile)
        eventData = self.addExtraData(data, techName, eventName, comments, importDate, True)
        pyKeyLogger = ConfigReader().getInstanceOfDatasourcePlugin("PyKeyLogger")
        insertedCount = pyKeyLogger.importClick(eventData)
        return insertedCount

    def importTimed(self, techName, eventName, comments, importDate):
        data = self.importJson(self.timedFile)
        eventData = self.addExtraData(data, techName, eventName, comments, importDate, True)
        pyKeyLogger = ConfigReader().getInstanceOfDatasourcePlugin("PyKeyLogger")
        insertedCount = pyKeyLogger.importTimed(eventData)
        return insertedCount
