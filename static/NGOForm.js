$(".NGOFormOptionIndividual a").click(function(){
	$(".IndividualForm").toggleClass("IndividualFormOpen");
});

$(".NGOFormOptionOrganization a").click(function(){
	$(".OrganizationForm").toggleClass("OrganizationFormOpen");
});

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

$(".NGOOrganizationContactFormSection2 .nextBtn").click(function(){
	$(".NGOOrganizationContactFormSection3").css("top","-200%");
	$(".NGOOrganizationContactFormSection3").css("animation","slideTop1 0.5s");
	$(".NGOOrganizationContactFormSection2").css("top","-200%");
	$(".NGOOrganizationContactFormSection2").css("animation","slideTop1 0.5s");
});

$(".NGOOrganizationContactFormSection3 .backBtn").click(function(){
	$(".NGOOrganizationContactFormSection3").css("top","-100%");
	$(".NGOOrganizationContactFormSection3").css("animation","slideBottom1 0.5s");
	$(".NGOOrganizationContactFormSection2").css("top","-100%");
	$(".NGOOrganizationContactFormSection2").css("animation","slideBotto1 0.5s");
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