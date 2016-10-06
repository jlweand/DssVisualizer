import os.path
from core.config.configReader import ConfigReader
from core.config.configDatasources import ConfigDatasources
from core.apis.renderer.datasourceChecker import DatasourceChecker



class ImportDataSource:

    def __init__(self):
        self.notInstalled = DatasourceChecker("plugins/datasource/").getUninstalledPlugins()

    #the parent directory and the plugin(.js) must have the same name
    #  ..ie viz/viz.js
    def importPlugin(self,plugin):
        if plugin in self.notInstalled:
                location = "plugins.datasource." + plugin
                ConfigDatasources().addDatasource(plugin,location)
                self.notInstalled.remove(plugin)
                return True;

        return False;

    def getUninstalledPlugins(self):
        return self.notInstalled
