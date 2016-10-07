from core.config.configReader import ConfigReader
from core.apis.renderer.datasourceReader import DatasourceReader

class DatasourceChecker:

    #create the path object adn attributes
    def __init__(self, path):
        self.path = path
        self.readConfigPlugins()
        self.readPluginFolder()
        self.checkInstalls()


    def readConfigPlugins(self):
        configList = ConfigReader().getListOfDatasources()
        self.installedList = list()
        for plugin in configList:
            plugin = plugin['location']
            directory = plugin[19:]

            self.installedList.append(directory)


    def readPluginFolder(self):
        folderReader = DatasourceReader(self.path)
        self.pluginList = folderReader.getPlugins()


    def checkInstalls(self):
        self.notInstalled = list()
        for plugin in self.pluginList:
            if plugin not in self.installedList:
                self.notInstalled.append(plugin)


    def getUninstalledPlugins(self):
        return self.notInstalled
