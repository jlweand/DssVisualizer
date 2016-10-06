$(function(){
	var dateFormat = "yyyy-mm-dd",
	start = $("#datepickerStart")
		.datepicker({
			defaultDate:"+1w",
			changeMonth: true
		})
		.on("change", function(){
			end.datepicker("option", "minDate", getDate(this));
		}),
	end = $("#datepickerEnd")
		.datepicker({
			defaultDate: "+1w",
			changeMonth: true
		})
		.on("change", function(){
			start.datepicker("option", "maxDate", getDate(this));
		});

	function getDate(element){
		var date;
		try{
			date = $.datepicker.parseDate(dateFormat, element.value);
		}catch(error){
			date = null;
		}

		return date;
	} 
});
