$(".NGOFormOptionIndividual a").click(function(){
	$(".IndividualForm").toggleClass("IndividualFormOpen");
});

$(".NGOFormOptionOrganization a").click(function(){
	$(".OrganizationForm").toggleClass("OrganizationFormOpen");
});

function openNGOOrganizationTabs(evt, tabName) {
    var i, mainTabContent, mainTabLinks;
    mainTabContent = document.getElementsByClassName("NGOOrganizationFormTabContent");
    for (i = 0; i < mainTabContent.length; i++) {
		if(mainTabContent[i].classList.contains("slideRight") )
		{
			mainTabContent[i].classList.toggle("slideLeft");
			mainTabContent[i].classList.toggle("slideRight");
		}
    }
    mainTabLinks = document.getElementsByClassName("NGOOrganizationFormTab");
    for (i = 0; i < mainTabLinks.length; i++) {
        mainTabLinks[i].className = mainTabLinks[i].className.replace(" activeTab", "");
    }
    document.getElementById(tabName).classList.toggle("slideRight");
	document.getElementById(tabName).classList.toggle("slideLeft");
    evt.currentTarget.className += " activeTab";
}

function openNGOIndividualTabs(evt, tabName) {
    var i, mainTabContent, mainTabLinks;
    mainTabContent = document.getElementsByClassName("NGOIndividualFormTabContent");
    for (i = 0; i < mainTabContent.length; i++) {
		if(mainTabContent[i].classList.contains("slideRight") )
		{
			mainTabContent[i].classList.toggle("slideLeft");
			mainTabContent[i].classList.toggle("slideRight");
		}
    }
    mainTabLinks = document.getElementsByClassName("NGOIndividualFormTab");
    for (i = 0; i < mainTabLinks.length; i++) {
        mainTabLinks[i].className = mainTabLinks[i].className.replace(" activeTab", "");
    }
    document.getElementById(tabName).classList.toggle("slideRight");
	document.getElementById(tabName).classList.toggle("slideLeft");
    evt.currentTarget.className += " activeTab";
}

function openNGOSocialLinksInput(evt, tabName) {
    var i, mainTabContent, mainTabLinks;
    mainTabContent = document.getElementsByClassName("NGOSocialLinksInput");
    for (i = 0; i < mainTabContent.length; i++) {
		mainTabContent[i].style.display="none";
		mainTabContent[i].style.opacity="0";
    }
    mainTabLinks = document.getElementsByClassName("NGOSocialMediaInputIcon");
    for (i = 0; i < mainTabLinks.length; i++) {
        mainTabLinks[i].className = mainTabLinks[i].className.replace(" activeIcon", "");
    }
    document.getElementById(tabName).style.display="block";
	document.getElementById(tabName).style.opacity="1";
	evt.currentTarget.className += " activeIcon";
}

/*Basicform*/
$(".NGOOrganizationBasicFormSection1 .nextBtn").click(function(){
	$(".NGOOrganizationBasicFormSection1").css("top","-100%");
	$(".NGOOrganizationBasicFormSection1").css("animation","slideTop 0.5s");
	$(".NGOOrganizationBasicFormSection2").css("top","-100%");
	$(".NGOOrganizationBasicFormSection2").css("animation","slideTop 0.5s");
});

$(".NGOOrganizationBasicFormSection2 .backBtn").click(function(){
	$(".NGOOrganizationBasicFormSection1").css("top","0%");
	$(".NGOOrganizationBasicFormSection1").css("animation","slideBottom 0.5s");
	$(".NGOOrganizationBasicFormSection2").css("top","0%");
	$(".NGOOrganizationBasicFormSection2").css("animation","slideBottom 0.5s");
});

$(".NGOOrganizationBasicFormSection2 .nextBtn").click(function(){
	$(".NGOOrganizationBasicFormSection3").css("top","-200%");
	$(".NGOOrganizationBasicFormSection3").css("animation","slideTop1 0.5s");
	$(".NGOOrganizationBasicFormSection2").css("top","-200%");
	$(".NGOOrganizationBasicFormSection2").css("animation","slideTop1 0.5s");
});

$(".NGOOrganizationBasicFormSection3 .backBtn").click(function(){
	$(".NGOOrganizationBasicFormSection3").css("top","-100%");
	$(".NGOOrganizationBasicFormSection3").css("animation","slideBottom1 0.5s");
	$(".NGOOrganizationBasicFormSection2").css("top","-100%");
	$(".NGOOrganizationBasicFormSection2").css("animation","slideBottom1 0.5s");
});

