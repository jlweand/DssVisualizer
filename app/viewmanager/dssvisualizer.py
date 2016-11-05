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

# Only use files from core.  DO NOT use files from plugins.
from core.apis.renderer.generateHtml import GenerateHtml
from core.apis.datasource.pyClick import PyClick
from core.apis.datasource.pyKeyPress import PyKeyPress
from core.apis.datasource.pyTimed import PyTimed
from core.apis.renderer.pluginImporter import PluginImporter
from core.config.configDatasources import ConfigDatasources
from core.config.configRenderers import ConfigRenderers
from core.apis.datasource.multiExcludeThroughput import MultiExcludeThroughput
from core.apis.datasource.multiIncludeThroughput import MultiIncludeThroughput
from core.apis.datasource.tsharkThroughput import TsharkThroughput
from core.apis.datasource.multiExcludeProtocol import MultiExcludeProtocol
from core.apis.datasource.multiIncludeProtocol import MultiIncludeProtocol
from core.apis.datasource.tsharkProtocol import TsharkProtocol
from core.apis.datasource.manualScreenShot import ManualScreenShot

gi.require_version("Gtk", "3.0")
gi.require_version("WebKit", "3.0")
from gi.repository import Gtk
from gi.repository import WebKit


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
        print("Technician:" + importInfo['tech'][0])
        print("Move to workspace:" + importInfo['moveFiles'][0])
        print("Import files from:" + importInfo['location'][0])
        print("Comments:" + importInfo['comment'][0])
        print("Event name:" + importInfo['event'][0])
        print("Date:" + importInfo['date'][0])
    # print (parse_qs(query))

    if 'exportData' in _uri:
        exportInfo = parse_qs(query)
        print("Technician:" + exportInfo['tech'][0])
        print("Move images:" + exportInfo['moveImages'][0])
        print("Import files from:" + exportInfo['location'][0])
        print("Event name:" + exportInfo['event'][0])
        print("Date:" + exportInfo['date'][0])
    # print (parse_qs(query))



    if not query:
        return
    else:
        queryDict = parse_qs(query)
        if 'request' in queryDict:
            if queryDict['request'][0] == 'keypressData':
                startDate = queryDict['startDate'][0]
                endDate = queryDict['endDate'][0]
                try:
                    techName = queryDict['techName'][0]
                except KeyError:
                    techName = ""
                try:
                    eventName = queryDict['eventName'][0]
                except KeyError:
                    eventName = ""
                keyData = PyKeyPress().selectKeyPressData(startDate, endDate, techName, eventName)
                clickData = PyClick().selectClickData(startDate, endDate, techName, eventName)
                timedData = PyTimed().selectTimedData(startDate, endDate, techName, eventName)
                js = "visualizeKeyData(%s, %s, %s);" % (keyData, clickData, timedData)
                webKitWebView.execute_script(js)
            elif queryDict['request'][0] == 'pcapData':
                startDate = queryDict['startDate'][0]
                endDate = queryDict['endDate'][0]
                try:
                    techName = queryDict['techName'][0]
                except KeyError:
                    techName = ""
                try:
                    eventName = queryDict['eventName'][0]
                except KeyError:
                    eventName = ""
                multiEx = MultiExcludeThroughput().selectMultiExcludeThroughputData(startDate, endDate, techName, eventName)
                multiInc = MultiIncludeThroughput().selectMultiIncludeThroughputData(startDate, endDate, techName, eventName)
                tshark = TsharkThroughput().selectTsharkThroughputData(startDate, endDate, techName, eventName)
                multiExProt = MultiExcludeProtocol().selectMultiExcludeProtocolData(startDate, endDate, techName, eventName)
                multiIncProt = MultiIncludeProtocol().selectMultiIncludeProtocolData(startDate, endDate, techName, eventName)
                tsharkProt = TsharkProtocol().selectTsharkProtocolData(startDate, endDate, techName, eventName)
                js = "visualizePCAPData(%s, %s, %s, %s, %s, %s);" % (
                    multiEx, multiExProt, multiInc, multiIncProt, tshark, tsharkProt)
                webKitWebView.execute_script(js)
            elif queryDict['request'][0] == 'screenshotData':
                startDate = queryDict['startDate'][0]
                endDate = queryDict['endDate'][0]
                try:
                    techName = queryDict['techName'][0]
                except KeyError:
                    techName = ""
                try:
                    eventName = queryDict['eventName'][0]
                except KeyError:
                    eventName = ""
                snap = ManualScreenShot().selectManualScreenShotData(startDate, endDate, techName, eventName)
                js = "visualizeSnapshotData(%s);" % (snap)
                webKitWebView.execute_script(js)

        elif 'submission' in queryDict:
            if queryDict['submission'][0] == 'annotation':
                print("trying to submit"+query)
                itemID = queryDict['itemID'][0]
                itemType = queryDict['type'][0]
                annotation = queryDict['annotation'][0]
                if itemType == 'keypress':
                    PyKeyPress().addAnnotationKeyPress(itemID, annotation)
                elif itemType == 'click':
                    PyClick().addAnnotationClick(itemID, annotation)
                elif itemType == 'timed':
                    PyTimed().addAnnotationTimed(itemID, annotation)
        elif 'adminRequest' in queryDict:
            if queryDict['adminRequest'][0] == 'availablePlugins':
                load_available_renderers()
        elif 'adminSubmission' in queryDict:
            if queryDict['adminSubmission'][0] == 'pluginChanges':
                database = queryDict['database'][0]
                pcapDataProtocol = queryDict['pcapDataProtocol'][0]
                pcapThroughput = queryDict['pcapThroughput'][0]
                pyKeyLogger = queryDict['pyKeyLogger'][0]
                screenshots = queryDict['screenshots'][0]
                scriptFile = "scripts.txt"
                ConfigDatasources().setDefaultDatasource(database)
                ConfigRenderers().setDefaultRenderer("pcapDataProtocol", pcapDataProtocol, scriptFile)
                ConfigRenderers().setDefaultRenderer("pcapThroughput", pcapThroughput, scriptFile)
                ConfigRenderers().setDefaultRenderer("pyKeyLogger", pyKeyLogger, scriptFile)
                ConfigRenderers().setDefaultRenderer("screenshots", screenshots, scriptFile)

                print("updating plugin")
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


# Once MongoDB is installed as a service one everyone's machine, this can be uncommented.
# MongoDB will then be started as the app is started.
# subprocess.call(["mongod", "--repair"], shell=True)
# subprocess.Popen(["mongod"], shell=True)

gtkWindow = Gtk.Window()
webKitWebView = WebKit.WebView()
gtkScrolledWindow = Gtk.ScrolledWindow()
gtkScrolledWindow.add(webKitWebView)
gtkWindow.add(gtkScrolledWindow)
gtkWindow.connect("delete-event", Gtk.main_quit)

gtkWindow.set_size_request(1000, 800)

# generate the index.html page based on the renderer plugin
GenerateHtml().generateHtml()
uri = "file:///" + os.getcwd() + "/viewmanager/index.html"

webKitWebView.load_uri(uri)
webKitWebView.connect("resource-request-starting", handle)

gtkWindow.show_all()
Gtk.main()

# python -m viewmanager.dssvisualizer
