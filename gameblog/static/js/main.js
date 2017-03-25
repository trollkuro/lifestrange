$('.blike').on('click', function(event) {
	event.preventDefault();
	var element = $(this);

	$.ajax({
		url:'like_post/',
		type:'GET',
		data: {post_id: element.attr("data-id")},

		success : function(response){
			element.html(' ' + response);
		}
	});

	});
