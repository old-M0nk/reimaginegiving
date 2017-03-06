$('.checkOutPageDonationAmount').on('keydown', function(event) {
  if($(this).text().length === 8 && event.keyCode != 8) {
  	event.preventDefault();
  }
});

function openPaymentOptionTabs(evt, tabName) {
    var i, mainTabContent, mainTabLinks;
    mainTabContent = document.getElementsByClassName("paymentOptionTabsContent");
    for (i = 0; i < mainTabContent.length; i++) {
        mainTabContent[i].style.display = "none";
		mainTabContent[i].style.width = "0";
    }
    mainTabLinks = document.getElementsByClassName("paymentOptionsLinks");
    for (i = 0; i < mainTabLinks.length; i++) {
        mainTabLinks[i].className = mainTabLinks[i].className.replace(" activePaymentOption", "");
    }
    document.getElementById(tabName).style.display = "block";
	document.getElementById(tabName).style.width = "100%";
    evt.currentTarget.className += " activePaymentOption";
}

function openPaypalPaymentOvelay() {
    document.getElementById("paypalPaymentOverlay").style.height = "100%";
	document.getElementsByTagName("body")[0].style.position = "fixed";
}


function showCVV(listId) {
	var i, mainTabContent;
    mainTabContent = document.getElementById("paymentBySavedCards").childNodes[1].children;
    for (i = 0; i < mainTabContent.length; i++) {
        document.getElementById("paymentBySavedCards").childNodes[1].children[i].children[2].style.display = "none";
    }
    document.getElementById("paymentBySavedCards").childNodes[1].children[listId].children[2].style.display = "block";
}
