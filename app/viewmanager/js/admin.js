$(document).ready(function(){
	var pluginsUrl = "http://localhost?adminRequest=availablePlugins";
	$.get(pluginsUrl);
	// alert(pluginsUrl);
	// createRadioButtons("hello");
});

function createRadioButtons(plugins){
	// $.ajax({
	// 	url: '../core/config/config.json',
	// 	success: function(data){
	// 		var parsedJson = data;
	// 		if(typeof data == 'string'){
	// 			parsedJson = JSON.parse(data);
	// 		}
			// alert(parsedJson);
			var activeDB = plugins['activeDatasourcePlugin'];
			var activeRend = plugins['activeRendererPlugins'];
			var activePcapDataProtocol = activeRend['pcapDataProtocol']['plugin'];
			var activePcapThroughput = activeRend['pcapThroughput']['plugin'];
			var activePyKeyLogger = activeRend['pyKeyLogger']['plugin'];
			var activeScreenshots = activeRend['screenshots']['plugin'];

			var datasourcePlugins = plugins['datasourcePlugins'];
			var rendererPlugins = plugins['rendererPlugins'];
			// alert(rendererPlugins);

			rendererPlugins.forEach(function(plugin){
				var pluginName = plugin['name'];
				if(pluginName == activePcapDataProtocol){
					$("#pcapDataProtocol").append('<input type="radio" name="pcapDataProtocol" value="'+pluginName+'" checked>'+pluginName+'</input><br>');
				}
				else{
					$("#pcapDataProtocol").append('<input type="radio" name="pcapDataProtocol" value="'+pluginName+'">'+pluginName+'</input><br>');
				}
				if(pluginName == activePcapThroughput){
					$("#pcapThroughput").append('<input type="radio" name="pcapThroughput" value="'+pluginName+'" checked>'+pluginName+'</input><br>');
				}
				else {
					$("#pcapThroughput").append('<input type="radio" name="pcapThroughput" value="'+pluginName+'">'+pluginName+'</input><br>');
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
	// 	}
	// });
}

$(document).on("click", "#submit", function(){
	updateJson();
});

function updateJson(){
	var database = $("input[name='database']:checked").val();
	var pcapDataProtocol= $("input[name='pcapDataProtocol']:checked").val();
	var pcapThroughput= $("input[name='pcapThroughput']:checked").val();
	var pyKeyLogger= $("input[name='pyKeyLogger']:checked").val();
	var screenshots= $("input[name='screenshots']:checked").val();
	var scriptFile= "";
	var newActive = "";

	var updateRendJson = "http://localhost?adminSubmission=pluginChanges&database="+database+"&pcapDataProtocol="+pcapDataProtocol+"&pcapThroughput="+pcapThroughput+"&pyKeyLogger="+pyKeyLogger+"&screenshots="+screenshots;
	$.get(updateRendJson);
}
$(document).ready(function(){
	$("#importSlide").click(function(){
			$("#importPanel").slideToggle("slow");
	});
 $("#exportSlide").click(function(){
			$("#exportPanel").slideToggle("slow");
	});
 $('#import').submit(function(){

		$.get("http://dssvisualizer.py/importData", $( '#import' ).serialize());
 });
 $('#export').submit(function(){

		$.get("http://dssvisualizer.py/exportData", $( '#export' ).serialize());
 });
});

function explore(){
	$.get("http://dssvisualizer.py/explore");
}
