var windowRangeStart;
var windowRangeEnd;
var techExport;
var eventExport;
$(document).on("click", "#dateInput", function(){
	$("#loading").removeClass("hidden");
	$("#keypressData").html("");
	$("#multiExcludeData").html("");
	$("#multiIncludeData").html("");
	$("#tsharkData").html("");
	$("#screenshotData").html("");

	var start = $("#datepickerStart").val();
	var end = $("#datepickerEnd").val();
	windowRangeStart = start;
	windowRangeEnd = end;
	var techNames = $("#techOptions").val();
	var eventNames = $("#eventOptions").val();
    var eventTechNames = $("#techAndEventOptions").val();

	if(start == ""){
		start = '2000-01-01 00:00:00';
	}
	else{
		start = start + " 00:00:00";
	}
	if(end == ""){
		end = '3000-01-01 23:59:59';
	}
	else{
		end = end + " 23:59:59";
	}
	var keypressDataUrl = "http://localhost?request=keypressData&startDate="+start+"&endDate="+end+"&techNames="+techNames+"&eventNames="+eventNames+"&eventTechNames="+eventTechNames;
	$.get(keypressDataUrl);
	var pcapDataUrl = "http://localhost?request=pcapData&startDate="+start+"&endDate="+end+"&techNames="+techNames+"&eventNames="+eventNames+"&eventTechNames="+eventTechNames;
	$.get(pcapDataUrl);
	var screenshotDataUrl = "http://localhost?request=screenshotData&startDate="+start+"&endDate="+end+"&techNames="+techNames+"&eventNames="+eventNames+"&eventTechNames="+eventTechNames;
	$.get(screenshotDataUrl);
});

$(document).on("change", "#keylogger", function(){
    $('#keypressData').toggle();
});

$(document).on("change", "#multiexclude", function(){
    $('#multiExcludeData').toggle();
});

$(document).on("change", "#multiinclude", function(){
    $('#multiIncludeData').toggle();
});

$(document).on("change", "#tshark", function(){
    $('#tsharkData').toggle();
});

$(document).on("change", "#snapshots", function(){
    $('#screenshotData').toggle();
});

var keylogger;
var pcapData;
var snap;
function visualizeKeyData(keyData, clickData, timedData, count){
    eventTechNames = getArrayOfEventTechNames();
    // if eventTechNames.length > 0 then we know we have multiple datasets to work with.
    if(eventTechNames.length > 0) {
        keyDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, keyData);
        _.each(keyDataArrays, function(keyDataArray) {
            _.each(keyDataArray['data'], function(obj) {
                obj['type'] = ['box'];
            });
        });

        clickDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, clickData);
        _.each(clickDataArrays, function(clickDataArray) {
            _.each(clickDataArray['data'], function(obj) {
                obj['type'] = ['box'];
            });
        });

        timedDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, timedData);
        _.each(timedDataArrays, function(timedDataArray) {
            _.each(timedDataArray['data'], function(obj) {
                obj['type'] = ['box'];
            });
        });


        _.each(eventTechNames, function(eventTechName, index) {
            $("#keypressData").append(eventTechName);
            keylogger = new KeyLogger(keyDataArrays[index]['data'], clickDataArrays[index]['data'], timedDataArrays[index]['data']);
        });

    } else {
        // otherwise we have just one dataset
        _.each(keyData, function(obj) {
            obj['type'] = ['box'];
        });
        _.each(clickData, function(obj) {
            obj['type'] = ['box'];
        });
        _.each(timedData, function(obj) {
            obj['type'] = ['box'];
        });

        keylogger = new KeyLogger(keyData, clickData, timedData);
	}

}

