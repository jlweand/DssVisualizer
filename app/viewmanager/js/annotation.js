// $(document).ready(function(){
//
// });

// function addAnnotation(currItem){
// 	var group = $('[data-id="'+currItem+'"]').attr("data-group");
// 	var dataNames = ['keypress', 'click ', 'timed'];
// 	var groupName = dataNames[group];
// 	prettyPrompt('Add annotation', 'Enter annotation for '+currItem+':', currItem.annotation, function (value) {
//         if (value) {
//           $("#oldAnnotations").html(value);
// 		  $.ajax({
// 			  url: "http://localhost?submission=annotation&itemID="+currItem+"&type="+groupName+"&annotation="+value,
// 			//   method: "GET",
// 			//   data: {submission: "annotation", itemID: currItem, type: groupName, annotation: value},
// 			  success: function(data){
// 				  alert("http://localhost?submission=annotation&itemID="+currItem+"&type="+groupName+"&annotation="+value);
// 			  }
// 		  })
//         //   callback(currItem); // send back adjusted new item
//         }
//         // else {
//         //   callback(null); // cancel item creation
//         // }
//       });
// }


// function prettyPrompt(title, text, inputValue, callback) {
//     swal({
//       title: title,
//       text: text,
//       type: 'input',
//       showCancelButton: true,
//       inputValue: inputValue
//     }, callback);
//   }
