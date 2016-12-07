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
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FolderExplorer:

    def __init__(self,window):
        self.window = window

    def findFolder(self):
        # print("exploring...")

        dialog = Gtk.FileChooserDialog("Please choose a folder", self.window,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        # if response == Gtk.ResponseType.OK:
        #     print("Select clicked")
        #     print("Folder selected: " + dialog.get_filename())
        # elif response == Gtk.ResponseType.CANCEL:
        #     print("Cancel clicked")
        folderName = dialog.get_filename()
        dialog.destroy()
        return folderName


    def openExplorer(self):
        ## get string path for folder from Explorer GUI
        folderPathPy = self.findFolder()

        if folderPathPy != None:
            folderPathHTML = list(folderPathPy)

            ## replace backslashes with forwardslashes so html doesn't complain
            ## ...and so user can see string version of selected folder path
            for i, char in enumerate(folderPathHTML):
                if char == '\\':
                    folderPathHTML[i] = '/'
            ##for linux
            folderPathHTML.append('/')
            folderPathHTML = ''.join(folderPathHTML)
            folderChange = "document.getElementById('chosenFolder').setAttribute('value','" + folderPathHTML + "');"
            return folderChange

## how to use
##folderName = FolderExplorer(Gtk.Window()).findFolder()
##print (folderName)
