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

from core.apis.renderer.pluginChecker import PluginChecker
from core.config.configRenderers import ConfigRenderers
from core.config.configDatasources import ConfigDatasources

class PluginImporter:

    def __init__(self, path):
        checker = PluginChecker(path)
        self.notInstalled = checker.getUninstalledPlugins()
        self.type = checker.getPluginType()
    #the parent directory and the plugin(.js) must have the same name
    #  ..ie viz/viz.js


    def importPlugin(self,plugin):
        fileExtension = "" 
        directory = self.type
        directory = directory.replace("/",".")

        if self.type == "renderer/":
            fileExtension = ".js"

        if plugin in self.notInstalled:
                location = "plugins." + directory + plugin
                if self.type == "renderer/":
                    ConfigRenderers().addRenderer(plugin + fileExtension,location)
                else:
                    ConfigDatasources().addDatasource(plugin + fileExtension,location)
                self.notInstalled.remove(plugin)
                return True;

        return False;


    def getUninstalledPlugins(self):
        return self.notInstalled