$(".NGOOrganizationBasicFormSection3 .nextBtn").click(function(){
	var i, mainTabContent, mainTabLinks;
    mainTabContent = document.getElementsByClassName("NGOOrganizationFormTabContent");
    for (i = 0; i < mainTabContent.length; i++) {
		if(mainTabContent[i].classList.contains("slideRight") )
		{
			mainTabContent[i].classList.toggle("slideLeft");
			mainTabContent[i].classList.toggle("slideRight");
		}
    }
    mainTabLinks = document.getElementsByClassName("NGOOrganizationFormTab");
    mainTabLinks[0].className = mainTabLinks[0].className.replace(" activeTab", "");
    document.getElementById('NGOOrganizationFormPeople').classList.toggle("slideRight");
	document.getElementById('NGOOrganizationFormPeople').classList.toggle("slideLeft");
	mainTabLinks[1].className += " activeTab";
});

/*PeopleForm*/
$(".NGOOrganizationPeopleFormSection1 .nextBtn").click(function(){
	$(".NGOOrganizationPeopleFormSection1").css("top","-100%");
	$(".NGOOrganizationPeopleFormSection1").css("animation","slideTop 0.5s");
	$(".NGOOrganizationPeopleFormSection2").css("top","-100%");
	$(".NGOOrganizationPeopleFormSection2").css("animation","slideTop 0.5s");
});

$(".NGOOrganizationPeopleFormSection2 .backBtn").click(function(){
	$(".NGOOrganizationPeopleFormSection1").css("top","0%");
	$(".NGOOrganizationPeopleFormSection1").css("animation","slideBottom 0.5s");
	$(".NGOOrganizationPeopleFormSection2").css("top","0%");
	$(".NGOOrganizationPeopleFormSection2").css("animation","slideBottom 0.5s");
});

$(".NGOOrganizationPeopleFormSection2 .nextBtn").click(function(){
	$(".NGOOrganizationPeopleFormSection3").css("top","-200%");
	$(".NGOOrganizationPeopleFormSection3").css("animation","slideTop1 0.5s");
	$(".NGOOrganizationPeopleFormSection2").css("top","-200%");
	$(".NGOOrganizationPeopleFormSection2").css("animation","slideTop1 0.5s");
});

$(".NGOOrganizationPeopleFormSection3 .backBtn").click(function(){
	$(".NGOOrganizationPeopleFormSection3").css("top","-100%");
	$(".NGOOrganizationPeopleFormSection3").css("animation","slideBottom1 0.5s");
	$(".NGOOrganizationPeopleFormSection2").css("top","-100%");
	$(".NGOOrganizationPeopleFormSection2").css("animation","slideBottom1 0.5s");
});

$(".NGOOrganizationPeopleFormSection3 .nextBtn").click(function(){
	var i, mainTabContent, mainTabLinks;
    mainTabContent = document.getElementsByClassName("NGOOrganizationFormTabContent");
    for (i = 0; i < mainTabContent.length; i++) {
		if(mainTabContent[i].classList.contains("slideRight") )
		{
			mainTabContent[i].classList.toggle("slideLeft");
			mainTabContent[i].classList.toggle("slideRight");
		}
    }
    mainTabLinks = document.getElementsByClassName("NGOOrganizationFormTab");
    mainTabLinks[1].className = mainTabLinks[1].className.replace(" activeTab", "");
    document.getElementById('NGOOrganizationFormPrevious').classList.toggle("slideRight");
	document.getElementById('NGOOrganizationFormPrevious').classList.toggle("slideLeft");
	mainTabLinks[2].className += " activeTab";
});

$(".NGOOrganizationPeopleFormSection1 .backBtn").click(function(){
	var i, mainTabContent, mainTabLinks;
    mainTabContent = document.getElementsByClassName("NGOOrganizationFormTabContent");
    for (i = 0; i < mainTabContent.length; i++) {
		if(mainTabContent[i].classList.contains("slideRight") )
		{
			mainTabContent[i].classList.toggle("slideLeft");
			mainTabContent[i].classList.toggle("slideRight");
		}
    }
    mainTabLinks = document.getElementsByClassName("NGOOrganizationFormTab");
    mainTabLinks[1].className = mainTabLinks[1].className.replace(" activeTab", "");
    document.getElementById('NGOOrganizationFormBasic').classList.toggle("slideRight");
	document.getElementById('NGOOrganizationFormBasic').classList.toggle("slideLeft");
	mainTabLinks[0].className += " activeTab";
});

