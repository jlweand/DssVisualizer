var attributesToBeSearchedAndFiltered = ['title', 'content', 'annotation', 'comment'];

function filterTheTimeline(){
	unFilterTheTimeline();
	var filter = $('#filter').val().trim().toLowerCase();
	if(filter != ''){
		if(keylogger != null){
			if(keylogger.length > 0){
				keylogger.forEach(function(timeline){
					var data = timeline.getDataset();
					filterTheData(data, filter);
				});
			}
		}
        if(snoopy != null){
			if(snoopy.length > 0){
				snoopy.forEach(function(timeline){
					var data = timeline.getDataset();
					filterTheData(data, filter);
				});
			}
		}
		if(pcapData != null){
			if(pcapData.length > 0){
				pcapData.forEach(function(timeline){
					var meData = timeline.getMEDataset();
					filterTheData(meData, filter);
					var miData = timeline.getMIDataset();
					filterTheData(miData, filter);
					var tsData = timeline.getTSDataset();
					filterTheData(tsData, filter);
				});
			}
		}
		if(snap != null){
			if(snap.length > 0){
				snap.forEach(function(timeline){
					var data = timeline.getDataset();
					filterTheData(data, filter);
				});
			}
		}
	}
}
function unFilterTheTimeline(){
	$(".filterHide").removeClass("filterHide");
}
function filterTheData(data, filter){
	data.forEach(function(dataObj){
		var objectShouldBeHidden = true;
		var itemID = dataObj['id'];
		attributesToBeSearchedAndFiltered.forEach(function(attr){
			if(dataObj[attr] != null){
				var stringToLookIn = dataObj[attr].trim().toLowerCase();
				if(stringToLookIn != '' && stringToLookIn.indexOf(filter) > -1){
					objectShouldBeHidden = false;
				}
			}
		});
		if(objectShouldBeHidden){
			$("[data-id='"+itemID+"']").addClass("filterHide");
		}
	});
}

function searchTheTimeline(){
	unSearchTheTimeline();
	var search = $('#search').val().trim().toLowerCase();
	if(search != ''){
		if(keylogger != null){
			if(keylogger.length > 0){
				keylogger.forEach(function(timeline){
					var data = timeline.getDataset();
					searchTheData(data, search);
				});
			}
		}
        if(snoopy != null){
			if(snoopy.length > 0){
				snoopy.forEach(function(timeline){
					var data = timeline.getDataset();
					searchTheData(data, search);
				});
			}
		}
		if(pcapData != null){
			if(pcapData.length > 0){
				pcapData.forEach(function(timeline){
					var meData = timeline.getMEDataset();
					searchTheData(meData, search);
					var miData = timeline.getMIDataset();
					searchTheData(miData, search);
					var tsData = timeline.getTSDataset();
					searchTheData(tsData, search);
				});
			}
		}
		if(snap != null){
			if(snap.length > 0){
				snap.forEach(function(timeline){
					var data = timeline.getDataset();
					searchTheData(data, search);
				});
			}
		}
	}
}
function unSearchTheTimeline(){
	$(".search").removeClass("search");
}
function searchTheData(data, search){
	data.forEach(function(dataObj){
		var objectShouldBeHighlighted = false;
		var itemID = dataObj['id'];
		attributesToBeSearchedAndFiltered.forEach(function(attr){
			if(dataObj[attr] != null){
				var stringToLookIn = dataObj[attr].trim().toLowerCase();
				if(stringToLookIn != '' && stringToLookIn.indexOf(search) > -1){
					objectShouldBeHighlighted = true;
				}
			}
		});
		if(objectShouldBeHighlighted){
			$("[data-id='"+itemID+"']").addClass("search");
		}
	});
}
