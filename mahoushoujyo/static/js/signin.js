 $("#login-button").click(function(event){
		 event.preventDefault();
	 $('form').fadeOut();
	 $('.wrapper').addClass('form-success');
	 $('#text').fadeOut(1000,function(){$('#text').text('Change the world or not?')});
	 setTimeout("$('#text').fadeIn(1000)",3000);
	 var account = $("#account").val();
	 var password =$("#password").val();
	 setTimeout("$('#form').submit()",5000);
});