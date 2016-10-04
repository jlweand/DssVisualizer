$(document).ready(function(){
	var startDate = '2016-08-01 09:00:00';
	var endDate = '2016-09-16 10:00:00';
	var keypressDataUrl = "http://localhost?request=keypressData&startDate="+startDate+"&endDate="+endDate;
	// var clickDataUrl = "http://localhost?request=clickData&startDate="+startDate+"&endDate="+endDate;
	// var timedDataUrl = "http://localhost?request=timedData&startDate="+startDate+"&endDate="+endDate;
	$.get(keypressDataUrl);
});
function visData(keyData, clickData, timedData){
	var parsedJson = $.extend({}, keyData, clickData, timedData);
	if(typeof parsedJson == 'string'){
		parsedJson = JSON.parse(parsedJson);
	}

	// hide the "loading..." message
	document.getElementById('loading').style.display = 'none';

	// DOM element where the Timeline will be attached
	var container = document.getElementById("keypressData");
	// var container = $("#keypressData");

	// Create a DataSet (allows two way data-binding)
	var items = new vis.DataSet(keyData);
	items.add(clickData);
	items.add(timedData);

	// Configuration for the Timeline
	var options = {
		editable: true,

		onAdd: function (item, callback) {
			prettyPrompt('Add item', 'Enter text content for new item:', item.content, function (value) {
				if (value) {
					item.content = value;
					callback(item); // send back adjusted new item
				}
				else {
					callback(null); // cancel item creation
				}
			});
		},

		onMove: function (item, callback) {
			var title = 'Do you really want to move the item to\n' +
			'start: ' + item.start + '\n' +
			'end: ' + item.end + '?';

			prettyConfirm('Move item', title, function (ok) {
				if (ok) {
					callback(item); // send back item as confirmation (can be changed)
				}
				else {
					callback(null); // cancel editing item
				}
			});
		},

		onMoving: function (item, callback) {
			if (item.start < min) item.start = min;
			if (item.start > max) item.start = max;
			if (item.end   > max) item.end   = max;

			callback(item); // send back the (possibly) changed item
		},

		onUpdate: function (item, callback) {
			prettyPrompt('Update item', 'Edit items text:', item.content, function (value) {
				if (value) {
					item.content = value;
					callback(item); // send back adjusted item
				}
				else {
					callback(null); // cancel updating the item
				}
			});
		},

		onRemove: function (item, callback) {
			prettyConfirm('Remove item', 'Do you really want to remove item ' + item.content + '?', function (ok) {
				if (ok) {
					callback(item); // confirm deletion
				}
				else {
					callback(null); // cancel deletion
				}
			});
		},
		dataAttributes: 'all',
		template: function (item) {
			var display = item.content;
			if(display == " "){
				return '<img src="' + item.title + '" alt="time: '+ item.start +'"/>';
			}
			else{
		    	return '<p>' + item.content + '</p>';
			}
		  }
	};

	// Create a Timeline
	var timeline = new vis.Timeline(container, items, options);

	timeline.on('select', function (properties) {
		var currItem = properties.items;
		if(currItem != ""){
			var currItemContent = $('[data-id="'+currItem+'"]').attr('data-content');
			$("#annotationLabel").html("Please enter the annotation for: '"+currItemContent);
			$("#objID").val(currItem);
			$("#annotation").attr("disabled", false);
			$("#submitAnnotation").attr("disabled", false);
		}
		else{
			$("#annotationLabel").html("Please select an object.");
			$("#objID").val("");
			$("#annotation").attr("disabled", true);
			$("#submitAnnotation").attr("disabled", true);
		}
	});

	function logEvent(event, properties) {
		var log = document.getElementById('currentItem');
		var msg = document.createElement('div');
		msg.innerHTML = 'event=' + JSON.stringify(event) + ', ' +
		'properties=' + JSON.stringify(properties);
		log.firstChild ? log.insertBefore(msg, log.firstChild) : log.appendChild(msg);
	}
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
