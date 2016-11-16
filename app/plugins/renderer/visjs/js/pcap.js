var PCAPData = function(meXY, meAll, miXY, miAll, tsXY, tsAll){
	var containerME = document.getElementById("multiExcludeData");
	var containerMI = document.getElementById("multiIncludeData");
	var containerTS = document.getElementById("tsharkData");

	var datasetMEXY = new vis.DataSet(meXY);
	var datasetMIXY = new vis.DataSet(miXY);
	var datasetTSXY = new vis.DataSet(tsXY);
	var datasetMEAll = new vis.DataSet(meAll);
	var datasetMIAll = new vis.DataSet(miAll);
	var datasetTSAll = new vis.DataSet(tsAll);

	var optionsXY = {
		drawPoints: true,
		interpolation: false,
		height: "150px",
		showMinorLabels: false,
		showMajorLabels: false,
		dataAxis: {visible: false}
	};
	var optionsAll = {
		stack: false,
		editable: {
			add: true,
			updateTime: true,
			updateGroup: true
		},
		onAdd: function(item, callback){
			prettyAdd('Add Annotation', function(value) {
				if (value) {
					var isoDate = new Date(item.start);
					var itemDateString = isoDate.getFullYear()+"-"+(isoDate.getMonth()+1)+"-"+isoDate.getDate();
					var itemTimeHours = addLeadingZeroes(isoDate.getHours());
					var itemTimeMinutes = addLeadingZeroes(isoDate.getMinutes());
					var itemTimeSeconds = addLeadingZeroes(isoDate.getSeconds());
					itemDateString += " "+itemTimeHours+":"+itemTimeMinutes+":"+itemTimeSeconds;
					item.start = itemDateString;
					item.content = "Annotation: "+value;
					item.annotation = value;
					var currItem = item.id;
					var groupName = "";
					// $.get("http://localhost?submission=annotation&itemID="+currItem+"&type="+groupName+"&annotation="+value);
					callback(item); // send back adjusted new item
				}
				else {
					callback(null); // cancel item creation
				}
			});
		},
		onUpdate: function(item, callback){
			// 	  $.get("http://localhost?submission=annotation&itemID="+currItem+"&type="+groupName+"&annotation="+value);
			prettyEdit("Edit item", item, function(value){
				var startHour = addLeadingZeroes(value['startHours']);
				var startMinutes = addLeadingZeroes(value['startMinutes']);
				var startSeconds = addLeadingZeroes(value['startSeconds']);
				var startDateTime = value['startDate']+" "+startHour+":"+startMinutes+":"+startSeconds;
				item['start'] = startDateTime;
				Object.keys(value).forEach(function(key){
					if(key != 'startDate' && key != 'startHours' && key != 'startMinutes' && key != 'startSeconds'){
						item[key] = value[key];
					}
				});
				callback(item);
			});
		}
	};


	this.graph2dME = new vis.Graph2d(containerME, datasetMEXY, optionsXY);
	this.timelineME = new vis.Timeline(containerME, datasetMEAll, optionsAll);
	this.graph2dMI = new vis.Graph2d(containerMI, datasetMIXY, optionsXY);
	this.timelineMI = new vis.Timeline(containerMI, datasetMIAll, optionsAll);
	this.graph2dTS = new vis.Graph2d(containerTS, datasetTSXY, optionsXY);
	this.timelineTS = new vis.Timeline(containerTS, datasetTSAll, optionsAll);


	$("#loading").addClass("hidden");
	$("#multiExcludeData").removeClass("hidden");
	$("#multiIncludeData").removeClass("hidden");
	$("#tsharkData").removeClass("hidden");

	var xBuffer = 100;
	var yBuffer = 5;

	this.graph2dME.on('rangechanged', getRangeChanged);
	this.timelineME.on('rangechanged', getRangeChanged);
	this.graph2dMI.on('rangechanged', getRangeChanged);
	this.timelineMI.on('rangechanged', getRangeChanged);
	this.graph2dTS.on('rangechanged', getRangeChanged);
	this.timelineTS.on('rangechanged', getRangeChanged);

	this.timelineME.on('select', function (properties) {
		var currItem = properties.items;
		datasetMEAll.forEach(function(data){
			if(data['id'] == currItem){
				console.log(data);
				prettyPrompt(data);
			}
		})
	});
	this.timelineMI.on('select', function (properties) {
		var currItem = properties.items;
		datasetMIAll.forEach(function(data){
			if(data['id'] == currItem){
				console.log(data);
				prettyPrompt(data);
			}
		})
	});
	this.timelineTS.on('select', function (properties) {
		var currItem = properties.items;
		datasetTSAll.forEach(function(data){
			if(data['id'] == currItem){
				console.log(data);
				prettyPrompt(data);
			}
		})
	});
}

