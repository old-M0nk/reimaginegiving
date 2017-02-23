
function openNav() {
	var div = document.getElementById('exploreContent');
	if(div.style.width == ""){
    document.getElementById("myNav").style.width = "100%";
	document.getElementById("exploreContent").style.width = "25%";
	document.getElementById('exploreDiv').classList.toggle('exploreDiv');
	document.getElementById('ninja-btn').classList.toggle('activated');
	document.getElementById('exploreButton').classList.toggle('exploreButtonActive');
	document.getElementsByTagName("body")[0].style.overflowY = "hidden";
	}
	else
	{
		closeNav();
	}
}

function closeNav() {
    document.getElementById("myNav").style.width = "0";
	document.getElementById("exploreContent").style.width = "";
	document.getElementById('exploreDiv').classList.toggle('exploreDiv');
	document.getElementById('ninja-btn').classList.toggle('activated');
	document.getElementById('exploreButton').classList.toggle('exploreButtonActive');
	document.getElementsByTagName("body")[0].style.overflowY = "scroll";
}

function myfunction1(){

	document.getElementById('downArrow1').classList.toggle('topArrow');
	var div = document.getElementById('locationInput');
    if (div.style.display !== 'none') {
        div.style.display = 'none';
    }
    else {
        div.style.display = 'block';
    }
}

function myfunction2() {

	document.getElementById('downArrow2').classList.toggle('topArrow');
	var div = document.getElementById('fundingInput');
    if (div.style.display !== 'none') {
        div.style.display = 'none';
    }
    else {
        div.style.display = 'block';
    }
}

function myfunction3(){
	document.getElementById('downArrow3').classList.toggle('topArrow');
	var div = document.getElementById('causeInput');
    if (div.style.display !== 'none') {
        div.style.display = 'none';
    }
    else {
        div.style.display = 'block';
	}
}