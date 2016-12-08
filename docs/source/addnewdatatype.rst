Adding a new data type
======================

In order to add a new type of data besides the current *Keylogger*, *PCAP*, and
*Screenshot* data types, it must be added in the code.

Renderer Plugin Creation
------------------------

This section will cover how to added a new type of data.

**index.html.template**

The first change that can be made is to add a new *div* to the *index.html* template.
In order to do this:

#. Open ``index.html.template`` in your favorite editor;
#. Look for the comment that says: ``<!-- Add div here for new data type -->``;
#. Add a new title for the *div* by using the ``H3`` header;
#. Add the *div*, give it an appropriately named *id*;
#. Finally apply the ``timeline`` CSS class to it.

**newDataType.js**

In order to prepare the renderer plugin for the new data type, the following must be considered:

* The way we are adding the timelines is by creating a new object. This object contains the function that generates the timeline.

    .. code-block:: javascript

        var NewDataType = function(newDataTypeData){});

* There must be two additional methods added by using the JavaScript ``Prototype`` builder.

    * The getDataset function that returns the data for that timeline.

        .. code-block:: javascript

            NewDataType.prototype.getDataset = function(){}

    * The setTimelineWindow function that sets the window for that timeline.

        .. code-block:: javascript

            NewDataType.prototype.setTimelineWindow = function(start,end){}

* The easiest example to look at is the *screenshot.js* file that is located in ``plugins/renderer/visjs/js``.

**main.js**

Now in order to get the data from the database we need to write the JavaScript to do an AJAX request to the Python backend. In order to do this:

#. At the very top underneath all the current variables, add a new array where the timelines will be stored.

    .. code-block:: javascript

        var newDataType = [];

#. Now we must form the AJAX request. So in the ``$(document).on("click", "#dateInput", function(){`` ... ``});`` function:

    * Add the ``$("#New_Data_Type_Div").html("")`` code to make the *div* you created in the *index.html* template blank. Otherwise, if the user does more than one search for data, the new timeline(s) will be appended to the ones from the previous search.

    * Form the AJAX request URL in the following manner:

        ``http://localhost?request=`` **newDataType** ``&startDate=" + start + "&endDate=" + end + "&techNames=" + techNames + "&eventNames=" + eventNames + "&eventTechNames=" + eventTechNames;``

    * Now pass that URL to the ``getRequest()`` function. The ``setTimeout()`` function was used so that the program would not freeze completely. Without it the program will freeze until all of the timelines have been loaded.

#. Now create the function that *dssvisualizer.py* will be calling to pass the data to.

    * The function naming convenction we followed is ``visualize`` **NewDataType** ``Data()``
    * Inside this function, the array of event and tech names must be collected. So the very first line will be ``var eventTechNames = getArrayOfEventTechNames();``
    * Now get the data split by event and tech name by calling ``splitDataForMultipleDataSetManagement()``. You will need to pass it the array of event and tech names and the data received from *dssvisualizer.py*

        .. code-block:: javascript

            newDataTypeDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, newDataTypeData);

    * Iterate through the arrays of what is returned and iterate through the data objects within the array, so that you can *fix* the data by calling the ``getFixedDataPoint()`` function.

        * We also added ``obj['type'] = ['box'];`` so that VisJS will render the data objects as blocks instead of just points.

    * Once the data is *fixed*, iterate through the ``eventTechNames`` array in order to append a new title and add the timeline objects to the array of timelines.

        .. code-block:: javascript

            newDataType.push(new NewDataTypeObject(newDataTypeDataArrays[index]['data']));

        * Please note that the timeline object is an object in the JavaScript file you made for your new renderer plugin inside of ``plugins/renderer/``.

    * If you want the timeline ranges to be synchronized, you will also have to add a way to iterate through the array of timelines so that you can call the ``setTimelineWindow()`` function in each of them. This iteration will be added in the ``getRangeChanged()`` function.

**filterAndSearch.js**

Now in order for the data in the timeline to be searched or filtered, code must also be added to *filterAndSearch.js*.

#. Within the ``filterTheTimeline()`` method, you must add a way to iterate through the array of timelines. This is currently being done in the following manner:

    .. code-block:: javascript

        if(newDataType != null){
            if(newDataType.length > 0){
                newDataType.forEach(function(timeline){
                    var data = timeline.getDataset();
                    filterTheData(data, filter);
                });
            }
        }

    This first checks if the array containing all the timelines exists and is not empty,
    grabs the data from the timeline using the ``getDataset()`` function within the plugin file,
    and sends the data and filter to the ``filterTheData()`` function.

#. Within the ``searchTheTimeline()`` method, iterate through the array of timelines in the same fashion as for the ``filterTheTimeline()`` method.
