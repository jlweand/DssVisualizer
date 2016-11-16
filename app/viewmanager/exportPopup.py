import gi
import os
import ujson
from urllib.parse import parse_qs
gi.require_version("Gtk", "3.0")
gi.require_version("WebKit", "3.0")
from gi.repository import Gtk
from gi.repository import WebKit
from core.config.dataExport import DataExport
from viewmanager.folderExplorer import FolderExplorer

class ExportPopup:

    def __init__(self,exportInfo):

        self.exportInfo = exportInfo
        self.gtkWindow = Gtk.Window()
        self.gtkWindow.set_title("Export Data")
        self.webKitWebView = WebKit.WebView()
        #gtkScrolledWindow = Gtk.ScrolledWindow()
        #gtkScrolledWindow.add(webKitWebView)
        self.gtkWindow.add(self.webKitWebView)
        self.gtkWindow.connect("delete-event", self.close)
        #self.gtkWindow.connect("leave-notify-event", self.close)
        #gtkWindow.connect("visibility-notify-event",Gtk.main_quit)


        # generate the index.html page based on the renderer plugin
        uri = "file:///" + os.getcwd() + "/viewmanager/exportPage.html"

        self.webKitWebView.load_uri(uri)
        self.webKitWebView.connect("resource-request-starting", self.handle)

        self.gtkWindow.show_all()
        self.gtkWindow.set_size_request(200, 100)
        self.gtkWindow.set_resizable(False)
        self.gtkWindow.set_position(Gtk.WindowPosition.MOUSE)

    def handle(self,web_view, web_frame, web_resource, request, response):
        query = request.get_message().get_uri().get_query()
        uri = request.get_uri()
        if 'explore' in uri:

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

        exporter = DataExport()
        if 'techAndEvent[]' in self.exportInfo:
            exporter.exportAllData(startDate, endDate, list(), list(), self.exportInfo['techAndEvent[]'], moveImages, location)
            self.close(self.gtkWindow,None)
        else:
            exporter.exportAllData(startDate, endDate, self.exportInfo['techName[]'], self.exportInfo['eventName[]'], list(), moveImages, location)
            self.close(self.gtkWindow,None)



    def prepareDate(self,rawDate):
        dateList = rawDate.split()
        day = ""
        time = ""
        month = ""
        processedDate = ""
        months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        if len(dateList) < 2:
            time = "0:0:0"
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
