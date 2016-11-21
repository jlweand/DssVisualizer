var Screenshot = function(snapData){
	snapData.forEach(function(obj){ obj['group'] = '0';});

	// DOM element where the Timeline will be attached
	var container = document.getElementById("screenshotData");

	// Create a DataSet (allows two way data-binding)
	var groups = new vis.DataSet();
	groups.add({id: 0, content: 'Snap'});

	var items = new vis.DataSet(snapData);

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
					// var groupName = dataNames[item.group];
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

	// Create a Timeline
	this.timeline = new vis.Timeline(container, items, groups, options);

	$("#screenshotData").removeClass("hidden");

	this.timeline.on('select', function (properties) {
		var currItem = properties.items;
		items.forEach(function(data){
			if(data['id'] == currItem){
				console.log(data);
				prettyPrompt(data);
			}
		})
	});
	this.timeline.on('rangechanged', getRangeChanged);

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
			var isImage = item['classname'] != null && item['classname'] == 'imgPoint';
			if(key != 'classname'){
				if(key == 'title' && isImage){
					text += "<tr>";
					text += "<td>"+key+":</td>";
					text += "<td>"+item[key]+"<br><img src='"+item[key]+"'/></td>";
					text += "</tr>";
				}
				else{
					text += "<tr>";
					text += "<td>"+key+":</td>";
					text += "<td>"+item[key]+"</td>";
					text += "</tr>";
				}
			}
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
				if(key != 'start' && key != 'annotation' && key != 'group' && key != 'id' && key != 'fixed' && key != 'type' && key != '_id' && key != 'timed_id' && key != 'keypress_id' && key != 'clicks_id'  && key != 'metadata'){
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
}


Screenshot.prototype.setTimelineWindow = function(start,end){
this.timeline.setWindow(start,end);
//this.timeline.redraw();
}
