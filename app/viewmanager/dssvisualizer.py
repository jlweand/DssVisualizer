#  Copyright (C) 2016  Jamie Acosta, Jennifer Weand, Juan Soto, Mark Eby, Mark Smith, Andres Olivas
#
# This file is part of DssVisualizer.
#
# DssVisualizer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DssVisualizer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DssVisualizer.  If not, see <http://www.gnu.org/licenses/>.

import gi
import os
import ujson
from urllib.parse import parse_qs
from datetime import datetime

# Only use files from core.  DO NOT use files from plugins.
from core.apis.renderer.generateHtml import GenerateHtml
from core.apis.datasource.pyClick import PyClick
from core.apis.datasource.pyKeyPress import PyKeyPress
from core.apis.datasource.pyTimed import PyTimed
from core.apis.renderer.pluginImporter import PluginImporter
from core.config.configDatasources import ConfigDatasources
from core.config.configRenderers import ConfigRenderers
from core.config.dataImport import DataImport
from viewmanager.exportPopup import ExportPopup
from core.apis.datasource.multiExcludeThroughput import MultiExcludeThroughput
from core.apis.datasource.multiIncludeThroughput import MultiIncludeThroughput
from core.apis.datasource.tsharkThroughput import TsharkThroughput
from core.apis.datasource.multiExcludeProtocol import MultiExcludeProtocol
from core.apis.datasource.multiIncludeProtocol import MultiIncludeProtocol
from core.apis.datasource.tsharkProtocol import TsharkProtocol
from core.apis.datasource.manualScreenShot import ManualScreenShot
from core.apis.datasource.techAndEventNames import TechAndEventNames
from viewmanager.folderExplorer import FolderExplorer

gi.require_version("Gtk", "3.0")
gi.require_version("WebKit", "3.0")
from gi.repository import Gtk
from gi.repository import WebKit
from time import gmtime, strftime

