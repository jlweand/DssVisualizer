import os

class PluginReader:
    #construct a PluginReader object
    def __init__(self, path):
        self.path = path
        self.collectPlugins()

    def collectPlugins(self):
        for root,dir,file in os.walk(self.path):
            self.plugins = dir
            break

    def getPlugins(self):

        return self.plugins
