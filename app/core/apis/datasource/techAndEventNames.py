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

class TechAndEventNames:
    """This class will consolidate all the unique technician names and events names in the active data source.
    It will select from ManualScreenshot, MultiExcludeThroughput, MultiIncludeThroughput, PyKeyPress, and TsharkThroughput
    since that will hit each 'group' of data that can be captured and parsed separately. Those Plugin classes will need
    a method to get both distinct Event Names and Technician Names from the datasource.
    """

    def getDistinctTechNames(self):
        keyPressPlugin = ConfigReader().getInstanceOfDatasourcePlugin("PyKeyPress")
        multiExcludePlugin = ConfigReader().getInstanceOfDatasourcePlugin("MultiExcludeThroughput")
        multiIncludePlugin = ConfigReader().getInstanceOfDatasourcePlugin("MultiIncludeThroughput")
        tsharkPlugin = ConfigReader().getInstanceOfDatasourcePlugin("TsharkThroughput")
        screenshotPlugin = ConfigReader().getInstanceOfDatasourcePlugin("ManualScreenShot")

        keyPressTechNames = keyPressPlugin.getDistinctTechNames()
        multiExcludeTechNames = multiExcludePlugin.getDistinctTechNames()
        multiIncludeTechNames = multiIncludePlugin.getDistinctTechNames()
        tsharkTechNames = tsharkPlugin.getDistinctTechNames()
        screenshotTechNames = screenshotPlugin.getDistinctTechNames()

        return self.getDistinctValues(keyPressTechNames, multiExcludeTechNames, multiIncludeTechNames, tsharkTechNames, screenshotTechNames)

    def getDistinctEventNames(self):
        keyPressPlugin = ConfigReader().getInstanceOfDatasourcePlugin("PyKeyPress")
        multiExcludePlugin = ConfigReader().getInstanceOfDatasourcePlugin("MultiExcludeThroughput")
        multiIncludePlugin = ConfigReader().getInstanceOfDatasourcePlugin("MultiIncludeThroughput")
        tsharkPlugin = ConfigReader().getInstanceOfDatasourcePlugin("TsharkThroughput")
        screenshotPlugin = ConfigReader().getInstanceOfDatasourcePlugin("ManualScreenShot")

        keyPressEventNames = keyPressPlugin.getDistinctEventNames()
        multiExcludeEventNames = multiExcludePlugin.getDistinctEventNames()
        multiInludeEventNames = multiIncludePlugin.getDistinctEventNames()
        tsharkEventNames = tsharkPlugin.getDistinctEventNames()
        screenshotEventNames = screenshotPlugin.getDistinctEventNames()

        return self.getDistinctValues(keyPressEventNames, multiExcludeEventNames, multiInludeEventNames, tsharkEventNames, screenshotEventNames)

    def getDistinctTechAndEventNames(self):
        keyPressPlugin = ConfigReader().getInstanceOfDatasourcePlugin("PyKeyPress")
        multiExcludePlugin = ConfigReader().getInstanceOfDatasourcePlugin("MultiExcludeThroughput")
        multiIncludePlugin = ConfigReader().getInstanceOfDatasourcePlugin("MultiIncludeThroughput")
        tsharkPlugin = ConfigReader().getInstanceOfDatasourcePlugin("TsharkThroughput")
        screenshotPlugin = ConfigReader().getInstanceOfDatasourcePlugin("ManualScreenShot")

        keyPressEventNames = keyPressPlugin.getDistinctTechAndEventNames()
        multiExcludeEventNames = multiExcludePlugin.getDistinctTechAndEventNames()
        multiInludeEventNames = multiIncludePlugin.getDistinctTechAndEventNames()
        tsharkEventNames = tsharkPlugin.getDistinctTechAndEventNames()
        screenshotEventNames = screenshotPlugin.getDistinctTechAndEventNames()

        return self.getDistinctValues(keyPressEventNames, multiExcludeEventNames, multiInludeEventNames, tsharkEventNames, screenshotEventNames)

    def getDistinctValues(self, keyPressNames, multiExcludeNames, multiInludeNames, tsharkNames, screenshotNames):
        distinctNames = keyPressNames

        for name in multiExcludeNames:
            if name not in distinctNames:
                distinctNames.append(name)
        for name in multiInludeNames:
            if name not in distinctNames:
                distinctNames.append(name)
        for name in tsharkNames:
            if name not in distinctNames:
                distinctNames.append(name)
        for name in screenshotNames:
            if name not in distinctNames:
                distinctNames.append(name)

        return distinctNames
