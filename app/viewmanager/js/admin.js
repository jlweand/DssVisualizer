$(document).ready(function(){
	var pluginsUrl = "http://localhost?adminRequest=availablePlugins";
	$.get(pluginsUrl);
});

function createRadioButtons(plugins){
    var datasourcePlugins = plugins['datasourcePlugins'];
    var rendererPlugins = plugins['rendererPlugins'];
    var activeDB = plugins['activeDatasourcePlugin'];
    var activeRend = plugins['activeRendererPlugins'];
    var activePcap= activeRend['pcap']['plugin'];
    var activePyKeyLogger = activeRend['pyKeyLogger']['plugin'];
    var activeScreenshots = activeRend['screenshots']['plugin'];

    rendererPlugins.forEach(function(plugin){
        var pluginName = plugin['name'];
        if(pluginName == activePcap){
            $("#pcap").append('<input type="radio" name="pcap" value="'+pluginName+'" checked>'+pluginName+'</input><br>');
        }
        else {
            $("#pcap").append('<input type="radio" name="pcap" value="'+pluginName+'">'+pluginName+'</input><br>');
        }
        if(pluginName == activePyKeyLogger){
            $("#pyKeyLogger").append('<input type="radio" name="pyKeyLogger" value="'+pluginName+'" checked>'+pluginName+'</input><br>');
        }
        else {
            $("#pyKeyLogger").append('<input type="radio" name="pyKeyLogger" value="'+pluginName+'">'+pluginName+'</input><br>');
        }
        if(pluginName == activeScreenshots){
            $("#screenshots").append('<input type="radio" name="screenshots" value="'+pluginName+'" checked>'+pluginName+'</input><br>');
        }
        else {
            $("#screenshots").append('<input type="radio" name="screenshots" value="'+pluginName+'">'+pluginName+'</input><br>');
        }
    });

    datasourcePlugins.forEach(function(plugin){
        var pluginName = plugin['name'];
        if(pluginName == activeDB){
            $("#database").append('<input type="radio" name="database" value="'+pluginName+'" checked>'+pluginName+'</input><br>');
        }
        else{
            $("#database").append('<input type="radio" name="database" value="'+pluginName+'">'+pluginName+'</input><br>');
        }
    });
}

$(document).on("click", "#submit", function(){
	updateJson();
});

function updateJson(){
	var database = $("input[name='database']:checked").val();
	var pcap= $("input[name='pcap']:checked").val();
	var pyKeyLogger= $("input[name='pyKeyLogger']:checked").val();
	var screenshots= $("input[name='screenshots']:checked").val();
	var scriptFile= "";
	var newActive = "";

	var updateRendJson = "http://localhost?adminSubmission=pluginChanges&database="+database+"&pcap="+pcap+"&pyKeyLogger="+pyKeyLogger+"&screenshots="+screenshots;
	$.get(updateRendJson);
}

$(document).ready(function(){
    $('#import').submit(function(){
        $.get("http://dssvisualizer.py/importData", $( '#import' ).serialize());
    });
    $('#export').submit(function(){
        $.get("http://dssvisualizer.py/exportData", $( '#export' ).serialize());
    });

    //$('#date').val(getCurrentDate());
});

function getCurrentDate() {
    var rightNow = new Date();
    var curr_date = zeroPadNumber(rightNow.getDate());
    var curr_month = zeroPadNumber(rightNow.getMonth() + 1);
    var curr_year = rightNow.getFullYear();
    var curr_hour = zeroPadNumber(rightNow.getHours());
    var curr_min = zeroPadNumber(rightNow.getMinutes());
    var curr_sec = zeroPadNumber(rightNow.getSeconds());
    return curr_year + "-" + curr_month + "-" + curr_date + " " + curr_hour + ":" + curr_min + ":" + curr_sec
}
function zeroPadNumber (number) {
    if (number == 1) {
        number = "0" + number;
    }
    return number;
}

function explore(){
	$.get("http://dssvisualizer.py/explore");
}

