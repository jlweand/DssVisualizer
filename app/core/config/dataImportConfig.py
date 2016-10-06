import ujson
from datetime import datetime
from core.apis.datasource.dataImport import DataImport

class DataImportConfig:

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
        data = self.importJson(self.keypressFile)
        data = self.addExtraData(data, techName, eventName, comments, importDate, False)
        return DataImport().importKeypressData(data)

    def importClick(self, techName, eventName, comments, importDate):
        data = self.importJson(self.clickFile)
        eventData = self.addExtraData(data, techName, eventName, comments, importDate, True)
        return DataImport().importClick(eventData)

    def importTimed(self, techName, eventName, comments, importDate):
        data = self.importJson(self.timedFile)
        eventData = self.addExtraData(data, techName, eventName, comments, importDate, True)
        return DataImport().importTimed(eventData)
