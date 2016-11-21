function splitDataForMultipleDataSetManagement(eventTechNames, jsonObjects) {
    var allDataArray = []

    eventTechNames.forEach(function(eventTechName) {
        dataArray = []
        jsonObjects.forEach(function(obj) {
            if(obj["metadata"]["eventName"] + " by " + obj["metadata"]["techName"] == eventTechName) {
                dataArray.push(obj);
            }
        });
        if(dataArray.length > 0) {
            var newJson = {}
            newJson["eventTechName"] = eventTechName;
            newJson["data"] = dataArray;
            allDataArray.push(newJson);
        }
    });

    return allDataArray;
}

function getArrayOfEventTechNames() {
    // we need to get an array of the different possible event/tech combinations that we will use to separate the
    // returned data for multi dataset management.

	var techNames = $("#techOptions").val();
	var eventNames = $("#eventOptions").val();
    var eventTechNames = $("#techAndEventOptions").val();
    var eventTechs = [];

    // #techAndEventOptions already as the unique list, just return it
    if(eventTechNames.length >= 1) {
        return eventTechNames;
    }
	// If either eventNames or techNames is > 1 we have multiple options
	else if (eventNames.length >= 1 || techNames.length >= 1) {
        techNames.forEach(function(tech) {
            eventNames.forEach(function(event){
                eventTechs.push(event + ' by ' + tech);
            });
        });
        return eventTechs;
    }
	// otherwise fill the array with all the options
	else {
		$("#techAndEventOptions option").each(function(){
			eventTechs.push($(this).attr('value'));
		});
        return eventTechs;
    }
}
