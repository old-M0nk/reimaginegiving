from django.shortcuts import render

from django.http import HttpResponse

from django.template import RequestContext
from data.models import Project


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


def projectPage (request):
    return render(request, 'projectPage.html')


def viewAllProjects (request):
    return render(request, 'viewAllProjects.html')


def checkOut (request):
    return render(request, 'checkOut.html')


def projectPage (request):
    return render(request, 'projectPage.html')

def contactUsPage (request):
    return render(request, 'contactUsPage.html')



