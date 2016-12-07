
Datasource API
==============

So to keep things simple for the developers and enable multiple people to work on the backend, there is one class created
for each data type.  All data types implement the same methods, and a few implement some more for the distinct Event/Tech name functionality.


Methods Implemented
-------------------
* **def importXxxxData(self, jsonData)**: Imports all records from a JSON file. Dates are in UTC time.

* **def selectXxxxData(self, startDate, endDate, techNames, eventNames, eventTechList)**: Select the key press data by start and end date. The input here will be strings, datetimes will be passed to the plugin.

* **def selectXxxxDataById(self, dataId)**: Select the key press data by its ID

* **def modifyFixedXxxxData(self, dataId, keypress_id, content, className, startDate, isDeleted)**: Inserts or updates the record of the 'fixed' key press data.

* **def deleteFixedXxxxData(self, dataId)**: Delete a 'fixed' key press data.

* **def modifyAnnotationXxxx(self, dataId, annotationText)**: Add or edit an annotation on the object.  This will add a single 'annotation' attribute to the object.

* **def addAnnotationToArrayXxxx(self, dataId, annotationText)**: Add an annotation to an array of annotations for the dataId.

* **def editAnnotationInArrayXxxx(self, dataId, oldAnnotationText, newAnnotationText)**: Edit an annotation in the array of annotations.

* **def deleteAnnotationFromArrayXxxx(self, dataId, annotationText)**: Delete an annotation from array for the dataId

* **def deleteAllAnnotationsForXxxx(self, dataId)**: Delete all annotations from the  object.

* **def addAnnotationToXxxxTimeline(self, startTime, annotationText, techName, eventName)**: Ands an annotation to the timeline (not a data point)

* These next two methods are only in KeyPress, MulitExcludeThroughput, MulitIncludeThroughput, TSharkThroughput, and ManualScreenshot

  * **def getDistinctTechNames(self)**: Get a list of distinct technician names. used for the UI when searching by technician name.
  * **def getDistinctEventNames(self)**: Get a list of distinct event names. used for the UI when searching by event name.

More Information
----------------
Please see the documentation in the following classes to learn more about the methods that are needed:

* KeyLogger Data

  * `Click API <core.apis.datasource.html#module-core.apis.datasource.pyClick>`_
  * `Keypress API <core.apis.datasource.html#module-core.apis.datasource.pyKeyPress>`_
  * `Timed API <core.apis.datasource.html#module-core.apis.datasource.pyTimed>`_

* Manual Screenshot Data

  * `ManualScreenShot API <core.apis.datasource.html#module-core.apis.datasource.manualScreenShot>`_

* PCAP Data

  * `MultiExcludeProtocol API <core.apis.datasource.html#module-core.apis.datasource.multiExcludeProtocol>`_
  * `MultiExcludeThroughput API <core.apis.datasource.html#module-core.apis.datasource.multiExcludeThroughput>`_
  * `MultiIncludeProtocol API <core.apis.datasource.html#module-core.apis.datasource.multiIncludeProtocol>`_
  * `MultiIncludeThroughput API <core.apis.datasource.html#module-core.apis.datasource.multiIncludeThroughput>`_
  * `TsharkProtocol API <core.apis.datasource.html#module-core.apis.datasource.tsharkProtocol>`_
  * `TsharkThroughput API <core.apis.datasource.html#module-core.apis.datasource.tsharkThroughput>`_

Simplify Things - Make it more Plug and Playable
------------------------------------------------
This architecture could be refactored to remove most of the classes and simplify plugin creation.  If each JSON file had a unique className (both the PCAP XY and All have the same classNames
so we can't distinguish between the three PCAP types) or other attribute that was unique across all .json files, core data source API could just pass the JSON along to the plugin.
The plugin could take that className/unique attribute and know which collection/doc_type to use.  The only difference between all these files is the collect/doc_type and the attributes
that type has (used for editing).
