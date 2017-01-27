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

from core.apis.renderer.pluginImporter import PluginImporter
import ujson

import gi
import os
from urllib.parse import parse_qs

# Only use files from core.  DO NOT use files from plugins.
from core.apis.renderer.eventTechNames import EventTechNames
from core.apis.renderer.importData import ImportData
from core.apis.renderer.plugins import Plugins
from core.apis.renderer.request import Request
from core.apis.renderer.submission import Submission
from core.apis.renderer.generateHtml import GenerateHtml

from viewmanager.exportPopup import ExportPopup
from viewmanager.folderExplorer import FolderExplorer

gi.require_version("Gtk", "3.0")
gi.require_version("WebKit", "3.0")
from gi.repository import Gtk
from gi.repository import WebKit

def handle(web_view, web_frame, web_resource, request, response):
    ##'query' contains the data sent from the jquery.get method

    query = request.get_message().get_uri().get_query()
    _uri = request.get_uri()

    if 'installDatasources' in _uri or 'adminset' in _uri:
        script = Plugins().load_uninstalled_plugins(query, "datasource")
        webKitWebView.execute_script(script)

    if 'installRends' in _uri or 'adminset' in _uri:
        script = Plugins().load_uninstalled_plugins(query, "renderer")
        webKitWebView.execute_script(script)

    if 'importData' in _uri:
        ImportData().importData(query)
        setLabel = "$('#importedData').html('Data imported!');"
        webKitWebView.execute_script(setLabel)

    if 'exportData' in _uri:
        if query:
            exportInfo = parse_qs(query)
            ExportPopup(exportInfo)

    if 'explore' in _uri:
        folderChange = FolderExplorer(Gtk.Window()).openExplorer()
        webKitWebView.execute_script(folderChange)

    if not query:
        return
    else:
        queryDict = parse_qs(query)
        if 'request' in queryDict:
            js = Request().getData(queryDict)
            
            webKitWebView.execute_script(js)

        elif 'submission' in queryDict:
            if queryDict['submission'][0] == 'annotation':
                Submission().editAnnotation(queryDict)

            if queryDict['submission'][0] == 'edit':
                Submission().editData(queryDict)

        elif 'adminRequest' in queryDict:
            if queryDict['adminRequest'][0] == 'availablePlugins':
                js = Plugins().load_available_renderers()
                webKitWebView.execute_script(js)

        elif 'adminSubmission' in queryDict:
            if queryDict['adminSubmission'][0] == 'pluginChanges':
                Submission().updateConfiguration(queryDict)

        elif 'populateDropdown' in queryDict:
            js = EventTechNames().getEventTechNames(queryDict)
            webKitWebView.execute_script(js)

    return



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
