var KeyLogger = function(keyData, clickData, timedData){
	keyData.forEach(function(obj){ obj['group'] = '0';});
	clickData.forEach(function(obj){ obj['group'] = '1';});
	timedData.forEach(function(obj){ obj['group'] = '2';});

	// DOM element where the Timeline will be attached
	var container = document.getElementById("keypressData");

	// Create a DataSet (allows two way data-binding)
	var dataNames = ['keypress', 'click', 'timed'];
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
					var eventName = metaDataItem.metadata.eventName;
					var techName = metaDataItem.metadata.techName;
					var isoDate = new Date(item.start);
					var itemDateString = isoDate.getFullYear()+"-"+(isoDate.getMonth()+1)+"-"+isoDate.getDate();
					var itemTimeHours = addLeadingZeroes(isoDate.getHours());
					var itemTimeMinutes = addLeadingZeroes(isoDate.getMinutes());
					var itemTimeSeconds = addLeadingZeroes(isoDate.getSeconds());
					itemDateString += " "+itemTimeHours+":"+itemTimeMinutes+":"+itemTimeSeconds;
					item.start = itemDateString;
					item.content = value;
					item.annotation = value;
					item.className = "annotation";
					var currItem = item.id;
					var groupName = dataNames[item.group];
					$.get("http://localhost?submission=annotation&itemID="+currItem+"&type="+groupName+"&annotation="+value+"&eventName="+eventName+"&techName="+techName+"&start="+itemDateString);
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
		},
		onRemove: function(item, callback) {
            prettyConfirm('Remove item', 'Do you really want to remove item ' + item.content + '?', function (ok) {
                 console.log(ok);
                if (ok) {
                    var groupName = dataNames[item.group];
                    $.get("http://localhost?submission=edit&editType=delete&itemID="+item.id+"&type="+groupName+"&start="+item.start);
                    callback(item); /* confirm deletion */
                }
                else {
                    callback(null); /* cancel deletion */
                }
            });
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

	// this weird thing is to get the event/tech name to add to the timeline annotation.
    var metaDataItem;
    this.timeline.on('doubleClick', function(properties){
        var firstChildItemOfTimeline = properties.event.firstTarget.firstChild;
        try {
            var firstChildId = firstChildItemOfTimeline.getAttribute("data-id");
            items.forEach(function(data){
                if(data['id'] == firstChildId){
                    metaDataItem = data;
                    return;
                }
            })
        } catch(TypeError) {}
    });

	this.timeline.on('rangechanged', getRangeChanged);

}
KeyLogger.prototype.setTimelineWindow = function(start,end){
	this.timeline.setWindow(start,end);
	//this.timeline.redraw();
}
