$(document).ready(function(){
		$('.ahlist li, .bslist li, .sslist li, .pslist li, .islist li').hide('slow');
		$('h3.ahlist, h3.bslist, h3.sslist, h3.pslist, h3.islist').addClass('clickable');
		$("h3.ahlist").click( function() { $('.ahlist li').toggle('slow'); $('h3.ahlist').toggleClass("selected"); return false; } );
		$("h3.bslist").click( function() { $('.bslist li').toggle('slow'); $('h3.bslist').toggleClass("selected"); return false; } );
		$("h3.pslist").click( function() { $('.pslist li').toggle('slow'); $('h3.pslist').toggleClass("selected"); return false; } );
		$("h3.islist").click( function() { $('.islist li').toggle('slow'); $('h3.islist').toggleClass("selected"); return false; } );
		$("h3.sslist").click( function() { $('.sslist li').toggle('slow'); $('h3.sslist').toggleClass("selected"); return false; } );
});