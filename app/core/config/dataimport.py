import ujson
from datetime import datetime

class DataImport:

    def __init__(self):
        self.keypressFile = "../json/keypressData.json"
        self.clickFile = "../json/click.json"
        self.timedFile = "../json/timed.json"

    def importKeypressData(name, computer):
        # get the JSON data
        data = importJson(self.keypressFile, name, computer)

        # add the new values to it and format dates
        data = addExtraData(data, name, computer, false)

        # todo get the datasource plugin.

        # call the insert method.
        pyKeyLogger = PyKeyLogger()
        insertedCount = pyKeyLogger.importKeypressData(data)
        return insertedCount

    def importClick(name, computer):
        # get the JSON data
        data = importJson(self.clickFile, name, computer)

        # add the new values to it and format dates
        eventData = addExtraData(data["events"], name, computer, true)
        data["events"] = eventData

        # todo get the datasource plugin.

        # call the insert method.
        pyKeyLogger = PyKeyLogger()
        insertedId = pyKeyLogger.importClick(data)
        return insertedId

    def importTimed(name, computer):
        # get the JSON data
        data = importJson(self.timedFile, name, computer)

        # add the new values to it and format dates
        eventData = addExtraData(data["events"], name, computer, true)
        data["events"] = eventData

        # todo get the datasource plugin.

        # call the insert method.
        pyKeyLogger = PyKeyLogger()
        insertedId = pyKeyLogger.importTimed(data)
        return insertedId


    def addExtraData(json, name, computer, hasEndDate):
        for data in json:
            data["importName"] = name
            data["computerName"] = computer
            data["start"] = datetime.strptime(data["start"], '%Y-%m-%d %H:%M:%S')

            if(hasEndDate)
                data["end"] = datetime.strptime(data["end"], '%Y-%m-%d %H:%M:%S')

        return json

    def importJson(fileName):
        with open(fileName, 'r') as jsonFile:
            jsonStr = jsonFile.read()
            data = ujson.loads(jsonStr)
        return data
