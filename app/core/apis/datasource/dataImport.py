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

class DataImport:

    def importKeypressData(self, jsonData):
        pyKeyPress = ConfigReader().getInstanceOfDatasourcePlugin("PyKeyPress")
        insertedCount = pyKeyPress.importKeypressData(jsonData)
        return insertedCount

    def importClick(self, jsonData):
        pyClick = ConfigReader().getInstanceOfDatasourcePlugin("PyClick")
        insertedCount = pyClick.importClick(jsonData)
        return insertedCount

    def importTimed(self, jsonData):
        pyTimed = ConfigReader().getInstanceOfDatasourcePlugin("PyTimed")
        insertedCount = pyTimed.importTimed(jsonData)
        return insertedCount

    def importTsharkThroughput(self, jsonData):
        tsharkThroughput = ConfigReader().getInstanceOfDatasourcePlugin("TsharkThroughput")
        insertedCount = tsharkThroughput.importTsharkThroughputData(jsonData)
        return insertedCount

    def importMultiExcludeThroughput(self, jsonData):
        multiExcludeThroughput = ConfigReader().getInstanceOfDatasourcePlugin("MultiExcludeThroughput")
        insertedCount = multiExcludeThroughput.importMultiExcludeThroughputData(jsonData)
        return insertedCount

    def importMultiIncludeThroughput(self, jsonData):
        multiInclude = ConfigReader().getInstanceOfDatasourcePlugin("MultiIncludeThroughput")
        insertedCount = multiInclude.importMultiIncludeThroughputData(jsonData)
        return insertedCount

    def importMultiExcludeProtocol(self, jsonData):
        multiExcludeProtocol = ConfigReader().getInstanceOfDatasourcePlugin("MultiExcludeProtocol")
        insertedCount = multiExcludeProtocol.importMultiExcludeProtocolData(jsonData)
        return insertedCount

    def importMultiIncludeProtocol(self, jsonData):
        multiIncludeProtocol = ConfigReader().getInstanceOfDatasourcePlugin("MultiIncludeProtocol")
        insertedCount = multiIncludeProtocol.importMultiIncludeProtocolData(jsonData)
        return insertedCount

    def importTsharkProtocol(self, jsonData):
        tsharkProtocol = ConfigReader().getInstanceOfDatasourcePlugin("TsharkProtocol")
        insertedCount = tsharkProtocol.importTsharkProtocolData(jsonData)
        return insertedCount