def handle(web_view, web_frame, web_resource, request, response):
    ##'query' contains the data sent from the jquery.get method

    query = request.get_message().get_uri().get_query()
    _uri = request.get_uri()

    if 'installDatasources' in _uri or 'adminset' in _uri:
        load_uninstalled_plugins(query, "datasource")

    if 'installRends' in _uri or 'adminset' in _uri:
        load_uninstalled_plugins(query, "renderer")

    if 'importData' in _uri:
        importInfo = parse_qs(query)
        techI = importInfo['tech'][0]
        locationI = importInfo['location'][0]
        commentI = importInfo['comment'][0]
        eventI = importInfo['event'][0]

        copyImagesI = False
        if 'copyImages' in importInfo:
            copyImagesI = True

        if 'date' in importInfo:
            dateI = importInfo['date'][0]
        else:
            dateI = strftime("%Y-%m-%d %H:%M:%S")

        importer = DataImport()
        importer.importAllDataFromFiles(locationI, techI, eventI, commentI, dateI, copyImagesI)
        setLabel = "$('#importedData').html('Data imported!');"
        webKitWebView.execute_script(setLabel)

    if 'exportData' in _uri:
        if query:
            exportInfo = parse_qs(query)
            ExportPopup(exportInfo)

    if 'explore' in _uri:

        ## get string path for folder from Explorer GUI
        folderPathPy = FolderExplorer(Gtk.Window()).findFolder()

        if folderPathPy != None:
            folderPathHTML = list(folderPathPy)

            ## replace backslashes with forwardslashes so html doesn't complain
            ## ...and so user can see string version of selected folder path
            for i,char in enumerate(folderPathHTML):
                if char == '\\':
                    folderPathHTML[i] = '/'
            ##for linux
            folderPathHTML.append('/')
            folderPathHTML = ''.join(folderPathHTML)
            folderChange = "document.getElementById('chosenFolder').setAttribute('value','"+folderPathHTML+"');"
            webKitWebView.execute_script(folderChange)




    if not query:
        return
    else:
        queryDict = parse_qs(query)
        if 'request' in queryDict:
            startDate = queryDict['startDate'][0]
            endDate = queryDict['endDate'][0]
            try:
                techNames = queryDict['techNames']
                techList = techNames[0].split(",")
            except KeyError:
                techList = []
            try:
                eventNames = queryDict['eventNames']
                eventList = eventNames[0].split(",")
            except KeyError:
                eventList = []
            try:
                eventTechNames = queryDict['eventTechNames']
                eventTechList = eventTechNames[0].split(",")
            except KeyError:
                eventTechList = []

            if queryDict['request'][0] == 'keypressData':
                print("keypressData before getting data: " + strftime("%Y-%m-%d %H:%M:%S"))
                start1 = datetime.now()
                keyData = PyKeyPress().selectKeyPressData(startDate, endDate, techList, eventList, eventTechList)
                clickData = PyClick().selectClickData(startDate, endDate, techList, eventList, eventTechList)
                timedData = PyTimed().selectTimedData(startDate, endDate, techList, eventList, eventTechList)
                print("keypressData before visualizeKeyData: " + strftime("%Y-%m-%d %H:%M:%S"))
                start2 = datetime.now()
                js = "visualizeKeyData(%s, %s, %s);" % (keyData, clickData, timedData)
                webKitWebView.execute_script(js)
                print("keypressData after visualizeKeyData: " + strftime("%Y-%m-%d %H:%M:%S"))
                end = datetime.now()

                data = start2 - start1
                ui = end - start2
                total = end - start1
                print("keypressData data : " + str(data))
                print("keypressData ui   : " + str(ui))
                print("keypressData total: " + str(total))

            elif queryDict['request'][0] == 'pcapData':
                print("pcapData before getting data: " + strftime("%Y-%m-%d %H:%M:%S"))
                start1 = datetime.now()
                multiEx = MultiExcludeThroughput().selectMultiExcludeThroughputData(startDate, endDate, techList, eventList, eventTechList)
                multiInc = MultiIncludeThroughput().selectMultiIncludeThroughputData(startDate, endDate, techList, eventList, eventTechList)
                tshark = TsharkThroughput().selectTsharkThroughputData(startDate, endDate, techList, eventList, eventTechList)
                multiExProt = MultiExcludeProtocol().selectMultiExcludeProtocolData(startDate, endDate, techList, eventList, eventTechList)
                multiIncProt = MultiIncludeProtocol().selectMultiIncludeProtocolData(startDate, endDate, techList, eventList, eventTechList)
                tsharkProt = TsharkProtocol().selectTsharkProtocolData(startDate, endDate, techList, eventList, eventTechList)
                js = "visualizePCAPData(%s, %s, %s, %s, %s, %s);" % (
                    multiEx, multiExProt, multiInc, multiIncProt, tshark, tsharkProt)
                print("pcapData before visualizeKeyData: " + strftime("%Y-%m-%d %H:%M:%S"))
                start2 = datetime.now()
                webKitWebView.execute_script(js)
                print("pcapData after visualizeKeyData: " + strftime("%Y-%m-%d %H:%M:%S"))
                end = datetime.now()

                data = start2 - start1
                ui = end - start2
                total = end - start1
                print("pcapData data : " + str(data))
                print("pcapData ui   : " + str(ui))
                print("pcapData total: " + str(total))

            elif queryDict['request'][0] == 'screenshotData':
                print("screenshotData before getting data: " + strftime("%Y-%m-%d %H:%M:%S"))
                start1 = datetime.now()
                snap = ManualScreenShot().selectManualScreenShotData(startDate, endDate, techList, eventList, eventTechList)
                print("screenshotData before visualizeKeyData: " + strftime("%Y-%m-%d %H:%M:%S"))
                start2 = datetime.now()
                js = "visualizeSnapshotData(%s);" % (snap)
                webKitWebView.execute_script(js)
                print("screenshotData after visualizeKeyData: " + strftime("%Y-%m-%d %H:%M:%S"))
                end = datetime.now()

                data = start2 - start1
                ui = end - start2
                total = end - start1
                print("screenshotData data : " + str(data))
                print("screenshotData ui   : " + str(ui))
                print("screenshotData total: " + str(total))

        elif 'submission' in queryDict:
            if queryDict['submission'][0] == 'annotation':
                print("trying to submit"+query)
                itemID = queryDict['itemID'][0]
                itemType = queryDict['type'][0]
                annotation = queryDict['annotation'][0]
                eventName = queryDict['eventName'][0]
                techName = queryDict['techName'][0]
                start = queryDict['start'][0]
                if itemType == 'keypress':
                    PyKeyPress().addAnnotationToKeyPressTimeline(start, annotation, techName, eventName)
                elif itemType == 'click':
                    PyClick().addAnnotationToClickTimeline(start, annotation, techName, eventName)
                elif itemType == 'timed':
                    PyTimed().addAnnotationToTimedTimeline(start, annotation, techName, eventName)
                elif itemType == 'multi_exclude':
                    MultiExcludeProtocol().addAnnotationToMultiExcludeProtocolTimeline(start, annotation, techName, eventName)
                elif itemType == 'multi_include':
                    MultiIncludeProtocol().addAnnotationToMultiIncludeProtocolTimeline(start, annotation, techName, eventName)
                elif itemType == 'tshark':
                    TsharkProtocol().addAnnotationToTsharkProtocolTimeline(start, annotation, techName, eventName)
                elif itemType == 'screenshot':
                    ManualScreenShot().addAnnotationToManualScreenShotTimeline(start, annotation, techName, eventName)
            if queryDict['submission'][0] == 'edit':
                print("trying to submit"+query)
                itemID = queryDict['itemID'][0]
                itemType = queryDict['type'][0]
                editType = queryDict['editType'][0]  #delete for delete, edit for edit
                start = queryDict['start'][0]
                try:
                    className = queryDict['className'][0]
                except KeyError:
                    className = ''
                try:
                    content = queryDict['content'][0]
                except KeyError:
                    content = ''
                try:
                    title = queryDict['title'][0]
                except KeyError:
                    title = ''
                try:
                    annotation = queryDict['annotation'][0]
                except KeyError:
                    annotation = ''
                try:
                    comment = queryDict['comment'][0]
                except KeyError:
                    comment = ''
                try:
                    dataType = queryDict['dataType'][0]
                except KeyError:
                    dataType = ''

                if editType == 'delete':
                    delete = True
                else:
                    delete = ''

                if itemType == 'keypress':
                    if annotation != '':
                        PyKeyPress().addAnnotationKeyPress(itemID, annotation)
                    PyKeyPress().insertFixedKeyPressData(itemID, className, content, dataType, start, delete)
                elif itemType == 'click':
                    if annotation != '':
                        PyClick().addAnnotationClick(itemID, annotation)
                    PyClick().insertFixedClickData(itemID, '', content, className, start, title, dataType, delete)
                elif itemType == 'timed':
                    if annotation != '':
                        PyTimed().addAnnotationTimed(itemID, annotation)
                    PyTimed().insertFixedTimedData(itemID, '', content, className, start, title, dataType, delete)
                elif itemType == 'multi_exclude':
                    if annotation != '':
                        MultiExcludeProtocol().addAnnotationMultiExcludeProtocol(itemID, annotation)
                    MultiExcludeProtocol().insertFixedMultiExcludeProtocolData(itemID, '', content, className, title, start, delete)
                elif itemType == 'multi_include':
                    if annotation != '':
                        MultiIncludeProtocol().addAnnotationMultiIncludeProtocol(itemID, annotation)
                    MultiIncludeProtocol().insertFixedMultiIncludeProtocolData(itemID, '', content, className, title, start, delete)
                elif itemType == 'tshark':
                    if annotation != '':
                        TsharkProtocol().addAnnotationTsharkProtocol(itemID, annotation)
                    TsharkProtocol().insertFixedTsharkProtocolData(itemID, '', content, className, title, start, delete)
                elif itemType == 'screenshot':
                    if annotation != '':
                        ManualScreenShot().addAnnotationManualScreenShot(itemID, annotation)
                    ManualScreenShot().insertFixedManualScreenShotData(itemID, '', content, className, start, title, dataType, comment, delete)

        elif 'adminRequest' in queryDict:
            if queryDict['adminRequest'][0] == 'availablePlugins':
                load_available_renderers()
        elif 'adminSubmission' in queryDict:
            if queryDict['adminSubmission'][0] == 'pluginChanges':
                database = queryDict['database'][0]
                pcap = queryDict['pcap'][0]
                pyKeyLogger = queryDict['pyKeyLogger'][0]
                screenshots = queryDict['screenshots'][0]
                ConfigDatasources().setDefaultDatasource(database)
                ConfigRenderers().setDefaultRenderer("pcap", pcap)
                ConfigRenderers().setDefaultRenderer("pyKeyLogger", pyKeyLogger)
                ConfigRenderers().setDefaultRenderer("screenshots", screenshots)

        elif 'populateDropdown' in queryDict:
            if queryDict['populateDropdown'][0] == 'availableTechNames':
                try:
                    eventTechNames = queryDict['eventNames']
                    eventTechList = eventTechNames[0].split(",")
                except KeyError:
                    eventTechList = []

                techList = TechAndEventNames().getDistinctTechNamesForEvents(eventTechList)
                js = "populateTechDropdown(%s)" % techList
                webKitWebView.execute_script(js)

            elif queryDict['populateDropdown'][0] == 'availableEventNames':
                eventList = TechAndEventNames().getDistinctEventNames()
                js = "populateEventDropdown(%s)" % eventList
                webKitWebView.execute_script(js)

            elif queryDict['populateDropdown'][0] == 'availableTechAndEventNames':
                techEventList = TechAndEventNames().getDistinctTechAndEventNames()
                js = "populateTechAndEventDropdown(%s)" % techEventList
                webKitWebView.execute_script(js)
    return


