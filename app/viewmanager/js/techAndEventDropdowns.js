function populateTechDropdown(techList) {
    for(var i=0; i<techList.length; i++) {
        $("#techOptions").append('<option value="'+techList[i]+'">'+techList[i]+'</option>')
    }
    $("#techOptions").trigger("chosen:updated");
}

function populateEventDropdown(eventList) {
    for(var i=0; i<eventList.length; i++) {
        $("#eventOptions").append('<option value="'+eventList[i]+'">'+eventList[i]+'</option>')
    }
    $("#eventOptions").trigger("chosen:updated");
}

function populateTechAndEventDropdown(techEventList) {
    for(var i=0; i<techEventList.length; i++) {
        $("#techAndEventOptions").append('<option value="'+techEventList[i]+'">'+techEventList[i]+'</option>')
    }
    $("#techAndEventOptions").trigger("chosen:updated");
}

// also need to enable/disable tech dropdown in this method
// enable when eventNames > 0, otherwise disable.
$(document).on("change", "#eventOptions", function(evt, params){
    $('#techOptions').empty()
    var eventNames = $("#eventOptions").val();
    if(eventNames.length > 0) {
        var getTechNames = "http://localhost?populateDropdown=availableTechNames&eventNames="+eventNames;
        $.get(getTechNames);
    } else {
        $("#techOptions").trigger("chosen:updated");
    }
});


$(document).ready(function() {
    var getEventNames = "http://localhost?populateDropdown=availableEventNames";
    $.get(getEventNames)
    var getEventTechNames = "http://localhost?populateDropdown=availableTechAndEventNames";
    $.get(getEventTechNames)
});

//Disables dropdown menu for events. Kept the plugin id updates ($("#techAndEventOptions").prop("disabled", false);)
//seperate from the on.change (for #eventOptions) function above and the #techAndEventOptions on.change below
//to prevent overwriting each other
$(document).on("change", "#eventOptions", function(evt, params){
	var eventNames = $("#eventOptions").val();
	if(eventNames.length>0){
		$("#techAndEventOptions").prop("disabled", true);
	}
	else{
		$("#techAndEventOptions").prop("disabled", false);
	}
	$("#techAndEventOptions").trigger("chosen:updated");
});


$(document).on("change", "#techAndEventOptions", function(evt, params){
	var techAndEventNames = $("#techAndEventOptions").val();
	if(techAndEventNames.length>0){
		$("#eventOptions").prop("disabled", true);
		$("#techOptions").prop("disabled", true);
	}
	else{
		$("#eventOptions").prop("disabled", false);
		$("#techOptions").prop("disabled", false);
	}
	$("#eventOptions").trigger("chosen:updated");
	$("#techOptions").trigger("chosen:updated");

});
