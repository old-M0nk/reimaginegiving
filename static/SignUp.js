
let currentlyVisible = ".form-sign-up";
let currentlyHidden = ".form-log-in";
$(".info-item .btn1").click(function(){
  $(".form-container").toggleClass("actived");
  $(currentlyVisible).fadeToggle('750', function() {
    $(currentlyHidden).fadeToggle();
    s = currentlyVisible;
    currentlyVisible = currentlyHidden;
    currentlyHidden = s;
  });
});

let currentlyVisible1 = ".form-log-in1";
let currentlyHidden1 = ".form-sign-up1";
$(".info-item1 .btn2").click(function(){
  $(".form-container1").toggleClass("actived1");
  $(currentlyVisible1).fadeToggle('750', function() {
    $(currentlyHidden1).fadeToggle();
    s = currentlyVisible1;
    currentlyVisible1 = currentlyHidden1;
    currentlyHidden1 = s;
  });
});


function openSignUpOverlay() {
    document.getElementById("SignUp").style.height = "100%";
	document.getElementsByTagName("body")[0].style.position = "fixed";
}

/* Close when someone clicks on the "x" symbol inside the explore */
function closeSignUpOverlay() {
	document.getElementById("SignUp").style.height = "0%";
	document.getElementsByTagName("body")[0].style.position = "";
}

function openLogInOverlay() {
	document.getElementById("LogIn").style.height = "100%";
	document.getElementsByTagName("body")[0].style.position = "fixed";
}

/* Close when someone clicks on the "x" symbol inside the explore */
function closeLogInOverlay() {
	document.getElementById("LogIn").style.height = "0%";
	document.getElementsByTagName("body")[0].style.position = "";
}

window.onclick = function(event) {
    if (event.target.matches('.translucentContainer')) {
        document.getElementById("SignUp").style.height = "0%";
		document.getElementById("LogIn").style.height = "0%";
		document.getElementById("myNav").style.width = "0";
		document.getElementsByTagName("body")[0].style.position = "";
		var div = document.getElementById('exploreContent');
		if(div.style.width == "25%"){
			document.getElementById('ninja-btn').classList.toggle('activated');
			document.getElementById("exploreContent").style.width = "";
			document.getElementById('exploreDiv').classList.toggle('exploreDiv');
			document.getElementById('exploreButton').classList.toggle('exploreButtonActive');
		}
    }
	else if (event.target.matches('.translucentContainer1')) {
		document.getElementById("displayPictureEditOverlay").style.height = "0%";
		document.getElementById("userPageShareBox").style.height = "0%";
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

}
//
// function SignMeUp() {
//     document.getElementById("SignUp").style.height = "0%";
// 	document.getElementById("LogIn").style.height = "0%";
// 	document.getElementsByTagName("body")[0].style.position = "";
// 	document.getElementById("navBarProfileButton").style.display = "inline-block";
// 	document.getElementById("navBarLogInButton").style.display = "none";
// 	document.getElementById("navBarSignUpButton").style.display = "none";
// }
//
// function logout() {
// 	document.getElementById("navBarProfileButton").style.display = "none";
// 	document.getElementById("navBarLogInButton").style.display = "inline-block";
// 	document.getElementById("navBarSignUpButton").style.display = "inline-block";
// }
//

