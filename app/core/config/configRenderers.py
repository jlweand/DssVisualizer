import ujson
import json
from pprint import pprint

class ConfigRenderers:

    def importConfigJson(self):
        with open('core/config/config.json', 'r') as configFile:
            jsonStr = configFile.read()
            config = ujson.loads(jsonStr)
        return config

    def writeToConfigJson(self, config):
        with open('core/config/config.json', 'w') as configFile:
            json.dump(config, configFile, sort_keys = True, indent = 2, ensure_ascii=False)

    def addRenderer(self, name, location):
        config = self.importConfigJson()
        rendererPlugins = config["rendererPlugins"]

        # check to make sure we don't have a renderer with this name already
        for rend in rendererPlugins:
            if rend["name"].lower() == name.lower():
                return "Duplicate renderer name. Unable to add this renderer plugin."

        renderer = {}
        renderer["name"] = name
        renderer["location"] = location

        rendererPlugins.append(renderer)
        self.writeToConfigJson(config)
        return name

    def removeRenderer(self, name):
        config = self.importConfigJson()
        defaultPlugins = config["activeRendererPlugins"]

        # can't delete if it is the default plugin
        for rend in defaultPlugins:
            if defaultPlugins[rend]["plugin"].lower() == name.lower():
                return "Sorry, this plugin cannot be deleted. It is currently in use. Please choose another default plugin before deleting this one."

        # now try to find the renderer and delete it
        rendererPlugins = config["rendererPlugins"]
        for i, rend in enumerate(rendererPlugins):
            if rend["name"].lower() == name.lower():
                rendererPlugins.pop(i)
                self.writeToConfigJson(config)
                return name

        return "Failed to find renderer plugin named " + name

    def setDefaultRenderer(self, pluginDataType, defaultPluginName, scriptFile):
        config = self.importConfigJson()
        rendererPlugins = config["rendererPlugins"]

        # check to make sure we have this plugin
        for rend in rendererPlugins:
            if rend["name"].lower() == defaultPluginName.lower():
                activePlugins = config["activeRendererPlugins"]
                activePlugin = activePlugins[pluginDataType]

                activePlugin["location"] = rend["location"]
                activePlugin["plugin"] = defaultPluginName
                activePlugin["scripts"] = scriptFile
                self.writeToConfigJson(config)
                return defaultPluginName

        return "No renderer plugin has been imported for " + defaultPluginName
