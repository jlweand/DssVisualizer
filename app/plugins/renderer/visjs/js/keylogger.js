$(document).ready(function(){
	var startDate = '2016-09-01 09:00:00';
	var endDate = '2016-09-16 10:00:00';
	var keypressDataUrl = "http://localhost?request=keypressData&startDate="+startDate+"&endDate="+endDate;
	$.get(keypressDataUrl);
});
$("#dateInput").click(function(){
	var start = $("#datepickerStart").val();
	var end = $("#datepickerStart").val();
	if(start == ""){
		start = '2000-01-01 00:00:00';
	}
	else{
		start = start + " 00:00:00";
	}
	if(end == ""){
		end = '3000-01-01 00:00:00';
	}
	else{
		end = end + " 00:00:00";
	}
	var keypressDataUrl = "http://localhost?request=keypressData&startDate="+start+"&endDate="+end;
	$.get(keypressDataUrl);
});
function visData(keyData, clickData, timedData){
	var parsedJson = $.extend({}, keyData, clickData, timedData);
	if(typeof parsedJson == 'string'){
		parsedJson = JSON.parse(parsedJson);
	}

	keyData.forEach(function(obj){ obj['group'] = '0'; });
	clickData.forEach(function(obj){ obj['group'] = '1'; });
	timedData.forEach(function(obj){ obj['group'] = '2'; });

	// var startDate = '2016-09-01 09:00:00';
	// var endDate = '2016-09-16 10:00:00';

	// hide the "loading..." message
	// document.getElementById('loading').style.display = 'none';

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
				return '<p>Img ' + item.start + '</p>';
			}
			else{
		    	return '<p>' + item.content + '</p>';
			}
		  }
	};

	// Create a Timeline
	var timeline = new vis.Timeline(container, items, groups, options);

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
