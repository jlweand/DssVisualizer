from core.config.configReader import ConfigReader
from core.apis.renderer.rendererReader import RendererReader

class RendererChecker:


    def __init__(self, path):
        self.path = path
        self.readConfigPlugins()
        self.readPluginFolder()
        self.checkInstalls()

    def readConfigPlugins(self):
        configList = ConfigReader().getListOfRenderers()
        self.installedList = list()
        for plugin in configList:
            plugin = plugin['location']
            directory = plugin[17:]

            self.installedList.append(directory)



    def readPluginFolder(self):
        folderReader = RendererReader(self.path)
        self.pluginList = folderReader.getPlugins()


    def checkInstalls(self):
        self.notInstalled = list()
        for plugin in self.pluginList:
            if plugin not in self.installedList:
                self.notInstalled.append(plugin)


    def getUninstalledPlugins(self):
        return self.notInstalled
