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
		  }
	};

	// Create a Timeline
	var timeline = new vis.Timeline(container, items, groups, options);

	$("#loading").addClass("hidden");
	$("#keypressData").removeClass("hidden");

	timeline.on('doubleClick', function(properties){
		var currItem = properties.items;
	});

	timeline.on('select', function (properties) {
		var currItem = properties.items;
		addAnnotation(currItem);
	});

	function prettyConfirm(title, text, callback) {
		swal({
			title: title,
			text: text,
			type: 'warning',
			showCancelButton: true,
			confirmButtonColor: "#DD6B55"
		}, callback);
	}

	function prettyPrompt(title, text, inputValue, callback) {
		swal({
			title: title,
			text: text,
			type: 'input',
			showCancelButton: true,
			inputValue: inputValue
		}, callback);
	}
}
