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
from core.apis.datasource.common import Common


class DataExportConfig:
    def exportAllData(self, startDate, endDate, techName, eventName, moveFiles, exportLocation):
        self.exportClickData(startDate, endDate, techName, eventName, moveFiles, exportLocation)
        self.exporKeyPressData(startDate, endDate, techName, eventName, exportLocation)
        self.exportTimedData(startDate, endDate, techName, eventName, moveFiles, exportLocation)
        self.exportMultiExcludeProtocolData(startDate, endDate, techName, eventName, exportLocation)
        self.exportMultiExcludeThroughputData(startDate, endDate, techName, eventName, exportLocation)
        self.exportMultiIncludeProtocolData(startDate, endDate, techName, eventName, exportLocation)
        self.exportMultiIncludeThroughputData(startDate, endDate, techName, eventName, exportLocation)
        self.exportTsharkProtocolData(startDate, endDate, techName, eventName, exportLocation)
        self.exportTsharkThroughputData(startDate, endDate, techName, eventName, exportLocation)

    def exportClickData(self, startDate, endDate, techName, eventName, moveFiles, exportLocation):
        pyClickData = PyClick().selectClickData(startDate, endDate, techName, eventName)
        self.cleanupData(pyClickData, True, False)
        self.exportToFile(exportLocation + "\\pyKeyLogger", "click.json" , pyClickData)
        if moveFiles and len(pyClickData) > 0:
            self.copyImages(exportLocation + "\\pyKeyLogger\\click_images", pyClickData)
        return len(pyClickData)

    def exportKeyPressData(self, startDate, endDate, techName, eventName, exportLocation):
        pyKeyPressData = PyKeyPress().selectKeyPressData(startDate, endDate, techName, eventName)
        self.cleanupData(pyKeyPressData, True, False)
        self.exportToFile(exportLocation + "\\pyKeyLogger", "keyPress.json", pyKeyPressData)
        return len(pyKeyPressData)

    def exportTimedData(self, startDate, endDate, techName, eventName, moveFiles, exportLocation):
        pyTimedData = PyTimed().selectTimedData(startDate, endDate, techName, eventName)
        self.cleanupData(pyTimedData, True, False)
        self.exportToFile(exportLocation + "\\pyKeyLogger", "timed.json", pyTimedData)
        if moveFiles and len(pyTimedData) > 0:
            self.copyImages(exportLocation + "\\pyKeyLogger\\timed_images", pyTimedData)
        return len(pyTimedData)

    def exportMultiExcludeProtocolData(self, startDate, endDate, techName, eventName, exportLocation):
        multiExcludePrototcolData = MultiExcludeProtocol().selectMultiExcludeProtocolData(startDate, endDate, techName,
                                                                                      eventName)
        self.cleanupData(multiExcludePrototcolData, True, False)
        self.exportToFile(exportLocation + "\\multi_exec_tshark", "networkDataAll.json", multiExcludePrototcolData)
        return len(multiExcludePrototcolData)

    def exportMultiExcludeThroughputData(self, startDate, endDate, techName, eventName, exportLocation):
        multiExcludeThroughputData = MultiExcludeThroughput().selectMultiExcludeThroughputData(startDate, endDate,
                                                                                               techName, eventName)
        self.cleanupData(multiExcludeThroughputData, False, True)
        self.exportToFile(exportLocation + "\\multi_exec_tshark", "networkDataXY.json", multiExcludeThroughputData)
        return len(multiExcludeThroughputData)

    def exportMultiIncludeProtocolData(self, startDate, endDate, techName, eventName, exportLocation):
        multiIncludeProtocolData = MultiIncludeProtocol().selectMultiIncludeProtocolData(startDate, endDate, techName,
                                                                                     eventName)
        self.cleanupData(multiIncludeProtocolData, True, False)
        self.exportToFile(exportLocation + "\\multi_incl_tshark", "networkDataAll.json", multiIncludeProtocolData)
        return len(multiIncludeProtocolData)

    def exportMultiIncludeThroughputData(self, startDate, endDate, techName, eventName, exportLocation):
        multiIncludeThroughputData = MultiIncludeThroughput().selectMultiIncludeThroughputData(startDate, endDate,
                                                                                               techName, eventName)
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

    def exportToFile(self, outputDirectory, outputFileName, jsonToExport):
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
        for dataObj in dataObjects:
            dataObj.pop("id", None)
            dataObj.pop("_id", None)

            dataObj["metadata"]["importDate"] = Common().formatDateStringToUTC(dataObj["metadata"]["importDate"])
            if hasStartDate:
                dataObj["start"] = Common().formatDateStringToUTC(dataObj["start"])

            if hasXDate:
                dataObj["x"] = Common().formatDateStringToUTC(dataObj["x"])
