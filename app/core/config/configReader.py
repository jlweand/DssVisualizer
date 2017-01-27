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

class ConfigReader:
    def getListOfDatasources(self):
        """ returns a list of installed data sources

        :return: list of data sources
        """
        config = self.importConfigJson()
        return config["datasourcePlugins"]

    def getListOfRenderers(self):
        """ returns a list of installed data renderers

        :return: list of data renderers
        """
        config = self.importConfigJson()
        return config["rendererPlugins"]

    def importConfigJson(self):
        """ Reads the confg.json file into memory

        :return: object dict
        """
        with open('core/config/config.json', 'r') as configFile:
            jsonStr = configFile.read()
            config = ujson.loads(jsonStr)
        return config

    def getDatasourcePluginLocation(self):
        """ Gets the locations of the active data source plugin

        :return: relative path to the active data source plugin
            """
        config = self.importConfigJson()
        activePlugin = config["activeDatasourcePlugin"]
        for plugin in self.getListOfDatasources():
            if plugin["name"] == activePlugin:
                return plugin["location"] + "."
        return "No Datasource found"

    def getRedererPluginForPyKeyLogger(self):
        """ Gets the locations of the active keyLogger renderer plugin

        :return: relative path to the active keyLogger renderer plugin
        """
        return self.getRendererPlugin("pyKeyLogger")
	
    def getRendererPluginForSnoopy(self):
        """ Gets the locations of the active snoopy renderer plugin

        :return: relative path to the active snoopy renderer plugin
        """
        return self.getRendererPlugin("snoopy")
        

    def getRedererPluginForPcap(self):
        """ Gets the locations of the active Pcap renderer plugin

        :return: relative path to the active Pcap renderer plugin
        """
        return self.getRendererPlugin("pcap")
        

    def getRedererPluginForScreenshots(self):
        """ Gets the locations of the active Screenshots renderer plugin

        :return: relative path to the active Screenshots renderer plugin
        """
        return self.getRendererPlugin("screenshots")

    def getRendererPlugin(self, datatype):
        """ Returns the location of the specified plugin

        :param datatype: The name of the plugin to get the location of.
        :type datatype: str
        :return: relative path to the plugin
        """
        config = self.importConfigJson()
        activePlugins = config["activeRendererPlugins"]
        activePlugin = activePlugins[datatype]
        for plugin in self.getListOfRenderers():
            if plugin["name"] == activePlugin["plugin"]:
                return activePlugin["location"].replace('.', '/') + "/"
        return "No Renderer found"

    def getDistinctListOfActiveRenderers(self):
        config = self.importConfigJson()
        activePlugins = config["activeRendererPlugins"]
        distinctRends = []
        if activePlugins["pcap"]["plugin"] not in distinctRends:
            distinctRends.append(activePlugins["pcap"]["plugin"])
        if activePlugins["pyKeyLogger"]["plugin"] not in distinctRends:
            distinctRends.append(activePlugins["pyKeyLogger"]["plugin"])
        if activePlugins["screenshots"]["plugin"] not in distinctRends:
            distinctRends.append(activePlugins["screenshots"]["plugin"])
        if activePlugins["snoopy"]["plugin"] not in distinctRends:
            distinctRends.append(activePlugins["snoopy"]["plugin"])

        return distinctRends

    def getInstanceOfDatasourcePlugin(self, classname):
        """ Returns an instance of the class of the active data source plugin. This is used to call the methods inside the class.

        :param classname: The name of the class you need an instance of
        :type classname: str
        :return: an instance of the data source class
        """
        return self.getInstanceOfPlugin(classname, True)

    def getInstanceOfRendererPlugin(self, classname):
        """ Returns an instance of the class of the active renderer plugin. This is used to call the methods inside the class.

        :param classname: The name of the class you need an instance of
        :type classname: str
        :return: an instance of the renderer class
        """
        return self.getInstanceOfPlugin(classname, False)

    def getInstanceOfPlugin(self, classname, isDatasource):
        """ Returns an instance of a class of an active plugin. This is used to call the methods inside the class.
        This imports the module by saying 'from myApp.models import Blog'

        :param classname: The name of the class you need an instance of
        :type classname: str
        :param isDatasource: Flag to treat the class as a renderer or datasource.
        :type isDatasource: bool
        :return: an instance of the class
        """
        # get this information from the config.json
        if (isDatasource):
            module = self.getDatasourcePluginLocation()
        else:
            module = self.getRendererPluginLocation()

        module = module + classname[0].lower() + classname[1:]

        # import the module by saying 'from myApp.models import Blog'
        module = __import__(module, {}, {}, classname)

        # now you can instantiate the class
        obj = getattr(module, classname)()
        return obj
