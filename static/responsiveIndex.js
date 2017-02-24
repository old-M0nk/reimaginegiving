window.onresize = function() {
	var txt;
	txt = $(window).width();
	$('.projectContent').width(txt);
}