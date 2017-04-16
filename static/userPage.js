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
	$(".userPageGeneralInformationContent1 input").removeAttr("readonly");
});

$(".userPageGeneralInformationi2").click(function(){
	$(".saveDetails2").css("display","block");
	$(".userPageGeneralInformationi2").css("display","none");
	$(".userPageGeneralInformationContent2 input").removeAttr("readonly");
});

$(".saveDetails1").click(function(){
	$(".saveDetails1").css("display","none");
	$(".userPageGeneralInformationi1").css("display","block");
	$(".userPageGeneralInformationContent1 input").attr("readonly","readonly");
});

$(".saveDetails2").click(function(){
	$(".saveDetails2").css("display","none");
	$(".userPageGeneralInformationi2").css("display","block");
	$(".userPageGeneralInformationContent2 input").attr("readonly","readonly");
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


window.onclick = function(event) {
    if (event.target.matches('.translucentContainer')) {
        document.getElementById("SignUp").style.height = "0%";
		document.getElementById("LogIn").style.height = "0%";
		document.getElementById("myNav").style.width = "0";
		document.getElementsByTagName("body")[0].style.position = "";
		var div = document.getElementById('exploreContent');
		if(div.style.width == "25vw"){
			document.getElementById('ninja-btn').classList.toggle('activated');
			document.getElementById("exploreContent").style.width = "";
			document.getElementById('exploreDiv').classList.toggle('exploreDiv');
			document.getElementById('exploreButton').classList.toggle('exploreButtonActive');

		}
    }
	else if (event.target.matches('.translucentContainer1')) {
		document.getElementById("userPageCauseAdd").style.height = "0%";
		document.getElementsByTagName("body")[0].style.position = "";
	}
	else if (event.target.matches('.translucentContainer5')){
		document.getElementById("userPageCauseDelete").style.height = "0%";
		document.getElementsByTagName("body")[0].style.position = "";
	}
	else if (event.target.matches('.translucentContainer2')){
		document.getElementById("paypalPaymentOverlay").style.height = "0%";
		document.getElementById("paymentBySavedCardsOverlay").style.height = "0%";
		document.getElementsByTagName("body")[0].style.position = "";
	}
	else if (event.target.matches('.translucentContainer3')){
		document.getElementById("projectPageShareBox").style.height = "0%";
		document.getElementsByTagName("body")[0].style.position = "";
	}
	else if (event.target.matches('.translucentContainer4')){
		document.getElementById("myModal").style.display = "none";
		document.getElementsByTagName("body")[0].style.position = "";
	}


}
