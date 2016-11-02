$(function(){
	var dateFormat = "yy-mm-dd";
	var start = $("#datepickerStart")
		.datepicker({
			defaultDate:"+1w",
			changeMonth: true,
			changeYear: true,
			maxDate: 0
		})
		.on("change", function(){
			start.datepicker("option", {"dateFormat": dateFormat});
			end.datepicker("option", {"minDate": getDate(this)});
		}),
	end = $("#datepickerEnd")
		.datepicker({
			defaultDate: "+1w",
			changeMonth: true,
			changeYear: true,
			maxDate: 0
		})
		.on("change", function(){
			end.datepicker("option", {"dateFormat": dateFormat});
			start.datepicker("option", {"maxDate": getDate(this)});
		});
	function getDate(element){
		var date;
		try{
			date = $.datepicker.parseDate(dateFormat, element.value);
		}catch(error){
			alert(error);
			date = null;
		}
		return date;
	}
});
