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
