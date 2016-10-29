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

from core.config.configReader import ConfigReader
from core.apis.datasource.pyClick import PyClick

class DataExport:

    def exportClick(self, startDate, endDate, techName, eventName):
        return PyClick().selectClickData(startDate, endDate, techName, eventName)

    def exportKeypressData(self, jsonData):
        pyKeyPress = ConfigReader().getInstanceOfDatasourcePlugin("PyKeyPress")
        insertedCount = pyKeyPress.exportKeypressData(jsonData)
        return insertedCount

    def exportTimed(self, jsonData):
        pyTimed = ConfigReader().getInstanceOfDatasourcePlugin("PyTimed")
        insertedCount = pyTimed.exportTimed(jsonData)
        return insertedCount

    def exportTsharkThroughput(self, jsonData):
        tsharkThroughput = ConfigReader().getInstanceOfDatasourcePlugin("TsharkThroughput")
        insertedCount = tsharkThroughput.exportTsharkThroughputData(jsonData)
        return insertedCount

    def exportMultiExcludeThroughput(self, jsonData):
        multiExcludeThroughput = ConfigReader().getInstanceOfDatasourcePlugin("MultiExcludeThroughput")
        insertedCount = multiExcludeThroughput.exportMultiExcludeThroughputData(jsonData)
        return insertedCount

    def exportMultiIncludeThroughput(self, jsonData):
        multiInclude = ConfigReader().getInstanceOfDatasourcePlugin("MultiIncludeThroughput")
        insertedCount = multiInclude.exportMultiIncludeThroughputData(jsonData)
        return insertedCount

    def exportMultiExcludeProtocol(self, jsonData):
        multiExcludeProtocol = ConfigReader().getInstanceOfDatasourcePlugin("MultiExcludeProtocol")
        insertedCount = multiExcludeProtocol.exportMultiExcludeProtocolData(jsonData)
        return insertedCount

    def exportMultiIncludeProtocol(self, jsonData):
        multiIncludeProtocol = ConfigReader().getInstanceOfDatasourcePlugin("MultiIncludeProtocol")
        insertedCount = multiIncludeProtocol.exportMultiIncludeProtocolData(jsonData)
        return insertedCount

    def exportTsharkProtocol(self, jsonData):
        tsharkProtocol = ConfigReader().getInstanceOfDatasourcePlugin("TsharkProtocol")
        insertedCount = tsharkProtocol.exportTsharkProtocolData(jsonData)
        return insertedCount
