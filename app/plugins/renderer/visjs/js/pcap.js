$(document).on("click", "#dateInput", function(){
	$("#loading").removeClass("hidden");
	$("#pcapData").addClass("hidden");
	$("#pcapData").html("");
	var start = $("#datepickerStart").val();
	var end = $("#datepickerEnd").val();
	if(start == ""){
		start = '2000-01-01 00:00:00';
	}
	else{
		start = start + " 00:00:00";
	}
	if(end == ""){
		end = '3000-01-01 23:59:59';
	}
	else{
		end = end + " 23:59:59";
	}
	var pcapDataUrl = "http://localhost?request=pcapData&startDate="+start+"&endDate="+end;
	$.get(pcapDataUrl);
});

function visPCAPData(xyData, allData){
	// alert("PCAP DATA:---------->"+data);
	var container = document.getElementById('pcapData');
	var dataset = new vis.DataSet(xyData);
	var options = {
		style: 'points',
		drawPoints: {
			enabled: true,
			size: 6,
			style: 'circle' // square, circle
		}
	};
	var graph2d = new vis.Graph2d(container, dataset, options);
	$("#loading").addClass("hidden");
	$("#pcapData").removeClass("hidden");
}
