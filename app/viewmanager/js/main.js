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
	var techName = $("#techName").val();
	var eventName = $("#eventName").val();
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
	var keypressDataUrl = "http://localhost?request=keypressData&startDate="+start+"&endDate="+end+"&techName="+techName+"&eventName="+eventName;
	$.get(keypressDataUrl);
	var pcapDataUrl = "http://localhost?request=pcapData&startDate="+start+"&endDate="+end+"&techName="+techName+"&eventName="+eventName;
	$.get(pcapDataUrl);
	var screenshotDataUrl = "http://localhost?request=screenshotData&startDate="+start+"&endDate="+end+"&techName="+techName+"&eventName="+eventName;
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
function visualizeKeyData(keyData, clickData, timedData){
	keyData.forEach(function(obj){
		obj['type'] = ['box'];
	});
	clickData.forEach(function(obj){
		obj['type'] = ['box'];
	});
	timedData.forEach(function(obj){
		obj['type'] = ['box'];
	});
	keylogger = new KeyLogger(keyData, clickData, timedData);
}

function visualizePCAPData(meXY, meAll, miXY, miAll, tsXY, tsAll){
	meXY.forEach(function(xyObj){
		var xyTime = xyObj['x'];
		meAll.forEach(function(allObj){
			var allTime = allObj['start'];
			if(allTime == xyTime){
				xyObj['label'] = {"content": allObj['content']};
			}
		});
	});
	miXY.forEach(function(xyObj){
		var xyTime = xyObj['x'];
		miAll.forEach(function(allObj){
			var allTime = allObj['start'];
			if(allTime == xyTime){
				xyObj['label'] = {"content": allObj['content']};
			}
		});
	});
	tsXY.forEach(function(xyObj){
		var xyTime = xyObj['x'];
		tsAll.forEach(function(allObj){
			var allTime = allObj['start'];
			if(allTime == xyTime){
				xyObj['label'] = {"content": allObj['content']};
			}
		});
	});
	pcapData = new PCAPData(meXY, meAll, miXY, miAll, tsXY, tsAll);
}

function visualizeSnapshotData(snapData){
	snapData.forEach(function(obj){
		obj['type'] = ['box'];
	});
	snap = new Screenshot(snapData);
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
	//alert('start:' + properties.start + ' end:' + properties.end)
	//start = properties.start
	//end = properties.end
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
			//alert('start: ' + windowRangeStart + ' end: ' + windowRangeEnd);

			$(document).ready(function(){

					$.get("http://dssvisualizer.py/exportData",{start:windowRangeStart,end:windowRangeEnd,techName:techExport,eventName:eventExport});

			});
		}
}
function populateTechDropdown(techList) {
  for(var i=0; i<techList.length; i++) {
		console.log(techList[i]);
    $("#techOptions").append('<option value='+techList[i]+'>'+techList[i]+'</option>')
  }
	$("#techOptions").trigger("chosen:updated");
}

// Add populateEventDropdown method here

$(document).ready(function() {
  var getTechNames = "http://localhost?populateDropdown=availableTechNames";
  $.get(getTechNames);
	//get the event names here
});
