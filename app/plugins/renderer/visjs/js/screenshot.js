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
		editable: true,
		onAdd: function(item, callback){
			prettyAdd('Add Annotation', function(value) {
				if (value) {
		          item.content = "Annotation: "+value;
  		// 		  console.log(value);
				  item.annotation = value;
				  console.log(JSON.stringify(item));
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
			prettyEdit('Edit Item', item.content, item.annotation, function(value){
				if (value) {
					item.content = "Annotation: "+value;
				  item.annotation = value;
				  console.log(JSON.stringify(item));
				  var currItem = item.id;
				  var groupName = dataNames[item.group];
				  $.get("http://localhost?submission=annotation&itemID="+currItem+"&type="+groupName+"&annotation="+value);
		          callback(item); // send back adjusted new item
		        }
		        else {
		          callback(null); // cancel item creation
		        }
			});
		}
	};

	// Create a Timeline
	var timeline = new vis.Timeline(container, items, groups, options);

	$("#loading").addClass("hidden");
	$("#screenshotData").removeClass("hidden");

	timeline.on('doubleClick', function(properties){
		var currItem = properties.items;
	});

	timeline.on('select', function (properties) {
		var currItem = properties.items;
	});

	function prettyAdd(title, callback){
		swal({
			title: title,
			input: 'textarea',
			showCancelButton: true
		}).then(callback);
	}

	function prettyEdit(title, text, inputValue, callback){
		swal({
			title: title,
			text: text,
			input: "textarea",
			inputValue: inputValue,
			showCancelButton: true
		}).then(callback);
	}
}