function prettyPrompt(item){
	var title = item.start;
	var text = formatObjectForDisplay(item);
	swal({
		title: title,
		html: text,
		width: '90%'
	});
}

function formatObjectForDisplay(item){
	var text = "<div><table>";
	Object.keys(item).forEach(function(key){
		text += "<tr>";
		text += "<td>"+key+":</td>";
		text += "<td>"+item[key]+"</td>";
		text += "</tr>";
	});
	text += "</table></div>";
	return text;
}

function prettyEdit(title, item, callback){

	var dateFormat = "yy-mm-dd";
	var itemDateTime = new Date(item['start'].replace(/-/g, "/").replace(/T/, " "));
	var itemDateString = itemDateTime.getFullYear()+"-"+(itemDateTime.getMonth()+1)+"-"+itemDateTime.getDate();
	var itemDate = new Date(itemDateString);
	var itemTimeHours = itemDateTime.getHours();
	var itemTimeMinutes = itemDateTime.getMinutes();
	var itemTimeSeconds = itemDateTime.getSeconds();
	var form = "<div style='border:none'>";
	form += "<label for='editStartDate'>Edit start date:</label>";
	form += "<input type='text' id='editStartDate' name='editStartDate' value='"+itemDateString+"'/>";
	form += "</div>";
	form += "<div style='border:none'>";
	form += "<label for='editStartHours'>Edit start time:</label>";
	form += "<input type='number' id='editStartHours' name='editStartHours' value='"+itemTimeHours+"' min='0' max='23'/>h ";
	form += "<input type='number' id='editStartMinutes' name='editStartMinutes' value='"+itemTimeMinutes+"' min='0' max='59'/>m ";
	form += "<input type='number' id='editStartSeconds' name='editStartSeconds' value='"+itemTimeSeconds+"' min='0' max='59'/>s";
	form += "</div>";

	Object.keys(item).forEach(function(key){
		if(key != "classname" && key != "className"){
			// if(item['classname'] != "imgPoint"){
			if(key != 'start' && key != 'annotation' && key != 'group' && key != 'id' && key != 'type' && key != 'traffic_all_id' && key != 'metadata' && key != '_id'){
				if(key == 'content' && (item['content'] != ' ' || item['content'] != '')){
					form += "<div style='border:none'>";
					form += "<label for='edit"+key+"'>Edit "+key+":</label>";
					form += "<textarea id='edit"+key+"' name='edit"+key+"'>"+item[key]+"</textarea>";
					form += "</div>";
				}
				else{
					form += "<div style='border:none'>";
					form += "<label for='edit"+key+"'>Edit "+key+":</label>";
					form += "<input type='text' id='edit"+key+"' name='edit"+key+"' value='"+item[key]+"'/>";
					form += "</div>";
				}
			}
		}
	});
	form += "<div style='border:none'>";
	form += "<label for='editAnnotation'>Edit Annotation:</label>";
	if(item['annotation'] == null){
		form += "<textarea id='editAnnotation' name='editAnnotation'></textarea>";
	}
	else{
		form += "<textarea id='editAnnotation' name='editAnnotation'>"+item['annotation']+"</textarea>";
	}
	form += "</div>";

	swal({
		title: title,
		html: form,
		showCancelButton: true,
		width: '90%',
		preConfirm: function(result) {
			return new Promise(function(resolve) {
				if (result) {
					var jsonResults = {
						"startDate": $('#editStartDate').val(),
						"startHours": $('#editStartHours').val(),
						"startMinutes": $('#editStartMinutes').val(),
						"startSeconds": $('#editStartSeconds').val(),
						"annotation": $('#editAnnotation').val()
					};
					Object.keys(item).forEach(function(key){
						if(key != "classname" && key != "className"){
							// if(item['classname'] != "imgPoint"){
							if(key != 'start' && key != 'annotation' && key != 'group' && key != 'id'){
								jsonResults[key] = $('#edit'+key).val();
							}
						}
					});
					resolve(jsonResults);
				}
			})
		}
	}).then(callback);
	var datePicker = $("#editStartDate").datepicker({
		defaultDate: itemDate,
		changeMonth: true,
		changeYear: true,
		maxDate: 0,
		dateFormat: dateFormat
	});
}

function replaceNewLines(text){
	var newText = "<div><table style='text-align: left'><tr><td>";
	newText += text.replace(/\n/g, "</td></tr><tr><td>");
	newText += "</td></tr></table><div>";
	return newText;
}

PCAPData.prototype.setPcapWindows = function (start,end){
	this.graph2dME.setWindow(start,end);
	this.timelineME.setWindow(start,end);
	this.graph2dMI.setWindow(start,end);
	this.timelineMI.setWindow(start,end);
	this.graph2dTS.setWindow(start,end);
	this.timelineTS.setWindow(start,end);
	//this.graph2dTS.redraw();
	//this.graph2dME.redraw();
	//this.graph2dMI.redraw();
}
