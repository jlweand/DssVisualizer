$(document).ready(function(){
	// load data via an ajax request. When the data is in, load the timeline
	$.ajax({
		url: '../json/keypressData.json',
		success: function (data) {
			var parsedJson = data;
			if(typeof data == 'string'){
				parsedJson = JSON.parse(data);
			}

			// hide the "loading..." message
			document.getElementById('loading').style.display = 'none';

			// DOM element where the Timeline will be attached
			var container = document.getElementById('visualization');

			// Create a DataSet (allows two way data-binding)
			var items = new vis.DataSet(parsedJson);

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
				dataAttributes: 'all'
			};

			// Create a Timeline
			var timeline = new vis.Timeline(container, items, options);

			timeline.on('select', function (properties) {
				var currItem = properties.items;
				if(currItem != ""){
					var currItemContent = $('[data-id="'+currItem+'"]').attr('data-content');
					$("#annotationLabel").html("Please enter the annotation for: '"+currItemContent+"' ["+currItem+"]");
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
		},
		error: function (err) {
			console.log('Error', err);
			if (err.status === 0) {
				alert('Failed to load data/basic.json.\nPlease run this example on a server.');
			}
			else {
				alert('Failed to load data/basic.json.');
			}
		}
	});
});
