function getFixedDataPoint(dataPoint) {
    var filteredData = dataPoint;
    if(dataPoint['fixedData'] != null){
        var fixedKeys = Object.keys(dataPoint['fixedData']);
        var originalKeys = Object.keys(dataPoint);

        originalKeys.forEach(function(key){
            if(key != "fixedData") {
                if(fixedKeys.indexOf(key)>-1){
                    filteredData[key] = filteredData['fixedData'][key];
                }
            }
        });
    }
    return filteredData;
}

function getFixedDataArray(dataArray) {
	var dataArrayFiltered = [];
	dataArray.forEach(function(dataPoint, index){
        dataArrayFiltered[index] = getFixedDataPoint(dataPoint);
    });
    return dataArrayFiltered;
}