function visualizePCAPData(meXY, meAll, miXY, miAll, tsXY, tsAll){
    eventTechNames = getArrayOfEventTechNames();
    // if eventTechNames.length > 0 then we know we have multiple datasets to work with.
    if(eventTechNames.length > 0) {

        // multi exclude data
        meXYDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, meXY);
        meAllDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, meAll);

        _.each(meXYDataArrays, function(meXYDataArray, index) {
            _.each(meXYDataArray['data'], function(xyObj) {
                var xyTime = xyObj['x'];
                _.each(meAllDataArrays[index]['data'], function(allObj) {
                    var allTime = allObj['start'];
                    if(allTime == xyTime){
                        xyObj['label'] = {"content": allObj['content']};
                    }
                });
            });
        });

        // multi include data
        miXYDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, miXY);
        miAllDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, miAll);

        _.each(miXYDataArrays, function(miXYDataArray, index) {
            _.each(miXYDataArray['data'], function(xyObj) {
                var xyTime = xyObj['x'];
                _.each(miAllDataArrays[index]['data'], function(allObj) {
                    var allTime = allObj['start'];
                    if(allTime == xyTime){
                        xyObj['label'] = {"content": allObj['content']};
                    }
                });
            });
        });

        // tshark data
        tsXYDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, tsXY);
        tsAllDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, tsAll);

        _.each(tsXYDataArrays, function(tsXYDataArray, index) {
            _.each(tsXYDataArray['data'], function(xyObj) {
                var xyTime = xyObj['x'];
                _.each(tsAllDataArrays[index]['data'], function(allObj) {
                    var allTime = allObj['start'];
                    if(allTime == xyTime){
                        xyObj['label'] = {"content": allObj['content']};
                    }
                });
            });
        });

        _.each(eventTechNames, function(eventTechName, index) {
            $("#multiExcludeData").append(eventTechName);
            $("#multiIncludeData").append(eventTechName);
            $("#tsharkData").append(eventTechName);
            pcapData = new PCAPData(meXYDataArrays[index]['data'], meAllDataArrays[index]['data'],
                                    miXYDataArrays[index]['data'], miAllDataArrays[index]['data'],
                                    tsXYDataArrays[index]['data'], tsAllDataArrays[index]['data']);
        });


    } else {
        // otherwise we have just one dataset
        _.each(meXY, function(xyObj) {
            var xyTime = xyObj['x'];
            _.each(meAll, function(allObj) {
                var allTime = allObj['start'];
                if(allTime == xyTime){
                    xyObj['label'] = {"content": allObj['content']};
                }
            });
        });

        _.each(miXY, function(xyObj) {
            var xyTime = xyObj['x'];
            _.each(miAll, function(allObj) {
                var allTime = allObj['start'];
                if(allTime == xyTime){
                    xyObj['label'] = {"content": allObj['content']};
                }
            });
        });
        _.each(tsXY, function(xyObj) {
            var xyTime = xyObj['x'];
            _.each(tsAll, function(allObj) {
                var allTime = allObj['start'];
                if(allTime == xyTime){
                    xyObj['label'] = {"content": allObj['content']};
                }
            });
        });
        pcapData = new PCAPData(meXY, meAll, miXY, miAll, tsXY, tsAll);
	}
}

function visualizeSnapshotData(snapData){
    eventTechNames = getArrayOfEventTechNames();
    // if eventTechNames.length > 0 then we know we have multiple datasets to work with.
    if(eventTechNames.length > 0) {
        snapDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, snapData);
        _.each(snapDataArrays, function(snapDataArray) {
            _.each(snapDataArray['data'], function(obj) {
                obj['type'] = ['box'];
            });

            $("#screenshotData").append(snapDataArray["eventTechName"]);
            snap = new Screenshot(snapDataArray['data']);
    	});
    } else {
        // otherwise we have just one dataset
        _.each(snapData, function(obj) {
            obj['type'] = ['box'];
        });

    	snap = new Screenshot(snapData);
	}

}

function splitDataForMultipleDataSetManagement(eventTechNames, jsonObjects) {
    var allDataArray = []

    _.each(eventTechNames, function(eventTechName) {
        dataArray = []
        _.each(jsonObjects, function(obj) {
            if(obj["metadata"]["eventName"] + " by " + obj["metadata"]["techName"] == eventTechName) {
                dataArray.push(obj);
            }
        });
        if(dataArray.length > 0) {
            var newJson = {}
            newJson["eventTechName"] = eventTechName;
            newJson["data"] = dataArray;
            allDataArray.push(newJson);
        }
    });

    return allDataArray;
}

