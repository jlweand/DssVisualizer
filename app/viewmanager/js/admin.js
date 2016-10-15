$(document).ready(function(){
	var pluginsUrl = "http://localhost?adminRequest=availablePlugins";
	$.get(pluginsUrl);
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
			var activePcapDataProtocol = activeRend['pcapDataProcol']['plugin'];
			var activePcapThroughput = activeRend['pcapThroughput']['plugin'];
			var activePyKeyLogger = activeRend['pyKeyLogger']['plugin'];
			var activeScreenshots = activeRend['screenshots']['plugin'];

			var datasourcePlugins = parsedJson['datasourcePlugins'];
			var rendererPlugins = parsedJson['rendererPlugins'];
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
					$("#pyKeyLogger").append('<input type="radio" name="pcapThroughput" value="'+pluginName+'">'+pluginName+'</input><br>');
				}
				if(pluginName == activeScreenshots){
					$("#screenshots").append('<input type="radio" name="screenshots" value="'+pluginName+'" checked>'+pluginName+'</input><br>');
				}
				else {
					$("#screenshots").append('<input type="radio" name="pcapThroughput" value="'+pluginName+'">'+pluginName+'</input><br>');
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
