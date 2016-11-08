$(document).on("click", "#dateInput", function(){
	$("#loading").removeClass("hidden");
	$("#keypressData").html("");
	$("#multiExcludeData").html("");
	$("#multiIncludeData").html("");
	$("#tsharkData").html("");
	$("#screenshotData").html("");

	var start = $("#datepickerStart").val();
	var end = $("#datepickerEnd").val();
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

$(document).ready(function() {
    $('#keylogger').val($(this).is(':checked'));
    $('#multiexclude').val($(this).is(':checked'));
    $('#multiinclude').val($(this).is(':checked'));
    $('#tshark').val($(this).is(':checked'));
    $('#snapshots').val($(this).is(':checked'));
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
	var keylogger = new KeyLogger(keyData, clickData, timedData);
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
	var pcapData = new PCAPData(meXY, meAll, miXY, miAll, tsXY, tsAll);
}

function visualizeSnapshotData(snapData){
	snapData.forEach(function(obj){
		obj['type'] = ['box'];
	});
	var snap = new Screenshot(snapData);
}

