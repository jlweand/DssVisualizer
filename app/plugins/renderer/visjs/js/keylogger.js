var KeyLogger = function(keyData, clickData, timedData){
	keyData.forEach(function(obj){ obj['group'] = '0';});
	clickData.forEach(function(obj){ obj['group'] = '1';});
	timedData.forEach(function(obj){ obj['group'] = '2';});

	// DOM element where the Timeline will be attached
	var container = document.getElementById("keypressData");

	// Create a DataSet (allows two way data-binding)
	var dataNames = ['Keypresses', 'Clicks ', 'Timed'];
	var groups = new vis.DataSet();
	for(var g=0; g<3; g++){
		groups.add({id: g, content: dataNames[g]});
	}

	var items = new vis.DataSet(keyData);
	items.add(clickData);
	items.add(timedData);

	// Configuration for the Timeline
	var options = {
		// start: startDate,
		// end: endDate,
		maxHeight: 400,
		dataAttributes: 'all',
		template: function (item) {
			var display = item.content;
			if(display == " "){
				return '<div>Img ' + item.start + '</div>';
			}
			else{
		    	return '<div>' + item.content + '</div>';
			}
		},
		editable: true,
		onAdd: function(item, callback){
			prettyAdd('Add Annotation', function(value) {
				if (value) {
					item.content = "Annotation: "+value;
					// 		  console.log(value);
					item.annotation = value;
					var currItem = item.id;
					var groupName = dataNames[item.group];
					$.get("http://localhost?submission=annotation&itemID="+currItem+"&type="+groupName+"&annotation="+value);
					callback(item); // send back adjusted new item
				}
				else {
					callback(null); // cancel item creation
				}
			});
		},
		onUpdate: function(item, callback){
			// prettyEdit('Edit Item', item.content, item.annotation, function(value){
			// 	if (value) {
			// 		item.content = "Annotation: "+value;
			// 	  item.annotation = value;
			// 	  console.log(JSON.stringify(item));
			// 	  var currItem = item.id;
			// 	  var groupName = dataNames[item.group];
			// 	  $.get("http://localhost?submission=annotation&itemID="+currItem+"&type="+groupName+"&annotation="+value);
		    //       callback(item); // send back adjusted new item
		    //     }
		    //     else {
		    //       callback(null); // cancel item creation
		    //     }
			// });
			prettyEdit("Edit item", item, function(value){
				var startDate = value[0];
				var startDateArr = startDate.split("/");
				var startDateTime = new Date(value[0]+" "+value[1]+":"+value[2]+":"+value[3]);
				var content = value[4];
				var title = value[5];
				var comment = value[6];
				var annotation = value[7];
				// console.log(startDateTime.toISOString());
				item.content = content;
				item.title = title;
				item.start = startDateTime.toISOString();
				callback(item);
			});
		}
	};

	// Create a Timeline
	this.timeline = new vis.Timeline(container, items, groups, options);

	$("#loading").addClass("hidden");
	$("#keypressData").removeClass("hidden");

	this.timeline.on('doubleClick', function(properties){
		var currItem = properties.items;
	});

	this.timeline.on('select', function (properties) {
		var currItem = properties.items;
	});
	this.timeline.on('rangechanged', getRangeChanged);

	function prettyEdit(title, item, callback){
		var itemDateTime = new Date(item['start'].replace(/-/g, "/").replace(/T/, " "));
		var itemDateString = itemDateTime.getMonth()+"/"+itemDateTime.getDate()+"/"+itemDateTime.getFullYear();
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
		form += "<input type='number' id='editStartHours' name='editStartHours' value='"+itemTimeHours+"' min='0' max='23'/>";
		form += "<input type='number' id='editStartMinutes' name='editStartMinutes' value='"+itemTimeMinutes+"' min='0' max='59'/>";
		form += "<input type='number' id='editStartSeconds' name='editStartSeconds' value='"+itemTimeSeconds+"' min='0' max='59'/>";
		form += "</div>";
		// console.log(JSON.stringify(item));
		// var form = "";
		Object.keys(item).forEach(function(key){
			if(key == "content"){
				form += "<div style='border:none'>";
				form += "<label for='editContent'>Edit Content:</label>";
				form += "<input type='text' id='editContent' name='editContent' value='"+item[key]+"'/>";
				form += "</div>";
			}
			else if(key == "title"){
				form += "<div style='border:none'>";
				form += "<label for='editTitle'>Edit Title:</label>";
				form += "<input type='text' id='editTitle' name='editTitle' value='"+item[key]+"'/>";
				form += "</div>";
			}
			else if(key == "comment"){
				form += "<div style='border:none'>";
				form += "<label for='editComment'>Edit Comment:</label>";
				form += "<input type='text' id='editComment' name='editComment' value='"+item[key]+"'/>";
				form += "</div>";
			}
		});
		form += "<div style='border:none'>";
		form += "<label for='editAnnotation'>Edit Annotation:</label>";
		if(item['annotation'] == null){
			form += "<input type='text' id='editAnnotation' name='editAnnotation'/>";
		}
		else{
			form += "<input type='text' id='editAnnotation' name='editAnnotation' value='"+item['annotation']+"'/>";
		}
		form += "</div>";
		swal({
			title: title,
			html: form,
			showCancelButton: true,
			preConfirm: function(result) {
				return new Promise(function(resolve) {
					if (result) {
						resolve([
							$('#editStartDate').val(),
							$('#editStartHours').val(),
							$('#editStartMinutes').val(),
							$('#editStartSeconds').val(),
							$('#editContent').val(),
							$('#editTitle').val(),
							$('#editComment').val(),
							$('#editAnnotation').val()
						])
					}
				})
			}
		}).then(callback);
		var datePicker = $("#editStartDate").datepicker({
			defaultDate: itemDate,
			changeMonth: true,
			changeYear: true,
			maxDate: 0
		});
	}

}
KeyLogger.prototype.setTimelineWindow = function(start,end){
	this.timeline.setWindow(start,end);
	//this.timeline.redraw();
}
