import ujson
from datetime import datetime
from core.apis.datasource.dataImport import DataImport

class DataImportConfig:

    def __init__(self):
        self.dateformat = '%Y-%m-%d %H:%M:%S'
        self.keypressFile = "json/keypressData.json"
        self.clickFile = "json/click.json"
        self.timedFile = "json/timed.json"
        self.tsharkThroughputFile = "json/tshark/networkDataXY.json"


    def addExtraData(self, json, techName, eventName, comments, importDate, hasStartDate, hasEndDate, hasXdate):
        for data in json:
            #create the metadata
            metadata = {}
            metadata["techName"] = techName
            metadata["eventName"] = eventName
            metadata["comments"] = comments
            metadata["importDate"] = importDate
            data["metadata"] = metadata

            if (hasStartDate):
                data["start"] = datetime.strptime(data["start"], self.dateformat)

            if (hasEndDate):
                data["end"] = datetime.strptime(data["end"], self.dateformat)

            if (hasXdate):
                data["x"] = datetime.strptime(data["x"], self.dateformat)

        return json

    def importJson(self, fileName):
        with open(fileName, 'r') as jsonFile:
            jsonStr = jsonFile.read()
            data = ujson.loads(jsonStr)
        return data

    def importKeypressData(self, techName, eventName, comments, importDate):
        data = self.importJson(self.keypressFile)
        data = self.addExtraData(data, techName, eventName, comments, importDate, True, False, False)
        return DataImport().importKeypressData(data)

    def importClick(self, techName, eventName, comments, importDate):
        data = self.importJson(self.clickFile)
        data = self.addExtraData(data, techName, eventName, comments, importDate, True, True, False)
        return DataImport().importClick(data)

    def importTimed(self, techName, eventName, comments, importDate):
        data = self.importJson(self.timedFile)
        data = self.addExtraData(data, techName, eventName, comments, importDate, True, True, False)
        return DataImport().importTimed(data)

    def importTsharkThroughput(self, techName, eventName, comments, importDate):
        data = self.importJson(self.tsharkThroughputFile)
        data = self.addExtraData(data, techName, eventName, comments, importDate, False, False, True)
        return DataImport().importTsharkThroughput(data)
