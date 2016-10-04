from core.apis.renderer.rendererChecker import RendererChecker
from core.config.configRenderers import ConfigRenderers

class ImportRenderer:

    def __init__(self):
        self.notInstalled = RendererChecker("plugins/renderer/").getUninstalledPlugins()

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