/*Previous Work Form*/
$(".NGOOrganizationPreviousFormSection1 .nextBtn").click(function(){
	$(".NGOOrganizationPreviousFormSection1").css("top","-100%");
	$(".NGOOrganizationPreviousFormSection1").css("animation","slideTop 0.5s");
	$(".NGOOrganizationPreviousFormSection2").css("top","-100%");
	$(".NGOOrganizationPreviousFormSection2").css("animation","slideTop 0.5s");
});

$(".NGOOrganizationPreviousFormSection2 .backBtn").click(function(){
	$(".NGOOrganizationPreviousFormSection1").css("top","0%");
	$(".NGOOrganizationPreviousFormSection1").css("animation","slideBottom 0.5s");
	$(".NGOOrganizationPreviousFormSection2").css("top","0%");
	$(".NGOOrganizationPreviousFormSection2").css("animation","slideBottom 0.5s");
});

$(".NGOOrganizationPreviousFormSection2 .nextBtn").click(function(){
	$(".NGOOrganizationPreviousFormSection3").css("top","-200%");
	$(".NGOOrganizationPreviousFormSection3").css("animation","slideTop1 0.5s");
	$(".NGOOrganizationPreviousFormSection2").css("top","-200%");
	$(".NGOOrganizationPreviousFormSection2").css("animation","slideTop1 0.5s");
});

$(".NGOOrganizationPreviousFormSection3 .backBtn").click(function(){
	$(".NGOOrganizationPreviousFormSection3").css("top","-100%");
	$(".NGOOrganizationPreviousFormSection3").css("animation","slideBottom1 0.5s");
	$(".NGOOrganizationPreviousFormSection2").css("top","-100%");
	$(".NGOOrganizationPreviousFormSection2").css("animation","slideBotto1 0.5s");
});

$(".NGOOrganizationPreviousFormSection3 .nextBtn").click(function(){
	$(".NGOOrganizationPreviousFormSection3").css("top","-300%");
	$(".NGOOrganizationPreviousFormSection3").css("animation","slideTop2 0.5s");
	$(".NGOOrganizationPreviousFormSection4").css("top","-300%");
	$(".NGOOrganizationPreviousFormSection4").css("animation","slideTop2 0.5s");
});

$(".NGOOrganizationPreviousFormSection4 .backBtn").click(function(){
	$(".NGOOrganizationPreviousFormSection4").css("top","-200%");
	$(".NGOOrganizationPreviousFormSection4").css("animation","slideBottom2 0.5s");
	$(".NGOOrganizationPreviousFormSection3").css("top","-200%");
	$(".NGOOrganizationPreviousFormSection3").css("animation","slideBottom2 0.5s");
});

$(".NGOOrganizationPreviousFormSection4 .nextBtn").click(function(){
	var i, mainTabContent, mainTabLinks;
    mainTabContent = document.getElementsByClassName("NGOOrganizationFormTabContent");
    for (i = 0; i < mainTabContent.length; i++) {
		if(mainTabContent[i].classList.contains("slideRight") )
		{
			mainTabContent[i].classList.toggle("slideLeft");
			mainTabContent[i].classList.toggle("slideRight");
		}
    }
    mainTabLinks = document.getElementsByClassName("NGOOrganizationFormTab");
    mainTabLinks[2].className = mainTabLinks[2].className.replace(" activeTab", "");
    document.getElementById('NGOOrganizationFormTechnology').classList.toggle("slideRight");
	document.getElementById('NGOOrganizationFormTechnology').classList.toggle("slideLeft");
	mainTabLinks[3].className += " activeTab";
});

