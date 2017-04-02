$("img.circleIconImage").hover(function(){
	$(".circleIconImage").toggleClass("circleIconImageFade");
	$(".icon-contPencil").toggleClass("icon-contPencilVisible");
});

$(".icon-contPencil").hover(function(){
	$(".circleIconImage").toggleClass("circleIconImageFade");
	$(".icon-contPencil").toggleClass("icon-contPencilVisible");
});

$(".userPageGeneralInformationi1").click(function(){
	$(".saveDetails1").css("display","block");
	$(".userPageGeneralInformationi1").css("display","none");
	$(".userPageGeneralInformationContent1 span").attr("contenteditable","true");
});

$(".userPageGeneralInformationi2").click(function(){
	$(".saveDetails2").css("display","block");
	$(".userPageGeneralInformationi2").css("display","none");
	$(".userPageGeneralInformationContent2 span").attr("contenteditable","true");
});

$(".saveDetails1").click(function(){
	$(".saveDetails1").css("display","none");
	$(".userPageGeneralInformationi1").css("display","block");
	$(".userPageGeneralInformationContent1 span").attr("contenteditable","false");
});

$(".saveDetails2").click(function(){
	$(".saveDetails2").css("display","none");
	$(".userPageGeneralInformationi2").css("display","block");
	$(".userPageGeneralInformationContent2 span").attr("contenteditable","false");
});

$(".input-cart-number").keyup(function () {
	if (this.value.length == this.maxLength) {
		var $next = $(this).next('.input-cart-number');
		if ($next.length)
			$(this).next('.input-cart-number').focus();
		else
			$(this).blur();
	}
});

function openUserPageLeftSideTabs(evt, tabName) {
    var i, mainTabContent, mainTabLinks;
    mainTabContent = document.getElementsByClassName("userPageLeftTabsContent");
    for (i = 0; i < mainTabContent.length; i++) {
        mainTabContent[i].style.display = "none";
		mainTabContent[i].style.width = "0";
    }
    mainTabLinks = document.getElementsByClassName("userPageLeftColumnOptionsLinks");
    for (i = 0; i < mainTabLinks.length; i++) {
        mainTabLinks[i].className = mainTabLinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
	document.getElementById(tabName).style.width = "100%";
    evt.currentTarget.className += " active";
}

function openUserPagePaymentOptionsTabs(evt, tabName) {
    var i, mainTabContent, mainTabLinks;
    mainTabContent = document.getElementsByClassName("userPagePaymentOptionsLinksContent");
    for (i = 0; i < mainTabContent.length; i++) {
        mainTabContent[i].style.display = "none";
		mainTabContent[i].style.width = "0";
    }
    mainTabLinks = document.getElementsByClassName("userPagePaymentOptionsLinks");
    for (i = 0; i < mainTabLinks.length; i++) {
        mainTabLinks[i].className = mainTabLinks[i].className.replace(" active1", "");
    }
    document.getElementById(tabName).style.display = "block";
	document.getElementById(tabName).style.width = "75%";
    evt.currentTarget.className += " active1";
}

function toggleChangePasswordForm(){
	document.getElementById('changePasswordForm').classList.toggle('displayChangePasswordForm');
}

var $badges = $('.js-progress-badge')
  , $window = $(window)

  incrementBadge($badges)


function incrementBadge ($progressBadge) {

  var $badge = $progressBadge.find('.badge')
    , fillingFromEmpty = $badge.hasClass('badge--empty')

  $progressBadge.addClass('is-filling')

  if (fillingFromEmpty) {
    $progressBadge.addClass('is-filling-from-empty')
  }
}

function openInNewTab(url) {
  var win = window.open(url, '_blank');
  win.focus();
}

function openCauseAddOverlay() {
    document.getElementById("userPageCauseAdd").style.height = "100%";
	document.getElementsByTagName("body")[0].style.position = "fixed";
}
function openDisplayPictureEditOverlay() {
    document.getElementById("displayPictureEditOverlay").style.height = "100%";
	document.getElementsByTagName("body")[0].style.position = "fixed";
}
