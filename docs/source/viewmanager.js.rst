viewmanager.js package
======================

Submodules
----------

viewmanager.js.admin module
---------------------------

Used solely by *admin.html*

.. js:function:: ready()

	Runs when the HTML is done loading.
	Currently split into three:
		* Sends an AJAX request to gather the list of available plugins upon load;
		* Calls the ``updateJson()`` function to set the active plugins when the *Submit* button is clicked;
		* Handles the submitting of the *Import* and *Export* forms.

.. js:function:: createRadioButtons(plugins)

	Receives the list of plugins as a JSON object from *dssvisualizer.py*.
	Produces the radio buttons for the available plugins.

	:param plugins: JSON object containg the available and currently active plugins.

.. js:function:: updateJson()

	Runs when the *Submit* button is clicked.
	Sends an AJAX request to submit any changes made to the active plugins.

.. js:function:: getCurrentDate()

	**Not being used.** Gets the current date.

.. js:function:: zeroPadNumber(number)

	**Not being used.** Used by ``getCurrentDate()``.

.. js:function:: explore()

	**Not being used.**

viewmanager.js.annotation module
--------------------------------

**Not being used.**

viewmanager.js.datepicker module
--------------------------------

Used for the calendar that pops up to allow the user to pick a date when selecting which data to display.

.. js:data:: dateFormat

	Sets the format of how the date will be displayed in the input box.

.. js:data:: start

	Initializes the *start* input box to be a *datepicker* object.
	Also assigns options and the *on change* events.

.. js:data:: end

	Initializes the *end* input box to be a *datepicker* object.
	Also assigns options and the *on change* events.

.. js:function:: getDate(element)

	Gets the date that is currently in the input box.
	Used to limit the dates that can be selected.

	:param element: The HTML DOM element from which to get the date.

viewmanager.js.exportData module
--------------------------------

Contains the function for exporting the data.

.. js:function:: exportData()

	Exports the visible data.
	Sends an AJAX request to submit the data export.

viewmanager.js.filterAndSearch module
-------------------------------------

Contains the functions for searching and filtering the visible data.

.. js:data:: attributesToBeSearchedAndFiltered

	Array of JSON attributes that will be searched or filtered through.

.. js:function:: filterTheTimeline()

	Gets the value of the *filter* input box and goes through the arrays of timelines,
	gets the dataset from each timeline, and sends the dataset and filter to the
	``filterTheData()`` function.

.. js:function:: unFilterTheTimeline()

	Removes the CSS class that hides the data objects by selecting the HTML elements
	that have the class.

.. js:function:: filterTheData(data, filter)

	Searches through the data for the filter based on the ``attributesToBeSearchedAndFiltered``
	array. If the filter is **not** found within the attribute content, the *filterHide*
	CSS class is applied to the HTML element based on the id within the *data*
	HTML attribute.

	:param data: JSON object that contains all the data to be filtered.
	:param String filter: Contains the value from the *filter* input box.

.. js:function:: searchTheTimeline()

	Gets the value of the *search* input box and goes through the arrays of timelines,
	gets the dataset from each timeline, and sends the dataset and search keyword to the
	``searchTheData()`` function.

.. js:function:: unSearchTheTimeline()

	Removes the CSS class that highlights the data objects by selecting the HTML elements
	that have the class.

.. js:function:: searchTheData(data, search)

	Searches through the data for the search keyword based on the ``attributesToBeSearchedAndFiltered``
	array. If the search keyword is found within the attribute content, the *search*
	CSS class is applied to the HTML element based on the id within the *data*
	HTML attribute.

	:param data: JSON object that contains all the data to be searched.
	:param String search: Contains the value from the *search* input box.

viewmanager.js.main module
--------------------------

Handles all the main functions needed. Contains global variables that get used
in other JavaScript modules throughout the system. Also begins the process of
creating the timelines.

.. js:data:: windowRangeStart

	Holds the start date for the window range to keep the timelines synchronized.

.. js:data:: windowRangeEnd

	Holds the end date for the window range to keep the timelines synchronized.

.. js:data:: techExport

	Holds the value of the selected technicians. Used by the ``exportData`` function.

.. js:data:: eventExport

	Holds the value of the selected events. Used by the ``exportData`` function.

.. js:data:: filter

	**Not being used.**

.. js:data:: search

	**Not being used.**

.. js:data:: keylogger

	Array of all the *keylogger* objects that hold the Keylogger timelines.

.. js:data:: pcapData

	Array of all the *pcap* objects that hold the PCAP timelines.

.. js:data:: snap

	Array of all the *snap* objects that hold the Screenshot timelines.

.. js:function:: on("click", "#dateInput")

	Handles the submission of the filter parameters for displaying the timelines.
	Prepares an AJAX request to *dssvisualizer.py* to receive the JSON for the
	Keylogger, PCAP, and Screenshot data.

.. js:function:: getRequest(url)

	Sends the AJAX request received from the submission of the initial form to
	*dssvisualizer.py*.

.. js:function:: on("change", IdOfCheckbox)

	These functions toggle the visibility of the timelines based on the *checked*
	status of the checkboxes.

.. js:function:: on("click", FilterSearchAndResetButtonID)

	These functions handle the firing of the filter and search functions and also
	the reset functions for each.

.. js:function:: visualizeKeyData(keyData, clickData, timedData, count)

	Receives the Keylogger data from *dssvisualizer.py* and prepares it by the
	event and tech names. Also *fixes* the data to only contain the fixed
	attributes and creates the ``KeyLogger`` objects and stores them in the
	``keylogger`` array.

	:param keyData: JSON object that holds all of the *keypress* data.
	:param clickData: JSON object that holds all of the *clicked* data.
	:param timedData: JSON object that holds all of the *timed* data.
	:param count: **Not being used.**

