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
from core.apis.renderer.pluginReader import PluginReader

class PluginChecker:


    def __init__(self, path):
        self.path = path
        self.setPluginType()#10/3/16
        self.readConfigPlugins()
        self.readPluginFolder()
        self.checkInstalls()

    def setPluginType(self):
        positionOfSlash = len("plugins/")#10/3/16
        self.pluginType = self.path[positionOfSlash:]#10/3/16
        #print (directory)#10/3/16

    def getPluginType(self):

        return self.pluginType

    def readConfigPlugins(self):
        configList = ConfigReader().getListOfDatasources()#10/3/16
        if self.pluginType == "renderer/":#10/3/16
            configList = ConfigReader().getListOfRenderers()#10/3/16

        self.installedList = list()
        for plugin in configList:
            plugin = plugin['location']

            positionOfSlash = plugin.rfind('.') #10/3/16

            directory = plugin[positionOfSlash+1:]#10/3/16

            self.installedList.append(directory)



    def readPluginFolder(self):
        folderReader = PluginReader(self.path)
        self.pluginList = folderReader.getPlugins()


    def checkInstalls(self):
        self.notInstalled = list()
        for plugin in self.pluginList:
            if plugin not in self.installedList:
                self.notInstalled.append(plugin)


    def getUninstalledPlugins(self):
        return self.notInstalled
