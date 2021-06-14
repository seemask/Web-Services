$(document).ready(function(e) {
  $('#form').submit(function(e) {
    e.preventDefault();
    var name = $('#name').val();
    var api = $('#api').val();
    if(!name || !api) {
      return;
    }

    // Need to change the url and the query params below, based on need
    $.ajax({
			url: `http://127.0.0.1:5003/service?name=${name}&api=${api}`,
			type: 'GET',
			success: function(response, textStatus, request){
				console.log(response);

                var content_type=request.getResponseHeader('Content-Type')
                if(content_type.includes('json'))
                {
                    $("#time").html(JSON.stringify(response))
                }
                else
                {
                                    $("#time").html(response)
                }

                console.log(request.getResponseHeader('Content-Type'));



			},

			error: function(error){
				console.log(error);
			}
		});
  });
});