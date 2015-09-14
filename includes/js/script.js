$(function() {
	$('#alertMe').click(function(e) {
		e.preventDefault();

		$('#successAlert').slideDown();
	});

	$('a.pop').click(function(e) {
		e.preventDefault();
	});

	$('a.pop').popover();

	$('[rel="tooltip"]').tooltip();

	/* Custom stuff */
	$('.btn:not(.btn-link)').hover(function() {
		var bg_color = $(this).css("background-color");
		var font_color = $(this).css("color");
		$(this).css('color', bg_color);
		$(this).css('background-color', font_color);
	});

	$(window).resize(function() {
		console.log('resize called');
		var width=$(window).width();
		if(width <= 480) {
			$('#blognail1').removeClass('col-6').addClass('col-12');
			$('#blognail2').removeClass('col-6').addClass('col-12');
		}
		else{
			$('#blognail1').removeClass('col-12').addClass('col-6');
			$('#blognail2').removeClass('col-12').addClass('col-6');
		}
	}).resize();

});
