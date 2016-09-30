import ujson
from pprint import pprint

class ConfigReader:

    def getListOfDatasources(self):
        config = self.importConfigJson()
        return config["datasourcePlugins"]

    def getListOfRenderers(self):
        config = self.importConfigJson()
        return config["rendererPlugins"]

    def importConfigJson(self):
        with open('core/config/config.json', 'r') as configFile:
            jsonStr = configFile.read()
            config = ujson.loads(jsonStr)
        return config

    def getDatasourcePluginLocation(self):
        config = self.importConfigJson();
        activePlugin = config["activeDatasourcePlugin"]
        for plugin in self.getListOfDatasources():
            if plugin["name"] == activePlugin:
                return plugin["location"] + "."
        return "No Datasource found";

    def getRendererPluginLocation(self):
        config = self.importConfigJson();
        activePlugin = config["activeRendererPlugin"]
        for plugin in self.getListOfRenderers():
            if plugin["name"] == activePlugin:
                return plugin["location"] + "."
        return "No Renderer found";

    def getInstanceOfDatasourcePlugin(self, classname):
        return self.getInstanceOfPlugin(classname, True)

    def getInstanceOfRendererPlugin(self, classname):
        return self.getInstanceOfPlugin(classname, False)

    def getInstanceOfPlugin(self, classname, isDatasource):
        # get this information from the config.json
        if(isDatasource):
            module = self.getDatasourcePluginLocation()
        else:
            module = self.getRendererPluginLocation()

        module = module + classname[0].lower() + classname[1:]

        #import the module by saying 'from myApp.models import Blog'
        module = __import__(module, {}, {}, classname)

        #now you can instantiate the class
        obj = getattr(module, classname )()
        return obj