$(".NGOOrganizationPreviousFormSection1 .backBtn").click(function(){
	var i, mainTabContent, mainTabLinks;
    mainTabContent = document.getElementsByClassName("NGOOrganizationFormTabContent");
    for (i = 0; i < mainTabContent.length; i++) {
		if(mainTabContent[i].classList.contains("slideRight") )
		{
			mainTabContent[i].classList.toggle("slideLeft");
			mainTabContent[i].classList.toggle("slideRight");
		}
    }
    mainTabLinks = document.getElementsByClassName("NGOOrganizationFormTab");
    mainTabLinks[2].className = mainTabLinks[2].className.replace(" activeTab", "");
    document.getElementById('NGOOrganizationFormPeople').classList.toggle("slideRight");
	document.getElementById('NGOOrganizationFormPeople').classList.toggle("slideLeft");
	mainTabLinks[1].className += " activeTab";
});

/*Technology Form*/
$(".NGOOrganizationTechnologyFormSection1 .nextBtn").click(function(){
	$(".NGOOrganizationTechnologyFormSection1").css("top","-100%");
	$(".NGOOrganizationTechnologyFormSection1").css("animation","slideTop 0.5s");
	$(".NGOOrganizationTechnologyFormSection2").css("top","-100%");
	$(".NGOOrganizationTechnologyFormSection2").css("animation","slideTop 0.5s");
});

$(".NGOOrganizationTechnologyFormSection2 .backBtn").click(function(){
	$(".NGOOrganizationTechnologyFormSection1").css("top","0%");
	$(".NGOOrganizationTechnologyFormSection1").css("animation","slideBottom 0.5s");
	$(".NGOOrganizationTechnologyFormSection2").css("top","0%");
	$(".NGOOrganizationTechnologyFormSection2").css("animation","slideBottom 0.5s");
});

$(".NGOOrganizationTechnologyFormSection2 .nextBtn").click(function(){
	$(".NGOOrganizationTechnologyFormSection3").css("top","-200%");
	$(".NGOOrganizationTechnologyFormSection3").css("animation","slideTop1 0.5s");
	$(".NGOOrganizationTechnologyFormSection2").css("top","-200%");
	$(".NGOOrganizationTechnologyFormSection2").css("animation","slideTop1 0.5s");
});

$(".NGOOrganizationTechnologyFormSection3 .backBtn").click(function(){
	$(".NGOOrganizationTechnologyFormSection3").css("top","-100%");
	$(".NGOOrganizationTechnologyFormSection3").css("animation","slideBottom1 0.5s");
	$(".NGOOrganizationTechnologyFormSection2").css("top","-100%");
	$(".NGOOrganizationTechnologyFormSection2").css("animation","slideBottom1 0.5s");
});

$(".NGOOrganizationTechnologyFormSection3 .nextBtn").click(function(){
	var i, mainTabContent, mainTabLinks;
    mainTabContent = document.getElementsByClassName("NGOOrganizationFormTabContent");
    for (i = 0; i < mainTabContent.length; i++) {
		if(mainTabContent[i].classList.contains("slideRight") )
		{
			mainTabContent[i].classList.toggle("slideLeft");
			mainTabContent[i].classList.toggle("slideRight");
		}
    }
    mainTabLinks = document.getElementsByClassName("NGOOrganizationFormTab");
    mainTabLinks[3].className = mainTabLinks[3].className.replace(" activeTab", "");
    document.getElementById('NGOOrganizationFormContact').classList.toggle("slideRight");
	document.getElementById('NGOOrganizationFormContact').classList.toggle("slideLeft");
	mainTabLinks[4].className += " activeTab";
});

$(".NGOOrganizationTechnologyFormSection1 .backBtn").click(function(){
	var i, mainTabContent, mainTabLinks;
    mainTabContent = document.getElementsByClassName("NGOOrganizationFormTabContent");
    for (i = 0; i < mainTabContent.length; i++) {
		if(mainTabContent[i].classList.contains("slideRight") )
		{
			mainTabContent[i].classList.toggle("slideLeft");
			mainTabContent[i].classList.toggle("slideRight");
		}
    }
    mainTabLinks = document.getElementsByClassName("NGOOrganizationFormTab");
    mainTabLinks[3].className = mainTabLinks[3].className.replace(" activeTab", "");
    document.getElementById('NGOOrganizationFormPrevious').classList.toggle("slideRight");
	document.getElementById('NGOOrganizationFormPrevious').classList.toggle("slideLeft");
	mainTabLinks[2].className += " activeTab";
});

/*Contact Form */
$(".NGOOrganizationContactFormSection1 .nextBtn").click(function(){
	$(".NGOOrganizationContactFormSection1").css("top","-100%");
	$(".NGOOrganizationContactFormSection1").css("animation","slideTop 0.5s");
	$(".NGOOrganizationContactFormSection2").css("top","-100%");
	$(".NGOOrganizationContactFormSection2").css("animation","slideTop 0.5s");
});