.. js:function:: visualizePCAPData(meXY, meAll, miXY, miAll, tsXY, tsAll)

	Receives the PCAP data from *dssvisualizer.py* and prepares it by the
	event and tech names. Also *fixes* the data to only contain the fixed
	attributes and creates the ``PCAPData`` objects and stores them in the
	``pcapData`` array.

	:param meXY: JSON object that holds all of the *multi exclude XY* data.
	:param meAll: JSON object that holds all of the *multi exlude all* data.
	:param miXY: JSON object that holds all of the *multi include XY* data.
	:param miAll: JSON object that holds all of the *multi inlude all* data.
	:param tsXY: JSON object that holds all of the *tshark XY* data.
	:param tsAll: JSON object that holds all of the *tshark all* data.

.. js:function:: visualizeSnapshotData(snapData)

	Receives the Screenshot data from *dssvisualizer.py* and prepares it by the
	event and tech names. Also *fixes* the data to only contain the fixed
	attributes and creates the ``Screenshot`` objects and stores them in the
	``snap`` array.

	:param snapData: JSON object that holds all of the *screenshot* data.

.. js:function:: getRangeChanged(properties)

	Receives an object containing the properties of the event for when the range
	is changed in one of the timelines. Calls the ``setTimelineWindow`` functions
	of each of the timelines stored in the ``keylogger``, ``pcapData``, and
	``snap`` arrays.

	:param properties: Object containing properties of the *rangechange* event.

viewmanager.js.multipleDatasetManager module
--------------------------------------------

Manages splitting up the data for multiple events and techs.

.. js:function:: splitDataForMultipleDataSetManagement(eventTechNames, jsonObjects)

	Splits the JSON objects received from *dssvisualizer.py* by the event and
	tech names that are selected.

	:param eventTechNames: Array of the event and tech names.
	:param jsonObjects: JSON object of all the contained data.
	:returns: Array of the JSON object split by the event and tech names.

.. js:function:: getArrayOfEventTechNames()

	Returns the array of event and tech names based off of the input box for each
	or the combined event and tech name input box.

	:returns: Array of event and tech name strings.

viewmanager.js.prettyPopups module
----------------------------------

Contains the code for making nice looking pop-ups using the *sweetalert2* JavaScript
library.

.. js:data:: arrayOfEditIncludedAttr

	Array of attributes to be included for editing when user is trying to edit
	a data object.

.. js:function:: prettyAdd(title, callback)

	Uses *sweetalert2* to make a nice looking pop-up for adding a new annotation
	to a timeline.

	:param String title: String containing the title to be displayed by the pop-up.
	:param callback: Function that will be called once the user clicks *OK*.

.. js:function:: prettyConfirm(title, text, callback)

	Uses *sweetalert2* to make a nice looking pop-up for confirmation upon the
	deletion of a data object from a timeline.

	:param String title: String containing the title to be displayed by the pop-up.
	:param String text: String containing the message to be displayed by the pop-up.
	:param callback: Function that will be called once the user clicks *OK*.

.. js:function:: prettyPrompt(item, groupName, callback)

	Uses *sweetalert2* to make a nice looking pop-up for displaying the attributes
	of the selected data object and for providing a way to edit that data object.

	:param item: Data object that was selected.
	:param groupName: Name of the timeline group that was clicked on.
	:param callback: Function that will be called once the user clicks *OK* after editing.

.. js:function:: getEditForm(item)

	Returns the HTML for displaying the edit form.

	:param item: Data object that was selected.
	:returns: HTML form for editing the data object.

.. js:function:: formatObjectForDisplay(item)

	Returns the HTML for displaying the contents of the data object.

	:param item: Data object that was selected.
	:returns: HTML formatted contents of the data object.

.. js:function:: addLeadingZeroes(num)

	Receives an integer representing any number in a date and converts it to a
	string. If the integer is single-digit, it adds a leading zero.

	:param Integer num: Integer to be converted
	:returns: Integer converted to two-digit string.

viewmanager.js.showFixedData module
-----------------------------------

Handles the replacing of the raw data attributes with their fixed values so
that the attributes being displayed, filtered, and searched are the fixed attributes
instead of the raw data attributes.

.. js:function:: getFixedDataPoint(dataPoint)

	If an attribute is found in the *fixed* attribute, it will replace the raw
	value with the fixed value.

	:param dataPoint: One JSON data object.
	:returns: *Fixed* data object.

.. js:function:: getFixedDataArray(dataArray)

	Receives the array of data objects and uses the ``getFixedDataPoint`` function
	to replace the raw attributes with the fixed attributes.

	:param dataArray: Array of JSON data objects.
	:returns: Array of *fixed* data objects.

viewmanager.js.techAndEventDropdowns module
-------------------------------------------

Handles populating the event and tech dropdown lists and the change events on them.

.. js:function:: populateTechDropdown(techList)

	Populates the tech dropdown list.

	:param techList: The list of tech names.

.. js:function:: populateEventDropdown(eventList)

	Populates the event dropdown list.

	:param eventList: The list of event names.

.. js:function:: populateTechAndEventDropdown(techEventList)

	Populates the *TechAndEvent* dropdown list.

	:param techEventList: The list of techn and event names.

.. js:function:: on("change", "#eventOptions")

	Populates the tech dropdown list when there is a change in the selected events.

.. js:function:: ready()

	On page load, sends AJAX requests to populate the event and tech dropdown lists.

.. js:function:: on("change", "#eventOptions")

	Disables the *TechAndEvent* dropdown list.

.. js:function:: on("change", "#techAndEventOptions")

	Disables the event and tech dropdown lists when there is a selection made in
	the *TechAndEvent* dropdown list.
