  var delay = function(s){
  return new Promise(function(resolve,reject){
   setTimeout(resolve,s); 
    });
  };

  function enterAnim() {
    $('#leftw').removeClass().addClass('pulse' + ' animated').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
      $(this).removeClass();
    });
    $('#rightw').removeClass().addClass('pulse' + ' animated').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
      $(this).removeClass();
    });
    var r = document.getElementById("rblack");
    var l = document.getElementById("lblack");
    delay(1000).then(function(){
    $('#leftw,#rightw').fadeOut(1500);
    return delay(2000);
    }).then(function(){
    l.style = "width:35%";
    l.style.top = 8+'%';
    l.style.left = 5+'%';
    return delay(150);
    }).then(function(){
    r.style = "width:35%";
    r.style.top = 30+'%';
    r.style.left = 70+'%';
    return delay(150);
    }).then(function(){
    l.style = "width:50%";
    l.style.top = 25+'%';
    l.style.left = 45+'%';
    return delay(150);
    }).then(function(){
    r.style = "width:50%";
    r.style.top = 7+'%';
    r.style.left = 6+'%';
    return delay(150);
    }).then(function(){
    l.style = "width:70%";
    l.style.top = 3+'%';
    l.style.left = '-'+30+'%';
    return delay(150); 
    }).then(function(){
    r.style = "width:70%";
    r.style.top = 7+'%';
    r.style.left = 50+'%';
    return delay(150)
    }).then(function(){
    document.getElementById("wrapper").style.display="none";
    document.body.style.backgroundColor = "black";
    return delay(1000)
    }).then(function(){
    window.location="signin";
    })
    
  };

  $('#enter').click(function(e){
      e.preventDefault();
      enterAnim();
  });

  $('#regi').click(function(e){
      e.preventDefault();
      $('#wrapper').fadeOut(1500);
      delay(1500).then(function(){
        window.location="register";
      })
  });