$(".NGOOrganizationContactFormSection2 .backBtn").click(function(){
	$(".NGOOrganizationContactFormSection1").css("top","0%");
	$(".NGOOrganizationContactFormSection1").css("animation","slideBottom 0.5s");
	$(".NGOOrganizationContactFormSection2").css("top","0%");
	$(".NGOOrganizationContactFormSection2").css("animation","slideBottom 0.5s");
});

$(".NGOOrganizationContactFormSection1 .backBtn").click(function(){
	var i, mainTabContent, mainTabLinks;
    mainTabContent = document.getElementsByClassName("NGOOrganizationFormTabContent");
    for (i = 0; i < mainTabContent.length; i++) {
		if(mainTabContent[i].classList.contains("slideRight") )
		{
			mainTabContent[i].classList.toggle("slideLeft");
			mainTabContent[i].classList.toggle("slideRight");
		}
    }
    mainTabLinks = document.getElementsByClassName("NGOOrganizationFormTab");
    mainTabLinks[4].className = mainTabLinks[4].className.replace(" activeTab", "");
    document.getElementById('NGOOrganizationFormTechnology').classList.toggle("slideRight");
	document.getElementById('NGOOrganizationFormTechnology').classList.toggle("slideLeft");
	mainTabLinks[3].className += " activeTab";
});

/*Basicform*/
$(".NGOIndividualBasicFormSection1 .nextBtn").click(function(){
	$(".NGOIndividualBasicFormSection1").css("top","-100%");
	$(".NGOIndividualBasicFormSection1").css("animation","slideTop 0.5s");
	$(".NGOIndividualBasicFormSection2").css("top","-100%");
	$(".NGOIndividualBasicFormSection2").css("animation","slideTop 0.5s");
});

$(".NGOIndividualBasicFormSection2 .backBtn").click(function(){
	$(".NGOIndividualBasicFormSection1").css("top","0%");
	$(".NGOIndividualBasicFormSection1").css("animation","slideBottom 0.5s");
	$(".NGOIndividualBasicFormSection2").css("top","0%");
	$(".NGOIndividualBasicFormSection2").css("animation","slideBottom 0.5s");
});

$(".NGOIndividualBasicFormSection2 .nextBtn").click(function(){
	$(".NGOIndividualBasicFormSection3").css("top","-200%");
	$(".NGOIndividualBasicFormSection3").css("animation","slideTop1 0.5s");
	$(".NGOIndividualBasicFormSection2").css("top","-200%");
	$(".NGOIndividualBasicFormSection2").css("animation","slideTop1 0.5s");
});

$(".NGOIndividualBasicFormSection3 .backBtn").click(function(){
	$(".NGOIndividualBasicFormSection3").css("top","-100%");
	$(".NGOIndividualBasicFormSection3").css("animation","slideBottom1 0.5s");
	$(".NGOIndividualBasicFormSection2").css("top","-100%");
	$(".NGOIndividualBasicFormSection2").css("animation","slideBottom1 0.5s");
});

$(".NGOIndividualBasicFormSection3 .nextBtn").click(function(){
	$(".NGOIndividualBasicFormSection3").css("top","-300%");
	$(".NGOIndividualBasicFormSection3").css("animation","slideTop2 0.5s");
	$(".NGOIndividualBasicFormSection4").css("top","-300%");
	$(".NGOIndividualBasicFormSection4").css("animation","slideTop2 0.5s");
});

$(".NGOIndividualBasicFormSection4 .backBtn").click(function(){
	$(".NGOIndividualBasicFormSection4").css("top","-200%");
	$(".NGOIndividualBasicFormSection4").css("animation","slideBottom2 0.5s");
	$(".NGOIndividualBasicFormSection3").css("top","-200%");
	$(".NGOIndividualBasicFormSection3").css("animation","slideBottom2 0.5s");
});

