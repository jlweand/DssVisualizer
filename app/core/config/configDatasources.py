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
import json


class ConfigDatasources:
    def importConfigJson(self):
        with open('core/config/config.json', 'r') as configFile:
            jsonStr = configFile.read()
            config = ujson.loads(jsonStr)
        return config

    def writeToConfigJson(self, config):
        with open('core/config/config.json', 'w') as configFile:
            json.dump(config, configFile, sort_keys=True, indent=2, ensure_ascii=False)

    def addDatasource(self, name, location):
        config = self.importConfigJson()
        datasourcePlugins = config["datasourcePlugins"]

        # check to make sure we don't have a datasource with this name already
        for ds in datasourcePlugins:
            if ds["name"].lower() == name.lower():
                return "Duplicate datasource name. Unable to add this datasource plugin."

        datasource = {}
        datasource["name"] = name
        datasource["location"] = location

        datasourcePlugins.append(datasource)
        self.writeToConfigJson(config)
        return name

    def removeDatasource(self, name):
        config = self.importConfigJson()
        defaultPlugin = config["activeDatasourcePlugin"]

        # can't delete if it is the default plugin
        if name.lower() == defaultPlugin.lower():
            return "Sorry, this plugin cannot be deleted. It is currently in use. Please choose another default plugin before deleting this one."

        # now try to find the datasource and delete it
        datasourcePlugins = config["datasourcePlugins"]
        for i, ds in enumerate(datasourcePlugins):
            if ds["name"].lower() == name.lower():
                datasourcePlugins.pop(i)
                self.writeToConfigJson(config)
                return name

        return "Failed to find datasource plugin named " + name

    def setDefaultDatasource(self, name):
        config = self.importConfigJson()
        datasourcePlugins = config["datasourcePlugins"]

        # check to make sure we have this plugin
        for ds in datasourcePlugins:
            if ds["name"].lower() == name.lower():
                config["activeDatasourcePlugin"] = name
                self.writeToConfigJson(config)
                return name

        return "No datasource plugin has been imported for " + name
