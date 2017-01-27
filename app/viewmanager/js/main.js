var windowRangeStart;
var windowRangeEnd;
var techExport;
var eventExport;
var filter;
var search;
var snoopy = [];
var keylogger = [];
var pcapData = [];
var snap = [];

$(document).on("click", "#dateInput", function(){
	$("#loading").removeClass("hidden");
	$("#snoopy").html("");
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
	var snoopyDataUrl = "http://localhost?request=snoopyData&startDate="+start+"&endDate="+end+"&techNames="+techNames+"&eventNames="+eventNames+"&eventTechNames="+eventTechNames;
	getRequest(snoopyDataUrl);
	var keypressDataUrl = "http://localhost?request=keypressData&startDate="+start+"&endDate="+end+"&techNames="+techNames+"&eventNames="+eventNames+"&eventTechNames="+eventTechNames;
	getRequest(keypressDataUrl);
	var pcapDataUrl = "http://localhost?request=pcapData&startDate="+start+"&endDate="+end+"&techNames="+techNames+"&eventNames="+eventNames+"&eventTechNames="+eventTechNames;
	setTimeout(getRequest, 5000, pcapDataUrl);
	var screenshotDataUrl = "http://localhost?request=screenshotData&startDate="+start+"&endDate="+end+"&techNames="+techNames+"&eventNames="+eventNames+"&eventTechNames="+eventTechNames;
	setTimeout(getRequest, 5000, screenshotDataUrl);
	$("#filterSearch").removeClass("hidden");
	
	
});

function getRequest(url){
	$.get(url);
}

$(document).on("change", "#snoopy", function(){
	$('#snoopyData').toggle();
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

$(document).on("click", "#goFilter", function(){
	filterTheTimeline();
});

$(document).on("click", "#resetFilter", function(){
	unFilterTheTimeline();
});

$(document).on("click", "#goSearch", function(){
	searchTheTimeline();
});

$(document).on("click", "#resetSearch", function(){
	unSearchTheTimeline();
});

function visualizeSnoopyData(snoopyData){
	alert(JSON.stringify(snoopyData))
	filter = $("#filter").val();
	var eventTechNames = getArrayOfEventTechNames();
	// if eventTechNames.length > 0 then we know we have multiple datasets to work with.
	
	if(eventTechNames.length > 0) {
		
		snoopyDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, snoopyData);
		
		snoopyDataArrays.forEach(function(snoopyDataArray) {
			snoopyDataArray['data'].forEach(function(obj) {
				obj = getFixedDataPoint(obj);
				obj['type'] = ['box'];
			});
		});

		
		eventTechNames.forEach(function(eventTechName, index) {
			if(eventTechNames.length > 1){
				$("#snoopyData").append("<h4>"+eventTechName+"</h4>");
			}
			
			
			snoopy.push(new Snoopy(snoopyDataArrays[index]['data']));
		});
		

	}
}

function visualizeKeyData(keyData, clickData, timedData, count){
	filter = $("#filter").val();
	var eventTechNames = getArrayOfEventTechNames();
	// if eventTechNames.length > 0 then we know we have multiple datasets to work with.
	
	if(eventTechNames.length > 0) {
		
		keyDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, keyData);
		
		keyDataArrays.forEach(function(keyDataArray) {
			keyDataArray['data'].forEach(function(obj) {
				obj = getFixedDataPoint(obj);
				obj['type'] = ['box'];
			});
		});

		clickDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, clickData);
		clickDataArrays.forEach(function(clickDataArray) {
			clickDataArray['data'].forEach(function(obj) {
				obj = getFixedDataPoint(obj);
				obj['type'] = ['box'];
			});
		});

		timedDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, timedData);
		timedDataArrays.forEach(function(timedDataArray) {
			timedDataArray['data'].forEach(function(obj) {
				obj = getFixedDataPoint(obj);
				obj['type'] = ['box'];
			});
		});

		
		eventTechNames.forEach(function(eventTechName, index) {
			if(eventTechNames.length > 1){
				$("#keypressData").append("<h4>"+eventTechName+"</h4>");
			}
			
			keylogger.push(new KeyLogger(keyDataArrays[index]['data'], clickDataArrays[index]['data'], timedDataArrays[index]['data']));
		});

	}
}

function visualizePCAPData(meXY, meAll, miXY, miAll, tsXY, tsAll){
    meAll = getFixedDataArray(meAll);
    miAll = getFixedDataArray(miAll);
    tsAll = getFixedDataArray(tsAll);

	eventTechNames = getArrayOfEventTechNames();
	// if eventTechNames.length > 0 then we know we have multiple datasets to work with.
	if(eventTechNames.length > 0) {

		// multi exclude data
		meXYDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, meXY);
		meAllDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, meAll);

		meXYDataArrays.forEach(function(meXYDataArray, index) {
			meXYDataArray['data'].forEach(function(xyObj) {
				xyObj['label'] = {"content": xyObj['y']+" p/s"};
			});
		});

		// multi include data
		miXYDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, miXY);
		miAllDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, miAll);

		miXYDataArrays.forEach(function(miXYDataArray, index) {
			miXYDataArray['data'].forEach(function(xyObj) {
				xyObj['label'] = {"content": xyObj['y']+" p/s"};
			});
		});

		// tshark data
		tsXYDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, tsXY);
		tsAllDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, tsAll);

		tsXYDataArrays.forEach(function(tsXYDataArray, index) {
			tsXYDataArray['data'].forEach(function(xyObj) {
				xyObj['label'] = {"content": xyObj['y']+" p/s"};
			});
		});

		eventTechNames.forEach(function(eventTechName, index) {
			if(eventTechNames.length > 1){
				$("#multiExcludeData").append("<h4>"+eventTechName+"</h4>");
				$("#multiIncludeData").append("<h4>"+eventTechName+"</h4>");
				$("#tsharkData").append("<h4>"+eventTechName+"</h4>");
			}
			pcapData.push(new PCAPData(meXYDataArrays[index]['data'], meAllDataArrays[index]['data'],
									miXYDataArrays[index]['data'], miAllDataArrays[index]['data'],
									tsXYDataArrays[index]['data'], tsAllDataArrays[index]['data']))
		});
	}
}

function visualizeSnapshotData(snapData){
	eventTechNames = getArrayOfEventTechNames();
	// if eventTechNames.length > 0 then we know we have multiple datasets to work with.
	if(eventTechNames.length > 0) {
		snapDataArrays = splitDataForMultipleDataSetManagement(eventTechNames, snapData);
		snapDataArrays.forEach(function(snapDataArray) {
			snapDataArray['data'].forEach(function(obj) {
				obj = getFixedDataPoint(obj);
				obj['type'] = ['box'];
			});

			if(eventTechNames.length > 1){
				$("#screenshotData").append("<h4>"+snapDataArray["eventTechName"]+"</h4>");
			}
			snap.push(new Screenshot(snapDataArray['data']));
		});
	}
	$("#loading").addClass("hidden");
}

function getRangeChanged(properties){
	windowRangeStart = properties.start;
	windowRangeEnd = properties.end;
	keylogger.forEach(function(keyloggerTimeline){
		keyloggerTimeline.setTimelineWindow(windowRangeStart,windowRangeEnd);
	});
	pcapData.forEach(function(pcapDataTimelines){
		pcapDataTimelines.setPcapWindows(windowRangeStart,windowRangeEnd);
	});
	snap.forEach(function(snapDataTimeline){
		snapDataTimeline.setTimelineWindow(windowRangeStart,windowRangeEnd);
	});
}
