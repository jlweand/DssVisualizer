from core.apis.renderer.pluginChecker import PluginChecker
from core.config.configRenderers import ConfigRenderers
from core.config.configDatasources import ConfigDatasources

class PluginImporter:

    def __init__(self, path):
        checker = PluginChecker(path)#10/13/16
        self.notInstalled = checker.getUninstalledPlugins()#10/13/16
        self.type = checker.getPluginType()#10/13/16
    #the parent directory and the plugin(.js) must have the same name
    #  ..ie viz/viz.js


    def importPlugin(self,plugin):
        fileExtension = "" #10/13/16
        directory = self.type#10/13/16
        directory = directory.replace("/",".")#10/13/16

        if self.type == "renderer/":#10/13/16
            fileExtension = ".js"#10/13/16

        if plugin in self.notInstalled:
                location = "plugins." + directory + plugin
                if self.type == "renderer/":
                    ConfigRenderers().addRenderer(plugin + fileExtension,location)
                else:
                    ConfigDatasources().addDatasource(plugin + fileExtension,location)
                self.notInstalled.remove(plugin)
                return True;

        return False;


    def getUninstalledPlugins(self):
        return self.notInstalled
