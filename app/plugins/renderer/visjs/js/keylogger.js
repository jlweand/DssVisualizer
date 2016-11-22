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
		stack: false,
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
			// 	  $.get("http://localhost?submission=annotation&itemID="+currItem+"&type="+groupName+"&annotation="+value);
			prettyPrompt(item, callback);
		}
	};

	// Create a Timeline
	this.timeline = new vis.Timeline(container, items, groups, options);
	$("#keypressData").removeClass("hidden");

	// this.timeline.on('select', function (properties) {
	// 	var currItem = properties.items;
	// 	items.forEach(function(data){
	// 		if(data['id'] == currItem){
	// 			prettyPrompt(data);
	// 		}
	// 	});
	// });

	// this.timeline.on('doubleClick', function(properties){
	// 	var firstChildItemOfTimeline = properties.event.firstTarget.firstChild;
	// 	var firstChildMetadata = firstChildItemOfTimeline.getAttribute("data-id");
	// 	console.log(firstChildMetadata);
	// });

	this.timeline.on('rangechanged', getRangeChanged);

}
KeyLogger.prototype.setTimelineWindow = function(start,end){
	this.timeline.setWindow(start,end);
	//this.timeline.redraw();
}
