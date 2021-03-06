var PCAPData = function(meXY, meAll, miXY, miAll, tsXY, tsAll){
	var containerME = document.getElementById("multiExcludeData");
	var containerMI = document.getElementById("multiIncludeData");
	var containerTS = document.getElementById("tsharkData");

	var datasetMEXY = new vis.DataSet(meXY);
	var datasetMIXY = new vis.DataSet(miXY);
	var datasetTSXY = new vis.DataSet(tsXY);
	this.datasetMEAll = new vis.DataSet(meAll);
	this.datasetMIAll = new vis.DataSet(miAll);
	this.datasetTSAll = new vis.DataSet(tsAll);
    var theMEAllItems = this.datasetMEAll;
    var theMIAllItems = this.datasetMIAll;
    var theTSAllItems = this.datasetTSAll;
    
  
	// get data start and end date
	startDate = datasetMEXY.min('id')['x'];
	endDate = datasetMEXY.max('id')['x'];
	var anHour = 1000 * 60 * 60;
	startDate = JSONDatetoMillis(startDate) - anHour;
	endDate = JSONDatetoMillis(endDate) + anHour;
	maxZoom = endDate - startDate;

	var optionsXY = {
		// limit viewing window to startdate and end date
		min: startDate,
		max: endDate,
		//limit zoomin to 30 sec
		zoomMin: 1000 * 30,
		//limit zoom out to whole data set
		zoomMax: maxZoom,
		drawPoints: true,
		interpolation: false,
		height: "150px",
		showMinorLabels: false,
		showMajorLabels: false,
		dataAxis: {visible: false}
	};
	var optionsAll = {
		// limit viewing window to startdate and end date
		min: startDate,
		max: endDate,
		//limit zoomin to 1 min
		zoomMin: 1000 * 60,
		//limit zoom out to 1 day
		zoomMax: 1000 * 60 * 30,
		stack: false,
		dataAttributes: 'all',
		editable: true,
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
					var groupName = metaDataItem.group;
					$.get("http://localhost?submission=annotation&itemID="+currItem+"&type="+groupName+"&annotation="+value+"&annotation="+value+"&eventName="+eventName+"&techName="+techName+"&start="+itemDateString);
					callback(item); // send back adjusted new item
				}
				else {
					callback(null); // cancel item creation
				}
			});
		},
		onUpdate: function(item, callback){
			// 	  $.get("http://localhost?submission=annotation&itemID="+currItem+"&type="+groupName+"&annotation="+value);
			prettyPrompt(item, groupName, callback);
		},
		onRemove: function(item, callback) {
            prettyConfirm('Remove item', 'Do you really want to remove item ' + item.content + '?', function (ok) {
                if (ok) {
                    $.get("http://localhost?submission=edit&editType=delete&itemID="+item.id+"&type="+groupName+"&start="+item.start);
                    callback(item); /* confirm deletion */
                }
                else {
                    callback(null); /* cancel deletion */
                }
            });
		}
	};


	this.graph2dME = new vis.Graph2d(containerME, datasetMEXY, optionsXY);
	this.timelineME = new vis.Timeline(containerME, this.datasetMEAll, optionsAll);
	this.graph2dMI = new vis.Graph2d(containerMI, datasetMIXY, optionsXY);
	this.timelineMI = new vis.Timeline(containerMI, this.datasetMIAll, optionsAll);
	this.graph2dTS = new vis.Graph2d(containerTS, datasetTSXY, optionsXY);
	this.timelineTS = new vis.Timeline(containerTS, this.datasetTSAll, optionsAll);

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

    // this weirdness sets the groupname (for the python) for deleting items.
    var groupName;
	this.timelineME.on('select', function (properties) {
		groupName = 'multi_exclude';
	});
	this.timelineMI.on('select', function (properties) {
		groupName = 'multi_include';
	});
	this.timelineTS.on('select', function (properties) {
		groupName = 'tshark';
	});

	// this weird thing is to get the event/tech name to add to the timeline annotation.
    var metaDataItem;
    this.timelineME.on('doubleClick', function(properties){
        var firstChildItemOfTimeline = properties.event.firstTarget.firstChild;
        try {
            var firstChildId = firstChildItemOfTimeline.getAttribute("data-id");
            theMEAllItems.forEach(function(data){
                if(data['id'] == firstChildId){
                    metaDataItem = data;
                    metaDataItem.group = 'multi_exclude';
                    return;
                }
            })
        } catch(TypeError) {}
    });
	// this weird thing is to get the event/tech name to add to the timeline annotation.
    this.timelineMI.on('doubleClick', function(properties){
        var firstChildItemOfTimeline = properties.event.firstTarget.firstChild;
        try {
            var firstChildId = firstChildItemOfTimeline.getAttribute("data-id");
            theMIAllItems.forEach(function(data){
                if(data['id'] == firstChildId){
                    metaDataItem = data;
                    metaDataItem.group = 'multi_include';
                    return;
                }
            })
        } catch(TypeError) {}
    });
	// this weird thing is to get the event/tech name to add to the timeline annotation.
    this.timelineTS.on('doubleClick', function(properties){
        var firstChildItemOfTimeline = properties.event.firstTarget.firstChild;
        try {
            var firstChildId = firstChildItemOfTimeline.getAttribute("data-id");
            theTSAllItems.forEach(function(data){
                if(data['id'] == firstChildId){
                    metaDataItem = data;
                    metaDataItem.group = 'tshark';
                    return;
                }
            })
        } catch(TypeError) {}
    });
	function JSONDatetoMillis(date){
		var theDate = date.split(/-|:| /);
		
		var d = new Date(theDate[0],theDate[1]-1,theDate[2],theDate[3],theDate[4],theDate[5]);
		return d.getTime();
	}
    

}

function replaceNewLines(text){
	var newText = "<div><table style='text-align: left'><tr><td>";
	newText += text.replace(/\n/g, "</td></tr><tr><td>");
	newText += "</td></tr></table><div>";
	return newText;
}

PCAPData.prototype.getMEDataset = function(){
	return this.datasetMEAll;
}
PCAPData.prototype.getMIDataset = function(){
	return this.datasetMIAll;
}
PCAPData.prototype.getTSDataset = function(){
	return this.datasetTSAll;
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
