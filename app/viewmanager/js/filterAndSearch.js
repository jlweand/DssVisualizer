function filterTheData(dataArray, attributeToFilter){
	JSON.stringify(dataArray);
	var dataArrayFiltered = [];
	var dataArrayKeys = Object.keys(dataArray);

	var filteredIndex = 0;
	dataArrayKeys.forEach(function(index){
		if(filter == ''){
			if(dataArray[index]['fixed'] != null){
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
		}
		else{
			var attributeExists = dataArray[index][attributeToFilter] != null;
			var filterInAttribute = attributeExists && dataArray[index][attributeToFilter].indexOf(filter) > -1;
			var fixedExists = dataArray[index]['fixed'] != null;
			var fixedAttributeExists = fixedExists && dataArray[index]['fixed'][attributeToFilter] != null;
			var filterInFixedAttribute = fixedAttributeExists && dataArray[index]['fixed'][attributeToFilter].indexOf(filter) > -1;
			if(filterInAttribute && !fixedExists){
				dataArrayFiltered[filteredIndex] = dataArray[index];
				filteredIndex++;
			}
			else if(filterInFixedAttribute){
				var fixedKeys = Object.keys(dataArray[index]['fixed']);
				var originalKeys = Object.keys(dataArray[index]);
				dataArrayFiltered[filteredIndex] = {};
				originalKeys.forEach(function(key){
					if(key != "fixed"){
						if(fixedKeys.indexOf(key)>-1){
							dataArrayFiltered[filteredIndex][key] = dataArray[index]['fixed'][key];
						}
						else{
							dataArrayFiltered[filteredIndex][key] = dataArray[index][key];
						}
					}
				});
				filteredIndex++;
			}
		}
	});
	return dataArrayFiltered;
}
