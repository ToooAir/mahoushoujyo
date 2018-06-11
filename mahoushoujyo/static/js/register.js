var openLoginRight = document.querySelector('.h1');
var loginWrapper = document.querySelector('.register-wrapper');

openLoginRight.addEventListener('click', function(){
  loginWrapper.classList.toggle('open'); 
});
$('#submit').click(function(){
			var password = $("#apassword").val();
			var password2 =$("#bpassword").val();
			if(password != password2){
				$("#form").attr('target', 'nm_iframe');
				alert('Password is not correct');
				$("#apassword").val("");
				$("#bpassword").val("");
			}else{
				$("#form").attr('target','');
				$('#form').submit();
			}
		});