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

	$.widget( "ui.timespinner", $.ui.spinner, {
      options: {
        // seconds
        step: 60 * 1000,
        // hours
        page: 60
      },

      _parse: function( value ) {
        if ( typeof value === "string" ) {
          // already a timestamp
          if ( Number( value ) == value ) {
            return Number( value );
          }
          return +Globalize.parseDate( value );
        }
        return value;
      },

      _format: function( value ) {
        return Globalize.format( new Date(value), "t" );
      }
    });

    $( "#spinner" ).timespinner();
});
