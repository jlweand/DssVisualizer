var PCAPData = function(meXY, meAll, miXY, miAll, tsXY, tsAll){
	var containerME = document.getElementById("multiExcludeData");
	var containerMI = document.getElementById("multiIncludeData");
	var containerTS = document.getElementById("tsharkData");

	var datasetME = new vis.DataSet(meXY);
	var datasetMI = new vis.DataSet(miXY);
	var datasetTS = new vis.DataSet(tsXY);

	var options = {
		drawPoints: true,
		interpolation: false,
		height: "150px"
	};

	var graph2dME = new vis.Graph2d(containerME, datasetME, options);
	var graph2dMI = new vis.Graph2d(containerMI, datasetMI, options);
	var graph2dTS = new vis.Graph2d(containerTS, datasetTS, options);

	$("#loading").addClass("hidden");
	$("#multiExcludeData").removeClass("hidden");
	$("#multiIncludeData").removeClass("hidden");
	$("#tsharkData").removeClass("hidden");

	var xBuffer = 100;
	var yBuffer = 5;

	// alert("before select");
	graph2dME.on('click', function(properties){
		var currTime = new Date(properties.time);
		var currY = properties.value;
		console.log(currY);
		meAll.forEach(function(allObj){
			var allTime = new Date(allObj['start'].replace(/-/g, "/").replace(/T/, " "));
			var allY = allObj[''];
			// var allTime = new Date(allObj['start']);
			var xDiff = Math.abs(currTime - allTime);
			var yDiff = Math.abs(currY - allY);
			// console.log(allObj['start']);
			// console.log(currTime+" - "+allTime+" = "+diff);
			if( xDiff < xBuffer){
				if( yDiff < yBuffer){
					prettyPrompt(allObj['start'], allObj['title']);
				}
			}
		});
	});
	graph2dMI.on('click', function(properties){
		var currTime = new Date(properties.time);
		var currY = properties.value;
		console.log(currY);
		miAll.forEach(function(allObj){
			var allTime = new Date(allObj['start'].replace(/-/g, "/").replace(/T/, " "));
			var allY = allObj[''];
			// var allTime = new Date(allObj['start']);
			var xDiff = Math.abs(currTime - allTime);
			var yDiff = Math.abs(currY - allY);
			// console.log(allObj['start']);
			// console.log(currTime+" - "+allTime+" = "+diff);
			if( xDiff < xBuffer){
				if( yDiff < yBuffer){
					prettyPrompt(allObj['start'], allObj['title']);
				}
			}
		});
	});
	graph2dTS.on('click', function(properties){
		var currTime = new Date(properties.time);
		var currY = properties.value;
		console.log(currY);
		tsAll.forEach(function(allObj){
			var allTime = new Date(allObj['start'].replace(/-/g, "/").replace(/T/, " "));
			var allY = allObj[''];
			// var allTime = new Date(allObj['start']);
			var xDiff = Math.abs(currTime - allTime);
			var yDiff = Math.abs(currY - allY);
			// console.log(allObj['start']);
			// console.log(currTime+" - "+allTime+" = "+diff);
			if( xDiff < xBuffer){
				if( yDiff < yBuffer){
					prettyPrompt(allObj['start'], allObj['title']);
				}
			}
		});
	});
}

function prettyPrompt(title, text) {
	swal({title: title, text: text, html: true, allowOutsideClick: true});
}
