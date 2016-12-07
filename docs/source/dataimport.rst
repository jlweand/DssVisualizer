
Import Data
===========
Requirements:
  * The directory pointed to should have JSON data.
  * Date format should be Year-Month-Day Hour:Minutes:Seconds

Import
------
1. Go to Administrator page in DSS Visualizer.
2. In the "Import Data" tab click on the text box for "Folder Location:". This opens up the file explorer.
3. Select directory you wish to search in. Double click to open folders.
  * The import process will search this folder and any subfolders for JSON files.
  * Based on the filename and folder in which it was found it will import it to the correct collection.
4. Once the file containing the data you wish to import is found, click Select. The path to this file will be added to the textbox.
5. Next enter the name of the technician, the name of the event, and any comments you may wish to add.
6. For the date field, the format is as stated above.

   **NOTE:** If no time is given, the default time will be the current time.

7. If you select the "Copy Images to Workspace" checkbox, the images will be copied into a local "workspace" folder.
8. Select submit to import the data you selected.


Export Data
===========

Requirements:
  * To export data you must have data currently visualized.

Export
------
1. Click on the "Export Visible Data" button.
2. A popup window will be displayed with a Destination field, an Export Images checkbox and an Export button.
3. By clicking on the Destination field, a File explorer window will open allowing for the selection of the folder destination.

   **NOTE:** The Destination field is a read-only field. Adding the destination path manually is not allowed.
   
4. By checking the Export Images checkbox, any images contained in the data will be saved in the destination folder along with other data.
5. Clicking on the Export button will save the Visible Data in the destination folder if one has been specified, otherwise it will do nothing.
