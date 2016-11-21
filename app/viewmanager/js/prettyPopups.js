function prettyAdd(title, callback){
	swal({
		title: title,
		input: 'textarea',
		showCancelButton: true
	}).then(callback);
}

function prettyPrompt(title, text){

}

function prettyEdit(){

}

function formatObjectForDisplay(item){
	var text = "<div><table>";
	Object.keys(item).forEach(function(key){
		var isImage = item['classname'] != null && item['classname'] == 'imgPoint';
		if(key != 'classname'){
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
