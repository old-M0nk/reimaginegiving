function openProjectMainTabs(evt, tabName) {
    var i, mainTabContent, mainTabLinks;
    mainTabContent = document.getElementsByClassName("mainTabContent");
    for (i = 0; i < mainTabContent.length; i++) {
        mainTabContent[i].style.display = "none";
		mainTabContent[i].style.width = "0";
    }
    mainTabLinks = document.getElementsByClassName("mainTabLinks");
    for (i = 0; i < mainTabLinks.length; i++) {
        mainTabLinks[i].className = mainTabLinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
	document.getElementById(tabName).style.width = "100%";
    evt.currentTarget.className += " active";
}

function openProjectDonationOptionsTabs(evt, tabName) {
    var i, donationOptionsTabContent, donationOptionsTabLinks;
    donationOptionsTabContent = document.getElementsByClassName("donationOptionsTabContent");
    for (i = 0; i < donationOptionsTabContent.length; i++) {
        donationOptionsTabContent[i].style.display = "none";
    }
    var activeTab = document.getElementById('donationOptionActive');
    if(evt == 'projectPageDonationOptionsMonthly')
    {
        if(activeTab.className == "slideLeft"){
            document.getElementById('donationOptionActive').classList.toggle('slideLeft');
            document.getElementById('donationOptionActive').classList.toggle('slideRight');
        }
    }
    else
    {
        if(activeTab.className == "slideRight"){
            document.getElementById('donationOptionActive').classList.toggle('slideLeft');
            document.getElementById('donationOptionActive').classList.toggle('slideRight');
        }
    }
    document.getElementById(tabName).style.display = "block";
}
