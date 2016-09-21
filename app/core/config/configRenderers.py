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
        defaultPlugin = config["activeRendererPlugin"]

        # can't delete if it is the default plugin
        if(name.lower() == defaultPlugin.lower()):
            return "Sorry, this plugin cannot be deleted. It is currently in use. Please choose another default plugin before deleting this one."

        # now try to find the renderer and delete it
        rendererPlugins = config["rendererPlugins"]
        for i, rend in enumerate(rendererPlugins):
            if rend["name"].lower() == name.lower():
                rendererPlugins.pop(i)
                self.writeToConfigJson(config)
                return name

        return "Failed to find renderer plugin named " + name

    def getListOfRenderers(self):
        config = self.importConfigJson()
        return config["rendererPlugins"]

    def setDefaultRenderer(self, name):
        config = self.importConfigJson()
        rendererPlugins = config["rendererPlugins"]

        # check to make sure we have this plugin
        for ds in rendererPlugins:
            if ds["name"].lower() == name.lower():
                config["activeRendererPlugin"] = name
                self.writeToConfigJson(config)
                return name

        return "No renderer plugin has been imported for " + name
