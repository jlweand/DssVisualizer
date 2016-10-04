from core.apis.renderer.pluginChecker import PluginChecker
from core.config.configRenderers import ConfigRenderers

class ImportPlugin:

    def __init__(self):
        self.notInstalled = PluginChecker("plugins/renderer/").getUninstalledPlugins()

    #the parent directory and the plugin(.js) must have the same name
    #  ..ie viz/viz.js
    def importPlugin(self,plugin):
        if plugin in self.notInstalled:
                location = "plugins.renderer." + plugin
                ConfigRenderers().addRenderer(plugin+".js",location)
                self.notInstalled.remove(plugin)
                return True;

        return False;

    def getUninstalledPlugins(self):
        return self.notInstalled
