$(document).on("click", "#dateInput", function(){
	$("#loading").removeClass("hidden");
	$("#pcapData").addClass("hidden");
	$("#multiExcludeData").html("");
	$("#multiIncludeData").html("");
	$("#tsharkData").html("");
	var start = $("#datepickerStart").val();
	var end = $("#datepickerEnd").val();
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
	var pcapDataUrl = "http://localhost?request=pcapData&startDate="+start+"&endDate="+end;
	$.get(pcapDataUrl);
});

function visPCAPData(meXY, meAll, miXY, miAll, tsXY, tsAll){
	visMEData(meXY, meAll);
	visMIData(miXY, miAll);
	visTSData(tsXY, tsAll);
}

function visMEData(xyData, allData){
	xyData.forEach(function(xyObj){
		var xyTime = xyObj['x'];
		allData.forEach(function(allObj){
			var allTime = allObj['start'];
			if(allTime == xyTime){
				xyObj['label'] = {"content": allObj['content']};
			}
		});
	});
	var container = document.getElementById("multiExcludeData");
	var datasetME = new vis.DataSet(xyData);
	var options = {
		drawPoints: true,
		interpolation: false,
		height: "150px"
	};
	var graph2dME = new vis.Graph2d(container, datasetME, options);
	$("#loading").addClass("hidden");
	$("#multiExcludeData").removeClass("hidden");

	// alert("before select");
	graph2dME.on('click', function(properties){
		var currTime = new Date(properties.time);
		allData.forEach(function(allObj){
			var allTime = new Date(allObj['start'].replace(/-/g, "/").replace(/T/, " "));
			// var allTime = new Date(allObj['start']);
			var diff = Math.abs(currTime - allTime);
			var buffer = 100;
			// console.log(allObj['start']);
			// console.log(currTime+" - "+allTime+" = "+diff);
			if( diff < buffer){
				prettyPrompt(allObj['start'], allObj['title']);
			}
		});
	});
}

function visMIData(xyData, allData){
	xyData.forEach(function(xyObj){
		var xyTime = xyObj['x'];
		allData.forEach(function(allObj){
			var allTime = allObj['start'];
			if(allTime == xyTime){
				xyObj['label'] = {"content": allObj['content']};
			}
		});
	});
	var container = document.getElementById("multiIncludeData");
	var datasetMI = new vis.DataSet(xyData);
	var options = {
		drawPoints: true,
		interpolation: false,
		height: "150px"
	};
	var graph2dMI = new vis.Graph2d(container, datasetMI, options);
	$("#loading").addClass("hidden");
	$("#multiIncludeData").removeClass("hidden");

	// alert("before select");
	graph2dMI.on('click', function(properties){
		var currTime = new Date(properties.time);
		allData.forEach(function(allObj){
			var allTime = new Date(allObj['start'].replace(/-/g, "/").replace(/T/, " "));
			var diff = Math.abs(currTime - allTime);
			var buffer = 100;
			// alert(currTime+" - "+allTime+" = "+diff);
			if( diff < buffer){
				prettyPrompt(allObj['start'], allObj['title']);
			}
		});
	});
}

function visTSData(xyData, allData){
	xyData.forEach(function(xyObj){
		var xyTime = xyObj['x'];
		allData.forEach(function(allObj){
			var allTime = allObj['start'];
			if(allTime == xyTime){
				xyObj['label'] = {"content": allObj['content']};
			}
		});
	});
	var container = document.getElementById("tsharkData");
	var datasetTS = new vis.DataSet(xyData);
	var options = {
		drawPoints: true,
		interpolation: false,
		height: "150px"
	};
	var graph2dTS = new vis.Graph2d(container, datasetTS, options);
	$("#loading").addClass("hidden");
	$("#tsharkData").removeClass("hidden");

	// alert("before select");
	graph2dTS.on('click', function(properties){
		var currTime = new Date(properties.time);
		allData.forEach(function(allObj){
			var allTime = new Date(allObj['start'].replace(/-/g, "/").replace(/T/, " "));
			var diff = Math.abs(currTime - allTime);
			var buffer = 100;
			// alert(currTime+" - "+allTime+" = "+diff);
			if( diff < buffer){
				prettyPrompt(allObj['start'], allObj['title']);
				$(".sweet-alert").scrollTop(0);
			}
		});
	});
}

function prettyPrompt(title, text) {
	swal({title: title, text: text, html: true, allowOutsideClick: true});
}
