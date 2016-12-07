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
from urllib.parse import parse_qs
gi.require_version("Gtk", "3.0")
gi.require_version("WebKit", "3.0")
from gi.repository import Gtk
from gi.repository import WebKit
from core.config.dataExport import DataExport
from viewmanager.folderExplorer import FolderExplorer

class ExportPopup:

    def __init__(self, exportInfo):

        self.exportInfo = exportInfo
        self.gtkWindow = Gtk.Window()
        self.gtkWindow.set_title("Export Data")
        self.webKitWebView = WebKit.WebView()
        self.gtkWindow.add(self.webKitWebView)
        self.gtkWindow.connect("delete-event", self.close)

        # generate the index.html page based on the renderer plugin
        uri = "file:///" + os.getcwd() + "/viewmanager/exportPage.html"

        self.webKitWebView.load_uri(uri)
        self.webKitWebView.connect("resource-request-starting", self.handle)

        self.gtkWindow.show_all()
        self.gtkWindow.set_size_request(200, 100)
        self.gtkWindow.set_resizable(False)
        self.gtkWindow.set_position(Gtk.WindowPosition.MOUSE)

    def handle(self, web_view, web_frame, web_resource, request, response):
        query = request.get_message().get_uri().get_query()
        uri = request.get_uri()
        if 'explore' in uri:
            folderChange = FolderExplorer(Gtk.Window()).openExplorer()
            self.webKitWebView.execute_script(folderChange)

        moreExportInfo = parse_qs(query)
        if not moreExportInfo:
            return

        location = moreExportInfo['location'][0]

        moveImages = False
        if 'moveImages' in moreExportInfo:
            moveImages = True

        ## date format -> %Y-%m-%d %H:%M:%S
        startDate = self.prepareDate(self.exportInfo['start'][0])
        endDate = self.prepareDate(self.exportInfo['end'][0])

        if startDate == endDate:
            endDate = endDate.replace('00:00:00', '23:59:59')

        exporter = DataExport()
        if 'techAndEvent[]' in self.exportInfo:
            exporter.exportAllData(startDate, endDate, list(), list(), self.exportInfo['techAndEvent[]'], moveImages, location)
            self.close(self.gtkWindow, None)
        else:
            exporter.exportAllData(startDate, endDate, self.exportInfo['techName[]'], self.exportInfo['eventName[]'], list(), moveImages, location)
            self.close(self.gtkWindow, None)



    def prepareDate(self, rawDate):
        dateList = rawDate.split()
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        if len(dateList) < 2:
            time = "00:00:00"
            day = dateList[0]
            processedDate = day + " " + time
        else:
            time = dateList[4]
            month = months.index(dateList[1]) + 1
            day = dateList[3] + "-" + str(month) + "-" + dateList[2]
            processedDate = day + " " + time

        return processedDate

    def close(self, widget, event):
        widget.remove(self.webKitWebView)
        widget.destroy()
