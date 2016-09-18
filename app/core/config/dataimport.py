import ujson
from datetime import datetime

class DataImport:

    def __init__(self):
        self.keypressFile = "json/keypressData.json"
        self.clickFile = "json/click.json"
        self.timedFile = "json/timed.json"

    def addExtraData(self, json, name, computer, hasEndDate):
        for data in json:
            data["importName"] = name
            data["computerName"] = computer
            # todo get the date parsing working
            #data["start"] = datetime.strptime(data["start"], '%a %b %d %H:%M:%S %Z %Y')

            #if(hasEndDate):
            #    data["end"] = datetime.strptime(data["end"], '%a %b %d %H:%M:%S %Z %Y')

        return json

    def importJson(self, fileName):
        with open(fileName, 'r') as jsonFile:
            jsonStr = jsonFile.read()
            data = ujson.loads(jsonStr)
        return data

    def getInstacneOfPlugin(self):
        # todo get this information from the config.json
        module = "plugins.datasource.mongodb.pykeylogger"
        classname = "PyKeyLogger"

        #import the module by saying 'from myApp.models import Blog'
        module = __import__(module, {}, {}, classname)

        #now you can instantiate the class
        obj = getattr(module, classname )()
        return obj

    def importKeypressData(self, name, computer):
        # get the JSON data
        data = self.importJson(self.keypressFile)

        # add the new values to it and format dates
        data = self.addExtraData(data, name, computer, False)

        # get the datasource plugin.
        pyKeyLogger = self.getInstacneOfPlugin()

        # call the insert method.
        insertedCount = pyKeyLogger.importKeypressData(data)
        return insertedCount

    def importClick(self, name, computer):
        data = self.importJson(self.clickFile)

        eventData = self.addExtraData( data["events"], name, computer, True)
        data["events"] = eventData

        pyKeyLogger = self.getInstacneOfPlugin()

        insertedId = pyKeyLogger.importClick(data)
        return insertedId

    def importTimed(self, name, computer):
        data = self.importJson(self.timedFile)

        eventData = self.addExtraData(data["events"], name, computer, True)
        data["events"] = eventData

        pyKeyLogger = self.getInstacneOfPlugin()

        insertedId = pyKeyLogger.importTimed(data)
        return insertedId
