import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FolderExplorer:

    def __init__(self,window):
        self.window = window

    def findFolder(self):
        # print("exploring...")

        folderName = ""
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

## how to use
##folderName = FolderExplorer(Gtk.Window()).findFolder()
##print (folderName)
