import ujson
import os
import shutil
from core.apis.datasource.dataImport import DataImport
from core.apis.datasource.common import Common

class DataImportConfig:

    def __init__(self):
        self.clickFile = "json/pyKeyLogger/click.json"
        self.keypressFile = "json/pyKeyLogger/keypressData.json"
        self.timedFile = "json/pyKeyLogger/timed.json"
        self.multiExcludeProtocolFile = "json/multi_exec_tshark/networkDataAll.json"
        self.multiExcludeThroughputFile = "json/multi_exec_tshark/networkDataXY.json"
        self.multiIncludeProtocolFile = "json/multi_incl_tshark/networkDataAll.json"
        self.multiIncludeThroughputFile = "json/multi_incl_tshark/networkDataXY.json"
        self.tsharkProtocolFile = "json/tshark/networkDataAll.json"
        self.tsharkThroughputFile = "json/tshark/networkDataXY.json"

    def addExtraData(self, json, techName, eventName, comments, importDate, hasStartDate, hasXdate):
        """This method will add the metadata to each object as well as convert any dates into a datetime object

        :param json: A python object of the parsed JSON
        :type json: object[]
        :param techName: User entered value
        :type techName: str
        :param eventName: User entered value
        :type eventName: str
        :param comments: User entered value
        :type comments: str
        :param importDate: User entered value for imported date
        :type importDate: str
        :param hasStartDate: Flag to indicate if the JSON has a "start" attribute
        :type hasStartDate: bool
        :param hasXdate: Flag to indicate if the JSON has an "x" attribute
        :type hasXdate: bool
        :returns: The JSON object with metadata and datetime dates
        """

        for data in json:

            #create the metadata
            metadata = {}
            metadata["techName"] = techName
            metadata["eventName"] = eventName
            metadata["comments"] = comments
            metadata["importDate"] = Common().formatDateStringToUTC(importDate)
            data["metadata"] = metadata

            if hasStartDate:
                data["start"] = Common().addUTCToDate(data["start"])

            if hasXdate:
                data["x"] = Common().addUTCToDate(data["x"])

        return json

    def importJson(self, fileName):
        """Single method to read in a JSON file and load it into an object[]

        :param fileName: The absolute or relative path of the file with file name.
        :type fileName: str
        :returns: A python object of the parsed JSON
        """
        with open(fileName, 'r') as jsonFile:
            jsonStr = jsonFile.read()
            data = ujson.loads(jsonStr)
        return data

    def moveImages(self, json, originalImageLocation, newImageLocation):
        """This method will moves the images from originalImageLocation to newImageLocation and update the path
        in the JSON object.

        :param json: A python object of the parsed JSON
        :type json: object[]
        :param originalImageLocation: the path of the original location of the images.
        :type originalImageLocation: str
        :param newImageLocation: The path to where the images should be copied to.
        :type newImageLocation: str
        :returns: A python object of the parsed JSON
        """
        # copy the images into our file system
        src_files = os.listdir(originalImageLocation)
        for fileName in src_files:
            if fileName.lower().endswith('.png'):
                fullFileName = os.path.join(originalImageLocation, fileName)
                if os.path.isfile(fullFileName):
                    shutil.copy(fullFileName, newImageLocation)

        # update raw json with the new file path
        for data in json:
            indexOf = data["title"].rfind('/')
            imageName = data["title"][indexOf+1:]
            data["title"] = newImageLocation + imageName

        return json

    def importAllDataFromFiles(self, fileLocation, techName, eventName, comments, importDate):
        """This method will recursive search all folders.  if it finds a .json file it will try to import it based
        on the folder and file name.

        :param fileLocation: The path of the parent directory in which to import all json files.
        :type fileLocation: str
        :param techName: User entered value
        :type techName: str
        :param eventName: User entered value
        :type eventName: str
        :param comments: User entered value
        :type comments: str
        :param importDate: User entered value for imported date
        :type importDate: str
        :return:
        """
        for subdir, dirs, files in os.walk(fileLocation):
            for file in files:
                fullFileName = os.path.join(subdir, file)
                if os.path.isfile(fullFileName) and file.lower().endswith(".json"):
                    if "click" in fullFileName.lower():
                        self.importClickFile(fullFileName, techName, eventName, comments, importDate, False, "")
                    elif "keypressdata" in fullFileName.lower():
                        self.importKeypressDataFile(fullFileName, techName, eventName, comments, importDate)
                    elif "timed" in fullFileName.lower():
                        self.importTimedFile(fullFileName, techName, eventName, comments, importDate, False, "")

                    elif "multi_exec_tshark" in fullFileName.lower() and "networkdataall" in fullFileName.lower():
                        self.importMultiExcludeProtocolFile(fullFileName, techName, eventName, comments, importDate)
                    elif "multi_exec_tshark" in fullFileName.lower() and "networkdataxy" in fullFileName.lower():
                        self.importMultiExcludeThroughputFile(fullFileName, techName, eventName, comments, importDate)

                    elif "multi_incl_tshark" in fullFileName.lower() and "networkdataall" in fullFileName.lower():
                        self.importMultiIncludeProtocolFile(fullFileName, techName, eventName, comments, importDate)
                    elif "multi_incl_tshark" in fullFileName.lower() and "networkdataxy" in fullFileName.lower():
                        self.importMultiIncludeThroughputFile(fullFileName, techName, eventName, comments, importDate)

                    elif "tshark" in fullFileName.lower() and "networkdataall" in fullFileName.lower():
                        self.importTsharkProtocolFile(fullFileName, techName, eventName, comments, importDate)
                    elif "tshark" in fullFileName.lower() and "networkdataxy" in fullFileName.lower():
                        self.importTsharkThroughputFile(fullFileName, techName, eventName, comments, importDate)


    def importClick(self, techName, eventName, comments, importDate, moveImages, originalImageLocation):
        return self.importClickFile(self.clickFile, techName, eventName, comments, importDate, moveImages,
                                    originalImageLocation)

    def importClickFile(self, fullFileName, techName, eventName, comments, importDate, moveImages,
                        originalImageLocation):
        data = self.importJson(fullFileName)
        data = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        if moveImages:
            data = self.moveImages(data, originalImageLocation, "images/click/")
        return DataImport().importClick(data)

    def importKeypressData(self, techName, eventName, comments, importDate):
        return self.importKeypressDataFile(self.keypressFile, techName, eventName, comments, importDate)

    def importKeypressDataFile(self, fullFileName, techName, eventName, comments, importDate):
        data = self.importJson(fullFileName)
        data = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        return DataImport().importKeypressData(data)

    def importTimed(self, techName, eventName, comments, importDate, moveImages, originalImageLocation):
        return self.importTimedFile(self.timedFile, techName, eventName, comments, importDate, moveImages,
                                    originalImageLocation)

    def importTimedFile(self, fullFileName, techName, eventName, comments, importDate, moveImages,
                        originalImageLocation):
        data = self.importJson(fullFileName)
        data = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        if moveImages:
            data = self.moveImages(data, originalImageLocation, "images/timed/")
        return DataImport().importTimed(data)

    def importMultiExcludeProtocol(self, techName, eventName, comments, importDate):
        return self.importMultiExcludeProtocolFile(self.multiExcludeProtocolFile, techName, eventName,
                                                   comments, importDate)

    def importMultiExcludeProtocolFile(self, fullFileName, techName, eventName, comments, importDate):
        data = self.importJson(fullFileName)
        multiExcludeProtocol = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        return DataImport().importMultiExcludeProtocol(multiExcludeProtocol)

    def importMultiExcludeThroughput(self, techName, eventName, comments, importDate):
        return self.importMultiExcludeThroughputFile(self.multiExcludeThroughputFile, techName, eventName,
                                                     comments, importDate)

    def importMultiExcludeThroughputFile(self, fullFileName, techName, eventName, comments, importDate):
        data = self.importJson(fullFileName)
        data = self.addExtraData(data, techName, eventName, comments, importDate, False, True)
        return DataImport().importMultiExcludeThroughput(data)

    def importMultiIncludeProtocol(self, techName, eventName, comments, importDate):
        return self.importMultiIncludeProtocolFile(self.multiIncludeProtocolFile, techName, eventName,
                                                   comments, importDate)

    def importMultiIncludeProtocolFile(self, fullFileName, techName, eventName, comments, importDate):
        data = self.importJson(fullFileName)
        multiIncludeProtocol = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        return DataImport().importMultiIncludeProtocol(multiIncludeProtocol)

    def importMultiIncludeThroughput(self, techName, eventName, comments, importDate):
        return self.importMultiIncludeThroughputFile(self.multiIncludeThroughputFile, techName, eventName,
                                                     comments, importDate)

    def importMultiIncludeThroughputFile(self, fullFileName, techName, eventName, comments, importDate):
        data = self.importJson(fullFileName)
        data = self.addExtraData(data, techName, eventName, comments, importDate, False, True)
        return DataImport().importMultiIncludeThroughput(data)

    def importTsharkProtocol(self, techName, eventName, comments, importDate):
        return self.importTsharkProtocolFile(self.tsharkProtocolFile, techName, eventName, comments, importDate)

    def importTsharkProtocolFile(self, fullFileName, techName, eventName, comments, importDate):
        data = self.importJson(fullFileName)
        tsharkProtocol = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        return DataImport().importTsharkProtocol(tsharkProtocol)

    def importTsharkThroughput(self, techName, eventName, comments, importDate):
        return self.importTsharkThroughputFile(self.tsharkThroughputFile, techName, eventName, comments, importDate)

    def importTsharkThroughputFile(self, fullFileName, techName, eventName, comments, importDate):
        data = self.importJson(fullFileName)
        data = self.addExtraData(data, techName, eventName, comments, importDate, False, True)
        return DataImport().importTsharkThroughput(data)

