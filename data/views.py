from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from datetime import datetime
from django.template import RequestContext
from data.models import Project, GiveOnce, GiveMonthly, TimelineEvent, Report, GalleryPic
from users.models import ContactUs
from users.forms import contact_us_form


def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    project_list = Project.objects.all() ###view all project... no logic used...
    context_dict = {'projects': project_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'index.html', context_dict, context)


def teamPage (request):
    return render(request, 'teamPage.html')


def userPage (request):
    return render(request, 'userPage.html')


def projectPage (request, pk):
    context = RequestContext(request)
    project_list = Project.objects.all()
    give_once_options = GiveOnce.objects.filter(project_id=pk)
    give_monthly_options = GiveMonthly.objects.filter(project_id=pk)
    project = Project.objects.get(project_id=pk)
    gallery = GalleryPic.objects.filter(project_id=pk)
    gallery_count = GalleryPic.objects.filter(project_id=pk).count()
    amount_left = project.total_amount-project.raised_amount
    progress_percent = (project.raised_amount)*100/(project.total_amount)
    desc = project.project_page_desc
    ngo_desc = project.ngo_id.project_page_desc
    ngo = project.ngo_id.name
    timeline = TimelineEvent.objects.filter(project_id=pk).order_by('date')
    report = Report.objects.filter(project_id=pk).order_by('date')
    # stars = project.rating

    context_dict = {'project': project,
                    'amount_left': amount_left,
                    'progress_percent': progress_percent,
                    'desc': desc,
                    'name': ngo,
                    'ngo_desc': ngo_desc,
                    'projects': project_list,
                    'pk': pk,
                    'give_once_options': give_once_options,
                    'give_monthly_options': give_monthly_options,
                    'events': timeline,
                    'reports': report,
                    'gallery': gallery,
                    'gallery_count': gallery_count}
                    # 'stars': stars
    return render(request, 'projectPage.html', context_dict, context)


def viewAllProjects (request, cause, funding):
    context = RequestContext(request)
    if cause == 'all' and funding == 'all':
        project_list = Project.objects.all()  ###view all project... no logic used...
        project_count = Project.objects.count()
    elif cause != 'all':
        project_list = Project.objects.filter(cause__name=cause)  ###view all project... no logic used...
        project_count = Project.objects.filter(cause__name=cause).count()
    elif funding != 'all':
        project_list = Project.objects.filter((raised_amount)/(total_amount)<0.2)
    context_dict = {'projects': project_list,
                    'count': project_count}
    return render(request, 'viewAllProjects.html', context_dict, context)


def checkOut(request, pk):
    context = RequestContext(request)
    project = Project.objects.get(project_id=pk)
    name = project.title
    ngo = project.ngo_id.name

    if request.method == "POST":
            if request.POST['amount']:
                amount = request.POST['amount']
                print amount
                return render(request, 'checkOut.html', {'amount': amount, 'project':project, 'ngo':ngo, 'title':name}, context)
            else:
                url = reverse('projectPage', kwargs={'pk': pk})
                return HttpResponseRedirect(url)
    else:
        url = reverse('projectPage', kwargs={'pk': pk})
        return HttpResponseRedirect(url)




def contactUsPage (request):
    if request.method == "POST":
        myform = contact_us_form(request.POST)
        print(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        def validateEmail(email):
            from django.core.validators import validate_email
            from django.core.exceptions import ValidationError
            try:
                validate_email(email)
                return True
            except ValidationError:
                return False

        if validateEmail(email):
            contact_us_obj = ContactUs(name= name, email= email, message= message)
            # saving all the data in the current object into the database
            contact_us_obj.save()
            context_dict = {'message': 'Thank You!'}
        else:
            context_dict = {'value':email,'message': 'Enter a valid e-mail address', 'form': myform}
    else:
        myform = contact_us_form()
        context_dict = {'form': myform}
    return render(request, 'contactUsPage.html', context_dict)


def aboutus (request):
    return render(request, 'aboutus.html')
def privacy (request):
    return render(request, 'privacy.html')
def terms (request):
    return render(request, 'terms.html')
def refund (request):
    return render(request, 'refund.html')
def pricing (request):
    return render(request, 'pricing.html')

