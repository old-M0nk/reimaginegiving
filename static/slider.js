$('.slider').each(function() {
  var $this = $(this);
  var $group = $this.find('.slide_group');
  var $slides = $this.find('.slide');
  var bulletArray = [];
  var currentIndex = 0;
  var timeout;
  
  function move(newIndex) {
    var animateLeft, slideLeft;
    
    advance();

    textOverlaySlides();
    
    if ($group.is(':animated') || currentIndex === newIndex) {
      return;
    }
    
    
    if (newIndex > currentIndex) {
      slideLeft = '100%';
      animateLeft = '-100%';
    } else {
      slideLeft = '100%';
      animateLeft = '-100%';
    }
    
    $slides.eq(newIndex).css({
      display: 'block',
      left: slideLeft
    });
    $group.animate({
      left: animateLeft
    }, function() {
      $slides.eq(currentIndex).css({
        display: 'none'
      });
      $slides.eq(newIndex).css({
        left: 0
      });
      $group.css({
        left: 0
      });
      currentIndex = newIndex;
    });
  }
  
  function move2(newIndex) {
    var animateLeft, slideLeft;
    
  textOverlaySlides2();
    advance();
    
    if ($group.is(':animated') || currentIndex === newIndex) {
      return;
    }
    
    
    if (newIndex > currentIndex) {
      slideLeft = '-100%';
      animateLeft = '100%';
    } else {
      slideLeft = '-100%';
      animateLeft = '100%';
    }
    
    $slides.eq(newIndex).css({
      display: 'block',
      left: slideLeft
    });
    $group.animate({
      left: animateLeft
    }, function() {
      $slides.eq(currentIndex).css({
        display: 'none'
      });
      $slides.eq(newIndex).css({
        left: 0
      });
      $group.css({
        left: 0
      });
      currentIndex = newIndex;
    });
  }
  
  function advance() {
    clearTimeout(timeout);
    timeout = setTimeout(function() {
      if (currentIndex < ($slides.length - 1)) {
        move(currentIndex + 1);
      } else {
        move(0);
      }
    }, 4000);
  }
  
  $('.next_btn').on('click', function() {
    if (currentIndex < ($slides.length - 1)) {
      move(currentIndex + 1);
    } else {
      move(0);
    }
  });
  
  $('.previous_btn').on('click', function() {
    if (currentIndex !== 0) {
      move2(currentIndex - 1);
    } else {
      move2(4);
    }
  });
  
  advance();
  textOverlaySlidesStart();
  function textOverlaySlidesStart(){
    $('#textOverlaySlide').html( 'RE<span>!</span>MAGINE ' + '<span class="textOverlaySlideChanging">Development</span>');
  }

  function textOverlaySlides(){
	  if(currentIndex==4)
		$('#textOverlaySlide').html( 'RE<span>!</span>MAGINE ' + '<span class="textOverlaySlideChanging">Development</span>');
	  else if(currentIndex==0)
		$('#textOverlaySlide').html( 'RE<span>!</span>MAGINE ' + '<span class="textOverlaySlideChanging">Growth</span>');
	  else if(currentIndex==1)
		$('#textOverlaySlide').html( 'RE<span>!</span>MAGINE ' + '<span class="textOverlaySlideChanging">Trust</span>');
	  else if(currentIndex==2)
		$('#textOverlaySlide').html( 'RE<span>!</span>MAGINE ' + '<span class="textOverlaySlideChanging">Hope</span>');
	  else 
		$('#textOverlaySlide').html( 'RE<span>!</span>MAGINE ' + '<span class="textOverlaySlideChanging">Giving</span>');
  }
  
  function textOverlaySlides2(){
	  if(currentIndex==1)
		$('#textOverlaySlide').html( 'RE<span>!</span>MAGINE ' + '<span class="textOverlaySlideChanging">Development</span>');
	  else if(currentIndex==2)
		$('#textOverlaySlide').html( 'RE<span>!</span>MAGINE ' + '<span class="textOverlaySlideChanging">Growth</span>');
	  else if(currentIndex==3)
		$('#textOverlaySlide').html( 'RE<span>!</span>MAGINE ' + '<span class="textOverlaySlideChanging">Trust</span>');
	  else if(currentIndex==4)
		$('#textOverlaySlide').html( 'RE<span>!</span>MAGINE ' + '<span class="textOverlaySlideChanging">Hope</span>');
	  else 
		$('#textOverlaySlide').html( 'RE<span>!</span>MAGINE ' + '<span class="textOverlaySlideChanging">Giving</span>');
  }
  
});