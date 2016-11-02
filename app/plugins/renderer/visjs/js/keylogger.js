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
	$("#keypressData").removeClass("hidden");

	timeline.on('doubleClick', function(properties){
		var currItem = properties.items;
	});

	timeline.on('select', function (properties) {
		var currItem = properties.items;
		// var title = currItem.start;
		// var text = "";
		// if(currItem.annotation){
		// 	text = currItem.annotation;
		// }
		// prettyDisplay(title, text);
	});

	// function prettyDisplay(title, text){
	// 	swal({
	// 		title: title,
	// 		text: text
	// 	});
	// }

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

	// function prettyAdd(title, callback){
	// 	var form = "<div style='border: none'>";
	// 	form += "<label for='addStart'>Select start date:</label>";
	// 	form += "<input type='text' id='addEventDatePicker' name='addStart' size='30'/>";
	// 	form += "</div><div style='border: none'>";
	// 	form += "<label for='annotation'>Enter the annotation:</label>";
	// 	form += "<input type='text' id='annotation' name='annotation'/>"
	// 	form += "</div>";
	// 	swal({
	// 		title: title,
	// 		html: form,
	// 		preConfirm: function(result) {
	// 			return new Promise(function(resolve) {
	// 				if (result) {
	// 					resolve([
	// 						$('#addEventDatePicker').val(),
	// 						$('#annotation').val()
	// 					])
	// 				}
	// 			})
	// 		}
	// 	}).then(callback);
	// 	var datePicker = $("#addEventDatePicker").datepicker({
	// 		defaultDate:"+1w",
	// 		changeMonth: true,
	// 		changeYear: true,
	// 		maxDate: 0
	// 	});
	// }

	// function prettyEdit(title, text, )
}
