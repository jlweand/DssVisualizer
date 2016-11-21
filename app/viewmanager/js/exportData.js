function exportData(){
	techExport = $("#techOptions").val();
	eventExport = $("#eventOptions").val();
	techAndEventExport = $("#techAndEventOptions").val();

    if(windowRangeStart == null || windowRangeEnd == null){
        alert(' time range is undefined');
    }
		else if((techExport == "" || eventExport == "") && (techAndEventExport == "")){
			if(techExport == ""){
					alert('tech name is undefined');
			}
			else if(eventExport == ""){
					alert(' event name is undefined')
			}
		}
    else{
        $(document).ready(function(){
            $.get("http://dssvisualizer.py/exportData",{start:windowRangeStart,end:windowRangeEnd,techName:techExport,eventName:eventExport,techAndEvent:techAndEventExport});
        });
    }
}
