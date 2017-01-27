#  Copyright (C) 2016  Jamie Acosta, Jennifer Weand, Juan Soto, Mark Eby, Mark Smith, Andres Olivas
#
# This file is part of DssVisualizer.
#
# DssVisualizer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DssVisualizer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DssVisualizer.  If not, see <http://www.gnu.org/licenses/>.

import ujson
import os
import shutil
from core.apis.datasource.pyClick import PyClick
from core.apis.datasource.pyKeyPress import PyKeyPress
from core.apis.datasource.pyTimed import PyTimed
from core.apis.datasource.multiExcludeProtocol import MultiExcludeProtocol
from core.apis.datasource.multiExcludeThroughput import MultiExcludeThroughput
from core.apis.datasource.multiIncludeProtocol import MultiIncludeProtocol
from core.apis.datasource.multiIncludeThroughput import MultiIncludeThroughput
from core.apis.datasource.tsharkProtocol import TsharkProtocol
from core.apis.datasource.tsharkThroughput import TsharkThroughput
from core.apis.datasource.manualScreenShot import ManualScreenShot
from core.apis.datasource.snoopy import Snoopy
from core.apis.datasource.common import Common

class DataImport:

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
        self.manualScreenShotFile = "json/manualScreenShot/snap.json"
        self.snoopyFile = "json/snoopyData.json"

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

        # ' by ' is used to concatenate the event and tech name together for the search dropdown
        # it is therefore used to split the string as well when it's being used again back here.
        # so we don't want an extra ' by ' in either name to mess that up later on down the line.
        techName = techName.replace(" by ", " ")
        eventName = eventName.replace(" by ", " ")

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

    def copyImages(self, json, newImageLocation):
        """This method will copy the images from the location found in the JSON file to newImageLocation and update the path
        in the JSON object.

        :param json: A python object of the parsed JSON
        :type json: object[]
        :param newImageLocation: The path to where the images should be copied to.
        :type newImageLocation: str
        :returns: A python object of the parsed JSON
        """

        if not os.path.exists(newImageLocation):
            os.makedirs(newImageLocation)

        for dataObj in json:

            # get the location of the image from the object.
            split = os.path.split(dataObj["title"])
            originalImageLocation = split[0]
            imageName = split[1]

            # copy the image into the export path
            fullFileName = os.path.join(originalImageLocation, imageName)
            if os.path.isfile(fullFileName):
                shutil.copy(fullFileName, newImageLocation)

            # update raw json with the new file path
            dataObj["title"] = newImageLocation + imageName

        return json

    def importAllDataFromFiles(self, fileLocation, techName, eventName, comments, importDate, copyImages):
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
        :param copyImages: True if the Click, Timed, Manual Screenshot images should be moved into our file system, False if they should stay where they are.
        :type copyImages: bool
        :return:
        """
        for subdir, dirs, files in os.walk(fileLocation):
            for file in files:
                fullFileName = os.path.join(subdir, file)
                if os.path.isfile(fullFileName) and file.lower().endswith(".json"):
                    if "click" in fullFileName.lower():
                        self.importClickFile(fullFileName, techName, eventName, comments, importDate, copyImages)
                    elif "keypressdata" in fullFileName.lower():
                        self.importKeypressDataFile(fullFileName, techName, eventName, comments, importDate)
                    elif "timed" in fullFileName.lower():
                        self.importTimedFile(fullFileName, techName, eventName, comments, importDate, copyImages)

                    elif "multi_exc_tshark" in fullFileName.lower() and "networkdataall" in fullFileName.lower():
                        self.importMultiExcludeProtocolFile(fullFileName, techName, eventName, comments, importDate)
                    elif "multi_exc_tshark" in fullFileName.lower() and "networkdataxy" in fullFileName.lower():
                        self.importMultiExcludeThroughputFile(fullFileName, techName, eventName, comments, importDate)

                    elif "multi_inc_tshark" in fullFileName.lower() and "networkdataall" in fullFileName.lower():
                        self.importMultiIncludeProtocolFile(fullFileName, techName, eventName, comments, importDate)
                    elif "multi_inc_tshark" in fullFileName.lower() and "networkdataxy" in fullFileName.lower():
                        self.importMultiIncludeThroughputFile(fullFileName, techName, eventName, comments, importDate)

                    elif "tshark" in fullFileName.lower() and "networkdataall" in fullFileName.lower():
                        self.importTsharkProtocolFile(fullFileName, techName, eventName, comments, importDate)
                    elif "tshark" in fullFileName.lower() and "networkdataxy" in fullFileName.lower():
                        self.importTsharkThroughputFile(fullFileName, techName, eventName, comments, importDate)
                    elif "snoopy" in fullFileName.lower():
                        self.importSnoopyDataFile(fullFileName, techName, eventName, comments, importDate)
                    elif "snap" in fullFileName.lower():
                        self.importManualScreenShotFile(fullFileName, techName, eventName, comments, importDate, copyImages)

    def importClick(self, techName, eventName, comments, importDate, copyImages):
        return self.importClickFile(self.clickFile, techName, eventName, comments, importDate, copyImages)

    def importClickFile(self, fullFileName, techName, eventName, comments, importDate, copyImages):
        data = self.importJson(fullFileName)
        data = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        if copyImages:
            data = self.copyImages(data, "images/click/")
        return PyClick().importClick(data)

    def importKeypressData(self, techName, eventName, comments, importDate):
        return self.importKeypressDataFile(self.keypressFile, techName, eventName, comments, importDate)
	


    def importKeypressDataFile(self, fullFileName, techName, eventName, comments, importDate):
        data = self.importJson(fullFileName)
        data = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        return PyKeyPress().importKeypressData(data)

    def importSnoopyData(self, techName, eventName, comments, importDate):
        return self.importSnoopyDataFile(self.snoopyFile, techName, eventName, comments, importDate)
	
    def importSnoopyDataFile(self, fullFileName, techName, eventName, comments, importDate):
        data = self.importJson(fullFileName)
        data = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        return Snoopy().importSnoopyData(data)
############
		
    def importTimed(self, techName, eventName, comments, importDate, copyImages):
        return self.importTimedFile(self.timedFile, techName, eventName, comments, importDate, copyImages)

    def importTimedFile(self, fullFileName, techName, eventName, comments, importDate, copyImages):
        data = self.importJson(fullFileName)
        data = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        if copyImages:
            data = self.copyImages(data, "images/timed/")
        return PyTimed().importTimed(data)

    def importMultiExcludeProtocol(self, techName, eventName, comments, importDate):
        return self.importMultiExcludeProtocolFile(self.multiExcludeProtocolFile, techName, eventName,
                                                   comments, importDate)

    def importMultiExcludeProtocolFile(self, fullFileName, techName, eventName, comments, importDate):
        data = self.importJson(fullFileName)
        multiExcludeProtocol = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        return MultiExcludeProtocol().importMultiExcludeProtocol(multiExcludeProtocol)

    def importMultiExcludeThroughput(self, techName, eventName, comments, importDate):
        return self.importMultiExcludeThroughputFile(self.multiExcludeThroughputFile, techName, eventName,
                                                     comments, importDate)

    def importMultiExcludeThroughputFile(self, fullFileName, techName, eventName, comments, importDate):
        data = self.importJson(fullFileName)
        data = self.addExtraData(data, techName, eventName, comments, importDate, False, True)
        return MultiExcludeThroughput().importMultiExcludeThroughput(data)

    def importMultiIncludeProtocol(self, techName, eventName, comments, importDate):
        return self.importMultiIncludeProtocolFile(self.multiIncludeProtocolFile, techName, eventName,
                                                   comments, importDate)

    def importMultiIncludeProtocolFile(self, fullFileName, techName, eventName, comments, importDate):
        data = self.importJson(fullFileName)
        multiIncludeProtocol = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        return MultiIncludeProtocol().importMultiIncludeProtocol(multiIncludeProtocol)

    def importMultiIncludeThroughput(self, techName, eventName, comments, importDate):
        return self.importMultiIncludeThroughputFile(self.multiIncludeThroughputFile, techName, eventName,
                                                     comments, importDate)

    def importMultiIncludeThroughputFile(self, fullFileName, techName, eventName, comments, importDate):
        data = self.importJson(fullFileName)
        data = self.addExtraData(data, techName, eventName, comments, importDate, False, True)
        return MultiIncludeThroughput().importMultiIncludeThroughput(data)

    def importTsharkProtocol(self, techName, eventName, comments, importDate):
        return self.importTsharkProtocolFile(self.tsharkProtocolFile, techName, eventName, comments, importDate)

    def importTsharkProtocolFile(self, fullFileName, techName, eventName, comments, importDate):
        data = self.importJson(fullFileName)
        tsharkProtocol = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        return TsharkProtocol().importTsharkProtocol(tsharkProtocol)

    def importTsharkThroughput(self, techName, eventName, comments, importDate):
        return self.importTsharkThroughputFile(self.tsharkThroughputFile, techName, eventName, comments, importDate)

    def importTsharkThroughputFile(self, fullFileName, techName, eventName, comments, importDate):
        data = self.importJson(fullFileName)
        data = self.addExtraData(data, techName, eventName, comments, importDate, False, True)
        return TsharkThroughput().importTsharkThroughput(data)

    def importManualScreenShot(self, techName, eventName, comments, importDate, copyImages):
        return self.importManualScreenShotFile(self.manualScreenShotFile, techName, eventName, comments, importDate, copyImages)

    def importManualScreenShotFile(self, fullFileName, techName, eventName, comments, importDate, copyImages):
        data = self.importJson(fullFileName)
        data = self.addExtraData(data, techName, eventName, comments, importDate, True, False)
        if copyImages:
            data = self.copyImages(data, "images/manualscreenshot/")
        return ManualScreenShot().importManualScreenShot(data)

