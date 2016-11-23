function prettyAdd(title, callback){
	swal({
		title: title,
		input: 'textarea',
		confirmButtonText: 'Add',
		showCancelButton: true
	}).then(callback);
}

function prettyConfirm(title, text, callback) {
    swal({
      title: title,
      text: text,
      type: 'warning',
      showCancelButton: true,
      confirmButtonColor: "#DD6B55"
    }).then(callback);
}

function prettyPrompt(item, groupName, callback){
	var title = item.start;
	var text = formatObjectForDisplay(item);
	var form = getEditForm(item);
	swal.setDefaults({
		confirmButtonText: 'Edit',
		showCancelButton: true,
		animation: false
	});
	var resultsFromForm = {};
	var steps = [
		{
			title: title,
			html: text,
			width: '90%'
		},
		{
			title: 'Editing: '+title,
			html: form,
			width: '90%',
			confirmButtonText: 'Submit',
			preConfirm: function(result) {
				return new Promise(function(resolve) {
					if (result) {
						var jsonResults = {
							"startDate": $('#editStartDate').val(),
							"startHours": $('#editStartHours').val(),
							"startMinutes": $('#editStartMinutes').val(),
							"startSeconds": $('#editStartSeconds').val(),
							"annotation": $('#editAnnotation').val()
						};
						Object.keys(item).forEach(function(key){
							if(arrayOfEditIncludedAttr.indexOf(key)>-1){
								jsonResults[key] = $('#edit'+key).val();
							}
						});
						resultsFromForm = jsonResults;
						resolve(jsonResults);
					}
				})
			}
		}
	];

	swal.queue(steps).then(function(ok){
            var value = resultsFromForm;
            var startHour = addLeadingZeroes(value['startHours']);
            var startMinutes = addLeadingZeroes(value['startMinutes']);
            var startSeconds = addLeadingZeroes(value['startSeconds']);
            var startDateTime = value['startDate']+" "+startHour+":"+startMinutes+":"+startSeconds;
            item['start'] = startDateTime;

            urlString = "http://localhost?submission=edit&editType=edit&itemID="+item.id+"&type="+groupName+"&start="+startDateTime;
            Object.keys(value).forEach(function(key){
                if(key != 'startDate' && key != 'startHours' && key != 'startMinutes' && key != 'startSeconds'){
                    urlString = urlString + "&"+key+"="+value[key]
                    item[key] = value[key];
                }
            });
            $.get(urlString);
            callback(item);
	});
}

//array of attributes included for editing.
//start and annotations not included because they are handled separately
var arrayOfEditIncludedAttr = ['content', 'title', 'comment'];

function getEditForm(item){
	var dateFormat = "yy-mm-dd";
	var itemDateTime = new Date(item['start'].replace(/-/g, "/").replace(/T/, " "));
	var itemDateString = itemDateTime.getFullYear()+"-"+(itemDateTime.getMonth()+1)+"-"+itemDateTime.getDate();
	var itemDate = new Date(itemDateString);
	var itemTimeHours = itemDateTime.getHours();
	var itemTimeMinutes = itemDateTime.getMinutes();
	var itemTimeSeconds = itemDateTime.getSeconds();
	var form = "<div style='border:none'>";
	form += "<label for='editStartDate'>Edit start date:</label>";
	form += "<input type='text' id='editStartDate' name='editStartDate' value='"+itemDateString+"'/>";
	form += "</div>";
	form += "<div style='border:none'>";
	form += "<label for='editStartHours'>Edit start time:</label>";
	form += "<input type='number' id='editStartHours' name='editStartHours' value='"+itemTimeHours+"' min='0' max='23'/>h ";
	form += "<input type='number' id='editStartMinutes' name='editStartMinutes' value='"+itemTimeMinutes+"' min='0' max='59'/>m ";
	form += "<input type='number' id='editStartSeconds' name='editStartSeconds' value='"+itemTimeSeconds+"' min='0' max='59'/>s";
	form += "</div>";

	Object.keys(item).forEach(function(key){
		if(arrayOfEditIncludedAttr.indexOf(key)>-1){
			form += "<div style='border:none'>";
			form += "<label for='edit"+key+"'>Edit "+key+":</label>";
			form += "<textarea id='edit"+key+"' name='edit"+key+"'>"+item[key]+"</textarea>";
			form += "</div>";
		}
	});
	form += "<div style='border:none'>";
	form += "<label for='editAnnotation'>Edit Annotation:</label>";
	if(item['annotation'] == null){
		form += "<textarea id='editAnnotation' name='editAnnotation'></textarea>";
	}
	else{
		form += "<textarea id='editAnnotation' name='editAnnotation'>"+item['annotation']+"</textarea>";
	}
	form += "</div>";
	var datePicker = $("#editStartDate").datepicker({
		defaultDate: itemDate,
		changeMonth: true,
		changeYear: true,
		maxDate: 0,
		dateFormat: dateFormat
	});
	return form;
}

