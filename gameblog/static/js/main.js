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

/* MODAL */
var modal = $('#reply-form');

$('#comments').on('click', 'a', function () {
	var element = $(this);
	
	var commentId = element.attr("comment-id");
	modal.attr('comment-id', commentId);
});

$('.reply-form__button').on('click', function () {
	var author = modal[0].author.value;
	var text = modal[0].text.value;
	var commentId = modal.attr('comment-id');
	var postId = modal.attr('post-id');
	console.log(postId);
		
	// $.ajax({
	// 	url: 'comment/',
	// 	type: 'POST',
	// 	data: { parent_id: commentId,  }
	// })
})