def getJson(file):
    with open(file) as json_data:
        d = ujson.load(json_data)
        return d


def load_available_renderers():
    jsonFile = getJson("core/config/config.json")
    allFile = ujson.dumps(jsonFile)
    js = "createRadioButtons(%s)" % allFile
    webKitWebView.execute_script(js)


def load_uninstalled_plugins(query, _type):
    folder = "plugins/renderer/"
    tagID = "installRends"
    if _type is "datasource":
        folder = "plugins/datasource/"
        tagID = "installDatasources"

    importer = PluginImporter(folder)  # diff
    newPlugins = importer.getUninstalledPlugins()
    if not query:
        for plugin in newPlugins:
            if "__" not in plugin:
                modify_uninstalled_plugin_html(plugin, tagID)
    else:
        importer.importPlugin(query)
        script = 'document.getElementById("' + tagID + '").innerHTML = "";'  # diff
        webKitWebView.execute_script(script)
        load_uninstalled_plugins(None, _type)


def modify_uninstalled_plugin_html(plugin, tagID):
    if plugin:
        script = 'var element = document.createElement("option");'
        script = script + 'element.innerHTML = "' + plugin + '";'
        script = script + 'document.getElementById("' + tagID + '").appendChild(element);'
    else:
        script = 'document.getElementById("' + tagID + '").innerHTML = "";'
    webKitWebView.execute_script(script)


gtkWindow = Gtk.Window()
webKitWebView = WebKit.WebView()
gtkScrolledWindow = Gtk.ScrolledWindow()
gtkScrolledWindow.add(webKitWebView)
gtkWindow.add(gtkScrolledWindow)
gtkWindow.connect("delete-event", Gtk.main_quit)

gtkWindow.set_default_size(1200, 1000)

# generate the index.html page based on the renderer plugin
GenerateHtml().generateHtml()
uri = "file:///" + os.getcwd() + "/viewmanager/index.html"

webKitWebView.load_uri(uri)
webKitWebView.connect("resource-request-starting", handle)

gtkWindow.show_all()
Gtk.main()

# python -m viewmanager.dssvisualizer