function formatObjectForDisplay(item){
	var text = "<div><table>";
	Object.keys(item).forEach(function(key){
		var isImage = item['classname'] != null && item['classname'] == 'imgPoint';
		if(key != 'classname' && typeof item[key] !== 'object'){
			if(key == 'title' && isImage){
				text += "<tr>";
				text += "<td>"+key+":</td>";
				text += "<td>"+item[key]+"<br><img src='file:///"+item[key]+"'/></td>";
				text += "</tr>";
			}
			else{
				text += "<tr>";
				text += "<td>"+key+":</td>";
				text += "<td>"+item[key]+"</td>";
				text += "</tr>";
			}
		}
	});
	text += "</table></div>";
	return text;
}

function addLeadingZeroes(num){
	if(num<10){
		return "0"+num;
	}
	else{
		return num;
	}
}

/*
function prettyEdit(title, item, callback){
	var dateFormat = "yy-mm-dd";
	var itemDateTime = new Date(item['start'].replace(/-/g, "/").replace(/T/, " "));
	var itemDateString = itemDateTime.getFullYear()+"-"+(itemDateTime.getMonth()+1)+"-"+itemDateTime.getDate();
	var itemDate = new Date(itemDateString);
	var itemTimeHours = itemDateTime.getHours();
	var itemTimeMinutes = itemDateTime.getMinutes();
	var itemTimeSeconds = itemDateTime.getSeconds();
	var form = "<div style='border:none'>";
	form += "<label for='editStartDate'>Edit start date:</label>";
	form += "<input type='text' id='editStartDate' name='editStartDate' value='"+itemDateString+"'/>";
	form += "</div>";
	form += "<div style='border:none'>";
	form += "<label for='editStartHours'>Edit start time:</label>";
	form += "<input type='number' id='editStartHours' name='editStartHours' value='"+itemTimeHours+"' min='0' max='23'/>h ";
	form += "<input type='number' id='editStartMinutes' name='editStartMinutes' value='"+itemTimeMinutes+"' min='0' max='59'/>m ";
	form += "<input type='number' id='editStartSeconds' name='editStartSeconds' value='"+itemTimeSeconds+"' min='0' max='59'/>s";
	form += "</div>";

	Object.keys(item).forEach(function(key){
		if(arrayOfEditIncludedAttr.indexOf(key)>-1){
			form += "<div style='border:none'>";
			form += "<label for='edit"+key+"'>Edit "+key+":</label>";
			form += "<textarea id='edit"+key+"' name='edit"+key+"'>"+item[key]+"</textarea>";
			form += "</div>";
		}
	});
	form += "<div style='border:none'>";
	form += "<label for='editAnnotation'>Edit Annotation:</label>";
	if(item['annotation'] == null){
		form += "<textarea id='editAnnotation' name='editAnnotation'></textarea>";
	}
	else{
		form += "<textarea id='editAnnotation' name='editAnnotation'>"+item['annotation']+"</textarea>";
	}
	form += "</div>";
	swal({
		title: title,
		html: form,
		showCancelButton: true,
		width: '90%',
		preConfirm: function(result) {
			return new Promise(function(resolve) {
				if (result) {
					var jsonResults = {
						"startDate": $('#editStartDate').val(),
						"startHours": $('#editStartHours').val(),
						"startMinutes": $('#editStartMinutes').val(),
						"startSeconds": $('#editStartSeconds').val(),
						"annotation": $('#editAnnotation').val()
					};
					Object.keys(item).forEach(function(key){
						if(key != "classname" && key != "className"){
							// if(item['classname'] != "imgPoint"){
							if(key != 'start' && key != 'annotation' && key != 'group' && key != 'id'){
								jsonResults[key] = $('#edit'+key).val();
							}
						}
					});
					resolve(jsonResults);
				}
			})
		}
	}).then(callback);
	var datePicker = $("#editStartDate").datepicker({
		defaultDate: itemDate,
		changeMonth: true,
		changeYear: true,
		maxDate: 0,
		dateFormat: dateFormat
	});
}
*/
