$(document).ready(function(){
	$("#annotationsForm").submit(function(event){
		event.preventDefault();
		var annotation = $("#annotation").val();
		var dataID = $("#objID").val();
		if(annotation==""){
			prettyConfirm("Invalid Input", "Please provide an input", function (ok) {});
		}
		else{
			$.get("", {annotation: annotation, dataID: dataID});
		}
	});

	function prettyConfirm(title, text, callback) {
		swal({
			title: title,
			text: text,
			type: 'warning',
			showCancelButton: false,
			confirmButtonColor: "#DD6B55"
		}, callback);
	}
});
