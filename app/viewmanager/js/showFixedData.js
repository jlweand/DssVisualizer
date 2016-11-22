function showFixedData(dataArray, attributeToFilter) {
	JSON.stringify(dataArray);
	var dataArrayFiltered = [];
	var dataArrayKeys = Object.keys(dataArray);

	var filteredIndex = 0;
	dataArrayKeys.forEach(function(index){
        if(dataArray[index]['fixed'] != null && dataArray[index]['fixed']['isDeleted'] != true){
            var fixedKeys = Object.keys(dataArray[index]['fixed']);
            var originalKeys = Object.keys(dataArray[index]);
            dataArrayFiltered[index] = {};
            originalKeys.forEach(function(key){
                if(key != "fixed"){
                    if(fixedKeys.indexOf(key)>-1){
                        dataArrayFiltered[index][key] = dataArray[index]['fixed'][key];
                    }
                    else{
                        dataArrayFiltered[index][key] = dataArray[index][key];
                    }
                }
            });
        }
        else{
            dataArrayFiltered[index] = dataArray[index];
        }
	});
	return dataArrayFiltered;
}