function getArrayOfEventTechNames() {
    // we need to get an array of the different possible event/tech combinations that we will use to separate the
    // returned data for multi dataset management.
    // but only if there is more than one option.  If there is just one option (or none) all the data will show
    // on one timeline.

	var techNames = $("#techOptions").val();
	var eventNames = $("#eventOptions").val();
    var eventTechNames = $("#techAndEventOptions").val();
    var eventTechs = [];

    // #techAndEventOptions already as the unique list, just return it
    if(eventTechNames.length > 1) {
        return eventTechNames;

    // If either eventNames or techNames is > 1 we have multiple options
    } else if (eventNames.length > 1 || techNames.length > 1) {

        _.each(techNames, function(tech) {
            _.each(eventNames, function(event){
                eventTechs.push(event + ' by ' + tech);
            });
        });
        return eventTechs;

    // otherwise return an empty array to indicate all data should be in one timeline.
    } else {
        return eventTechs;
    }
}

function prettyAdd(title, callback){
	swal({
		title: title,
		input: 'textarea',
		showCancelButton: true
	}).then(callback);
}


function getRangeChanged(properties){
	windowRangeStart = properties.start;
	windowRangeEnd = properties.end;
	keylogger.setTimelineWindow(windowRangeStart,windowRangeEnd);
	pcapData.setPcapWindows(windowRangeStart,windowRangeEnd);
	snap.setTimelineWindow(windowRangeStart,windowRangeEnd);
}

function exportData(){
	techExport = $("#techName").val();
	eventExport = $("#eventName").val();
    if(windowRangeStart == null || windowRangeEnd == null){
        alert(' time range is undefined');
    }
    else if(techExport == ""){
        alert('tech name is undefined');
    }
    else if(eventExport == ""){
        alert(' event name is undefined')
    }
    else{
        $(document).ready(function(){
            $.get("http://dssvisualizer.py/exportData",{start:windowRangeStart,end:windowRangeEnd,techName:techExport,eventName:eventExport});
        });
    }
}

function populateTechDropdown(techList) {
    for(var i=0; i<techList.length; i++) {
        $("#techOptions").append('<option value="'+techList[i]+'">'+techList[i]+'</option>')
    }
    $("#techOptions").trigger("chosen:updated");
}

function populateEventDropdown(eventList) {
    for(var i=0; i<eventList.length; i++) {
        $("#eventOptions").append('<option value="'+eventList[i]+'">'+eventList[i]+'</option>')
    }
    $("#eventOptions").trigger("chosen:updated");
}

function populateTechAndEventDropdown(techEventList) {
    for(var i=0; i<techEventList.length; i++) {
        $("#techAndEventOptions").append('<option value="'+techEventList[i]+'">'+techEventList[i]+'</option>')
    }
    $("#techAndEventOptions").trigger("chosen:updated");
}

// also need to enable/disable tech dropdown in this method
// enable when eventNames > 0, otherwise disable.
$(document).on("change", "#eventOptions", function(evt, params){
    $('#techOptions').empty()
    var eventNames = $("#eventOptions").val();
    if(eventNames.length > 0) {
        var getTechNames = "http://localhost?populateDropdown=availableTechNames&eventNames="+eventNames;
        $.get(getTechNames);
    } else {
        $("#techOptions").trigger("chosen:updated");
    }
});


$(document).ready(function() {
    var getEventNames = "http://localhost?populateDropdown=availableEventNames";
    $.get(getEventNames)
    var getEventTechNames = "http://localhost?populateDropdown=availableTechAndEventNames";
    $.get(getEventTechNames)
});

//Disables dropdown menu for events. Kept the plugin id updates ($("#techAndEventOptions").prop("disabled", false);)
//seperate from the on.change (for #eventOptions) function above and the #techAndEventOptions on.change below
//to prevent overwriting each other
$(document).on("change", "#eventOptions", function(evt, params){
	var eventNames = $("#eventOptions").val();
	if(eventNames.length>0){
		$("#techAndEventOptions").prop("disabled", true);
	}
	else{
		$("#techAndEventOptions").prop("disabled", false);
	}
	$("#techAndEventOptions").trigger("chosen:updated");
});


$(document).on("change", "#techAndEventOptions", function(evt, params){
	var techAndEventNames = $("#techAndEventOptions").val();
	if(techAndEventNames.length>0){
		$("#eventOptions").prop("disabled", true);
		$("#techOptions").prop("disabled", true);
	}
	else{
		$("#eventOptions").prop("disabled", false);
		$("#techOptions").prop("disabled", false);
	}
	$("#eventOptions").trigger("chosen:updated");
	$("#techOptions").trigger("chosen:updated");

});