$(".NGOIndividualBasicFormSection4 .nextBtn").click(function(){
	var i, mainTabContent, mainTabLinks;
    mainTabContent = document.getElementsByClassName("NGOIndividualFormTabContent");
    for (i = 0; i < mainTabContent.length; i++) {
		if(mainTabContent[i].classList.contains("slideRight") )
		{
			mainTabContent[i].classList.toggle("slideLeft");
			mainTabContent[i].classList.toggle("slideRight");
		}
    }
    mainTabLinks = document.getElementsByClassName("NGOIndividualFormTab");
    mainTabLinks[0].className = mainTabLinks[0].className.replace(" activeTab", "");
    document.getElementById('NGOIndividualFormMotivation').classList.toggle("slideRight");
	document.getElementById('NGOIndividualFormMotivation').classList.toggle("slideLeft");
	mainTabLinks[1].className += " activeTab";
});

/*PeopleForm*/
$(".NGOIndividualMotivationFormSection1 .nextBtn").click(function(){
	$(".NGOIndividualMotivationFormSection1").css("top","-100%");
	$(".NGOIndividualMotivationFormSection1").css("animation","slideTop 0.5s");
	$(".NGOIndividualMotivationFormSection2").css("top","-100%");
	$(".NGOIndividualMotivationFormSection2").css("animation","slideTop 0.5s");
});

$(".NGOIndividualMotivationFormSection2 .backBtn").click(function(){
	$(".NGOIndividualMotivationFormSection1").css("top","0%");
	$(".NGOIndividualMotivationFormSection1").css("animation","slideBottom 0.5s");
	$(".NGOIndividualMotivationFormSection2").css("top","0%");
	$(".NGOIndividualMotivationFormSection2").css("animation","slideBottom 0.5s");
});

$(".NGOIndividualMotivationFormSection2 .nextBtn").click(function(){
	$(".NGOIndividualMotivationFormSection3").css("top","-200%");
	$(".NGOIndividualMotivationFormSection3").css("animation","slideTop1 0.5s");
	$(".NGOIndividualMotivationFormSection2").css("top","-200%");
	$(".NGOIndividualMotivationFormSection2").css("animation","slideTop1 0.5s");
});

$(".NGOIndividualMotivationFormSection3 .backBtn").click(function(){
	$(".NGOIndividualMotivationFormSection3").css("top","-100%");
	$(".NGOIndividualMotivationFormSection3").css("animation","slideBottom1 0.5s");
	$(".NGOIndividualMotivationFormSection2").css("top","-100%");
	$(".NGOIndividualMotivationFormSection2").css("animation","slideBottom1 0.5s");
});

$(".NGOIndividualMotivationFormSection1 .backBtn").click(function(){
	var i, mainTabContent, mainTabLinks;
    mainTabContent = document.getElementsByClassName("NGOIndividualFormTabContent");
    for (i = 0; i < mainTabContent.length; i++) {
		if(mainTabContent[i].classList.contains("slideRight") )
		{
			mainTabContent[i].classList.toggle("slideLeft");
			mainTabContent[i].classList.toggle("slideRight");
		}
    }
    mainTabLinks = document.getElementsByClassName("NGOIndividualFormTab");
    mainTabLinks[1].className = mainTabLinks[1].className.replace(" activeTab", "");
    document.getElementById('NGOIndividualFormBasic').classList.toggle("slideRight");
	document.getElementById('NGOIndividualFormBasic').classList.toggle("slideLeft");
	mainTabLinks[0].className += " activeTab";
});

/*nationality*/
$('#nationality').change(function(){
	if($(this).val()==="India"){
		$("#aadharCard").css("opacity","1");
		$("#aadharCard").css("max-height","230px");
		$("#aadharCard").css("overflow","visible");
		$("#aadharCard").css("display","block");
		$("#passportNumber").css("display","none");
		$("#passportNumber").css("opacity","0");
		$("#passportNumber").css("max-height","0px");
		$("#passportNumber").css("overflow","hidden");
	}
	else if($(this).val()==="Choose"){
		$("#passportNumber").css("opacity","0");
		$("#passportNumber").css("max-height","230px");
		$("#aadharCard").css("opacity","0");
		$("#aadharCard").css("max-height","0px");
	}
	else{
		$("#passportNumber").css("opacity","1");
		$("#passportNumber").css("max-height","230px");
		$("#passportNumber").css("overflow","visible");
		$("#passportNumber").css("display","block");
		$("#aadharCard").css("display","none");
		$("#aadharCard").css("opacity","0");
		$("#aadharCard").css("max-height","0px");
		$("#aadharCard").css("overflow","hidden");
	}
});