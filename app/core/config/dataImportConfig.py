import ujson
from datetime import datetime
from core.apis.datasource.dataImport import DataImport

class DataImportConfig:

    def __init__(self):
        self.dateformat = '%Y-%m-%dT%H:%M:%S'
        self.keypressFile = "json/pyKeyLogger/keypressData.json"
        self.clickFile = "json/pyKeyLogger/click.json"
        self.timedFile = "json/pyKeyLogger/timed.json"
        self.tsharkThroughputFile = "json/tshark/networkDataXY.json"
        self.multiIncludeThroughputFile = "json/multi_incl_tshark/networkDataXY.json"
        self.multiExcludeThroughputFile = "json/multi_exec_tshark/networkDataXY.json"
        self.tsharkProtocolFile = "json/tshark/networkDataAll.json"
        self.multiIncludeProtocolFile = "json/multi_incl_tshark/networkDataAll.json"
        self.multiExcludeProtocolFile = "json/multi_exec_tshark/networkDataAll.json"

    def addExtraData(self, json, techName, eventName, comments, importDate, hasStartDate, hasXdate):
        for data in json:
            #create the metadata
            metadata = {}
            metadata["techName"] = techName
            metadata["eventName"] = eventName
            metadata["comments"] = comments
            metadata["importDate"] = importDate
            data["metadata"] = metadata

            if hasStartDate:
                data["start"] = datetime.strptime(data["start"], self.dateformat)

            if hasXdate:
                data["x"] = datetime.strptime(data["x"], self.dateformat)

        return json

    def importJson(self, fileName):
        with open(fileName, 'r') as jsonFile:
            jsonStr = jsonFile.read()
            data = ujson.loads(jsonStr)
        return data

    def importKeypressData(self, techName, eventName, comments, importDate):
        data = self.importJson(self.keypressFile)
        data = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        return DataImport().importKeypressData(data)

    def importClick(self, techName, eventName, comments, importDate):
        data = self.importJson(self.clickFile)
        data = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        return DataImport().importClick(data)

    def importTimed(self, techName, eventName, comments, importDate):
        data = self.importJson(self.timedFile)
        data = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        return DataImport().importTimed(data)

    def importTsharkThroughput(self, techName, eventName, comments, importDate):
        data = self.importJson(self.tsharkThroughputFile)
        data = self.addExtraData(data, techName, eventName, comments, importDate, False, True)
        return DataImport().importTsharkThroughput(data)

    def importMultiIncludeThroughput(self, techName, eventName, comments, importDate):
        data = self.importJson(self.multiIncludeThroughputFile)
        data = self.addExtraData(data, techName, eventName, comments, importDate, False, True)
        return DataImport().importMultiIncludeThroughput(data)

    def importMultiExcludeThroughput(self, techName, eventName, comments, importDate):
        data = self.importJson(self.multiExcludeThroughputFile)
        data = self.addExtraData(data, techName, eventName, comments, importDate, False, True)
        return DataImport().importMultiExcludeThroughput(data)

    def importMultiExcludeProtocol(self, techName, eventName, comments, importDate):
        data = self.importJson(self.multiExcludeProtocolFile)
        multiExcludeProtocol = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        return DataImport().importMultiExcludeProtocol(multiExcludeProtocol)

    def importMultiIncludeProtocol(self, techName, eventName, comments, importDate):
        data = self.importJson(self.multiIncludeProtocolFile)
        multiIncludeProtocol = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        return DataImport().importMultiIncludeProtocol(multiIncludeProtocol)

    def importTsharkProtocol(self, techName, eventName, comments, importDate):
        data = self.importJson(self.tsharkProtocolFile)
        tsharkProtocol = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        return DataImport().importTsharkProtocol(tsharkProtocol)
