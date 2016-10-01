import os.path
from core.config.configReader import ConfigReader
from core.config.configDatasources import ConfigDatasources


class importDataSource:
    #searches data sources folder, creates a list with files inside and prints it to console
    def searchDSPlugins(self):
        path ="plugins/datasource/"
        dirs = os.listdir(path)
        pluginList = list()
        print ("Plugins in Folder")
        for folder in dirs:
            pluginList.append(folder.lower())
        for i in pluginList:
            print (i)

        #Need to get the list of already installed plugins from getListOfDatasources and compare to pluginLIst
        configList = (ConfigReader().getListOfDatasources())
        installedList= list()
        print ("\nInstalled plugins")
        for plugin in configList:
            plugin= plugin['name']
            installedList.append(plugin.lower())
        for i in installedList:
            print (i)

        #compare both lists
        newPluginList= list()
        for pluginName in pluginList:
            if pluginName in installedList:
                print ("No new plugins to install")
            else:
                name= pluginName
                location = "plugins.datasource."+pluginName
                newPluginList.append(pluginName)
                ConfigDatasources().addDatasource(name,location) # trying to use the addDatasource method from congifDatasources file to update config.json. Maybe Im using the parameters wrong
        for plugin in newPluginList:
            print ("\n"+i)
        return newPluginList


a= importDataSource()
a.searchDSPlugins()
