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
from core.apis.renderer.pluginImporter import PluginImporter


class Plugins:
    """This class has all the methods that the admin.html needs for the install plugin and activate plugin tabs"""

    def load_uninstalled_plugins(self, query, _type):
        """Generate all the javascript to create the list of plugins that have not been installed already.

        :param query: the query from the webkit
        :type query: str
        :param _type: indicates whether to work with data source or renderer plugins
        :type _type: str
        :return: javascript to be executed
        """
        folder = "plugins/renderer/"
        tagID = "installRends"
        if _type is "datasource":
            folder = "plugins/datasource/"
            tagID = "installDatasources"

        importer = PluginImporter(folder)  # diff
        newPlugins = importer.getUninstalledPlugins()
        if not query:
            for plugin in newPlugins:
                if "__" not in plugin:
                    return self.modify_uninstalled_plugin_html(plugin, tagID)
        else:
            importer.importPlugin(query)
            script = 'document.getElementById("' + tagID + '").innerHTML = "";'  # diff
            self.load_uninstalled_plugins(None, _type)
            return script

    def modify_uninstalled_plugin_html(self, plugin, tagID):
        """Generate the javascript for the plugin"""
        if plugin:
            script = 'var element = document.createElement("option");'
            script = script + 'element.innerHTML = "' + plugin + '";'
            script = script + 'document.getElementById("' + tagID + '").appendChild(element);'
        else:
            script = 'document.getElementById("' + tagID + '").innerHTML = "";'

        return script

    def load_available_renderers(self):
        """Get a list of available renderer plugins"""
        jsonFile = self.getJson("core/config/config.json")
        allFile = ujson.dumps(jsonFile)
        js = "createRadioButtons(%s)" % allFile
        return js

    def getJson(self, file):
        with open(file) as json_data:
            d = ujson.load(json_data)
            return d
