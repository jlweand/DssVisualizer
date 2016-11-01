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

import json
import os
import shutil
from bson import json_util
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
from core.apis.datasource.common import Common


class DataExport:

    def exportAllData(self, startDate, endDate, techName, eventName, copyImages, exportLocation):
        """Selects and exports all data to the exportLocation based on the start and end dates, tech name, event name.  Will copy images to exportLocation if copyImages is True.

        :param startDate: The datetime to return data
        :type startDate: str
        :param endDate: The datetime to return data
        :type endDate: str
        :param techName: The technician name to return data
        :type techName: str
        :param eventName: The name of the event to return data
        :type eventName: str
        :param copyImages: Flag to indicate whether to copy images to exportLocation
        :type copyImages: bool
        :param exportLocation: Base path to copy all json and images (if requested).  Data will all be copied to their specific folders within exportLocation.
        :type exportLocation: str
        :return:
        """
        self.exportClickData(startDate, endDate, techName, eventName, copyImages, exportLocation)
        self.exportKeyPressData(startDate, endDate, techName, eventName, exportLocation)
        self.exportTimedData(startDate, endDate, techName, eventName, copyImages, exportLocation)
        self.exportMultiExcludeProtocolData(startDate, endDate, techName, eventName, exportLocation)
        self.exportMultiExcludeThroughputData(startDate, endDate, techName, eventName, exportLocation)
        self.exportMultiIncludeProtocolData(startDate, endDate, techName, eventName, exportLocation)
        self.exportMultiIncludeThroughputData(startDate, endDate, techName, eventName, exportLocation)
        self.exportTsharkProtocolData(startDate, endDate, techName, eventName, exportLocation)
        self.exportTsharkThroughputData(startDate, endDate, techName, eventName, exportLocation)
        self.exportManualScreenShotData(startDate, endDate, techName, eventName, copyImages, exportLocation)

    def exportClickData(self, startDate, endDate, techName, eventName, copyImages, exportLocation):
        pyClickData = PyClick().selectClickData(startDate, endDate, techName, eventName)
        self.cleanupData(pyClickData, True, False)
        self.exportToFile(exportLocation + "\\pyKeyLogger", "click.json" , pyClickData)
        if copyImages and len(pyClickData) > 0:
            self.copyImages(exportLocation + "\\pyKeyLogger\\click_images", pyClickData)
        return len(pyClickData)

    def exportKeyPressData(self, startDate, endDate, techName, eventName, exportLocation):
        pyKeyPressData = PyKeyPress().selectKeyPressData(startDate, endDate, techName, eventName)
        self.cleanupData(pyKeyPressData, True, False)
        self.exportToFile(exportLocation + "\\pyKeyLogger", "keyPress.json", pyKeyPressData)
        return len(pyKeyPressData)

    def exportTimedData(self, startDate, endDate, techName, eventName, copyImages, exportLocation):
        pyTimedData = PyTimed().selectTimedData(startDate, endDate, techName, eventName)
        self.cleanupData(pyTimedData, True, False)
        self.exportToFile(exportLocation + "\\pyKeyLogger", "timed.json", pyTimedData)
        if copyImages and len(pyTimedData) > 0:
            self.copyImages(exportLocation + "\\pyKeyLogger\\timed_images", pyTimedData)
        return len(pyTimedData)

    def exportMultiExcludeProtocolData(self, startDate, endDate, techName, eventName, exportLocation):
        multiExcludePrototcolData = MultiExcludeProtocol().selectMultiExcludeProtocolData(startDate, endDate, techName, eventName)
        self.cleanupData(multiExcludePrototcolData, True, False)
        self.exportToFile(exportLocation + "\\multi_exec_tshark", "networkDataAll.json", multiExcludePrototcolData)
        return len(multiExcludePrototcolData)

    def exportMultiExcludeThroughputData(self, startDate, endDate, techName, eventName, exportLocation):
        multiExcludeThroughputData = MultiExcludeThroughput().selectMultiExcludeThroughputData(startDate, endDate, techName, eventName)
        self.cleanupData(multiExcludeThroughputData, False, True)
        self.exportToFile(exportLocation + "\\multi_exec_tshark", "networkDataXY.json", multiExcludeThroughputData)
        return len(multiExcludeThroughputData)

    def exportMultiIncludeProtocolData(self, startDate, endDate, techName, eventName, exportLocation):
        multiIncludeProtocolData = MultiIncludeProtocol().selectMultiIncludeProtocolData(startDate, endDate, techName, eventName)
        self.cleanupData(multiIncludeProtocolData, True, False)
        self.exportToFile(exportLocation + "\\multi_incl_tshark", "networkDataAll.json", multiIncludeProtocolData)
        return len(multiIncludeProtocolData)

    def exportMultiIncludeThroughputData(self, startDate, endDate, techName, eventName, exportLocation):
        multiIncludeThroughputData = MultiIncludeThroughput().selectMultiIncludeThroughputData(startDate, endDate, techName, eventName)
        self.cleanupData(multiIncludeThroughputData, False, True)
        self.exportToFile(exportLocation + "\\multi_incl_tshark", "networkDataXY.json", multiIncludeThroughputData)
        return len(multiIncludeThroughputData)

    def exportTsharkProtocolData(self, startDate, endDate, techName, eventName, exportLocation):
        tsharkPrototcolData = TsharkProtocol().selectTsharkProtocolData(startDate, endDate, techName, eventName)
        self.cleanupData(tsharkPrototcolData, True, False)
        self.exportToFile(exportLocation + "\\tshark", "networkDataAll.json", tsharkPrototcolData)
        return len(tsharkPrototcolData)

    def exportTsharkThroughputData(self, startDate, endDate, techName, eventName, exportLocation):
        tsharkThroughputData = TsharkThroughput().selectTsharkThroughputData(startDate, endDate, techName, eventName)
        self.cleanupData(tsharkThroughputData, False, True)
        self.exportToFile(exportLocation + "\\tshark", "networkDataXY.json", tsharkThroughputData)
        return len(tsharkThroughputData)

    def exportManualScreenShotData(self, startDate, endDate, techName, eventName, copyImages, exportLocation):
        manualScreenShotData = ManualScreenShot().selectManualScreenShotData(startDate, endDate, techName, eventName)
        self.cleanupData(manualScreenShotData, True, False)
        self.exportToFile(exportLocation + "\\manualscreenshot", "snap.json", manualScreenShotData)
        if copyImages and len(manualScreenShotData) > 0:
            self.copyImages(exportLocation + "\\manualscreenshot\\images", manualScreenShotData)
        return len(manualScreenShotData)

    def exportToFile(self, outputDirectory, outputFileName, jsonToExport):
        """Creates the output directory, and dumps the JSON data to the specified file. Right now the JSON is pretty printed.
        There is a commented out json.dump command that will print the JOSN all on one line if it's needed in the future.

        :param outputDirectory: The directory to write the file to.
        :type outputDirectory: str
        :param outputFileName: The filename of the file.
        :type outputFileName: str
        :param jsonToExport: A python object of the parsed JSON
        :type jsonToExport: object[]
        """
        # check that the output directory exists and create it if not.
        if not os.path.exists(outputDirectory):
            os.makedirs(outputDirectory)

        fullFileName = os.path.join(outputDirectory, outputFileName)

        with open(fullFileName, 'w') as file:
            # pretty print
            json.dump(jsonToExport, file, default=json_util.default, sort_keys=True, indent=2, ensure_ascii=False)
            # not pretty print
            # json.dump(jsonToExport, file, default=json_util.default)

    def copyImages(self, exportPath, dataObjects):
        """This method will copy the images from the location found in the JSON file to newImageLocation and update the path
        in the JSON object.

        :param dataObjects: A python object of the parsed JSON
        :type dataObjects: object[]
        :param exportPath: The path to where the images should be copied to.
        :type exportPath: str
        :returns: A python object of the parsed JSON
        """
        # check that the output directory exists and create it if not.
        if not os.path.exists(exportPath):
            os.makedirs(exportPath)

        # we only want to export the images for the data we are exporting
        for dataObj in dataObjects:
            # get the location of the image from the object.
            indexOf = dataObj["title"].rfind('/')
            originalImageLocation = dataObj["title"][:indexOf]
            fileName = dataObj["title"][indexOf+1:]

            # copy the image into the export path
            fullFileName = os.path.join(originalImageLocation, fileName)
            if os.path.isfile(fullFileName):
                shutil.copy(fullFileName, exportPath)

    def cleanupData(self, dataObjects, hasStartDate, hasXDate):
        """ Takes the data selected from the data source, removes the IDs, adds an exportedDate to the metadata and
         converts all dates to ISO_8601 UTC strings

        :param dataObjects: A python object of the parsed JSON
        :type dataObjects: object[]
        :param hasStartDate: Flag to convert the 'start' date in the object.
        :type hasStartDate: bool
        :param hasXDate: Flag to convert the 'x' date in the object.
        :type hasXDate: bool
        """
        for dataObj in dataObjects:
            dataObj.pop("id", None)
            dataObj.pop("_id", None)

            dataObj["metadata"]["exportDate"] = Common().getRightNowAsUTCString()
            dataObj["metadata"]["importDate"] = Common().getLocalStringDateAsUTCString(dataObj["metadata"]["importDate"])
            if hasStartDate:
                dataObj["start"] = Common().getLocalStringDateAsUTCString(dataObj["start"])

            if hasXDate:
                dataObj["x"] = Common().getLocalStringDateAsUTCString(dataObj["x"])
