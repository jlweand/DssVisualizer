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
			prettyPrompt(item, callback);
		}
	};

	// Create a Timeline
	this.timeline = new vis.Timeline(container, items, groups, options);

	$("#screenshotData").removeClass("hidden");

	this.timeline.on('select', function (properties) {
		var currItem = properties.items;
		items.forEach(function(data){
			if(data['id'] == currItem){
				// console.log(data);
				// prettyPrompt(data);
			}
		})
	});
	this.timeline.on('rangechanged', getRangeChanged);
}


Screenshot.prototype.setTimelineWindow = function(start,end){
	this.timeline.setWindow(start,end);
	//this.timeline.redraw();
}
