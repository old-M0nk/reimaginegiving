from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from datetime import datetime
from django.template import RequestContext
from data.models import Project, GiveOnce, GiveMonthly, TimelineEvent, Report, GalleryPic
from users.models import ContactUs
from users.forms import contact_us_form
from django.db.models import F
from forms import *
from django.contrib import messages
from instamojo_wrapper import Instamojo
from django.template.loader import get_template
from django.template import Context, Template, RequestContext
import datetime
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf







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
        project_count = project_list.count()
    elif cause != 'all':
        project_list = Project.objects.filter(cause__name=cause)
        project_count = project_list.count()
    elif funding != 'all':
        if funding == 'nearly_funded':
            project_list = Project.objects.annotate(x=F('raised_amount')/F('total_amount')).filter(x__gte=0.8)
            project_count = project_list.count()
        elif funding == 'just_started':
            project_list = Project.objects.annotate(x=F('raised_amount') / F('total_amount')).filter(x__lte=0.2)
            project_count = project_list.count()
        elif funding == 'ongoing':
            project_list = Project.objects.annotate(x=F('raised_amount') / F('total_amount')).filter(x__lte=1, end_date__gte=datetime.date.today())
            project_count = project_list.count()
    context_dict = {'projects': project_list,
                    'count': project_count}
    return render(request, 'viewAllProjects.html', context_dict, context)


def checkOut(request, pk):
    context = RequestContext(request)
    project = Project.objects.get(project_id=pk)
    name = project.title
    ngo = project.ngo_id.name
    form = PaymentDetailsForm(request.POST or None)

    if 'amount' not in request.session:
        if request.method == "POST":
            print (request.POST['amount'])
            import re
            if re.match("^[0-9]+(\.[0-9]{1,2})?$", request.POST['amount']):
                if request.POST['amount']:
                    amount = request.POST['amount']
                    print amount
                    return render(request, 'checkOut.html', {'amount': amount, 'project':project.title, 'ngo':ngo, 'title':name, 'form': form, 'pk': pk}, context)
                else:
                    messages.add_message(request, messages.ERROR, 'Enter a valid amount.', extra_tags="amount")
                    url = reverse('projectPage', kwargs={'pk': pk})
                    return HttpResponseRedirect(url)
            else:
                messages.add_message(request, messages.ERROR, 'Enter a valid amount.', extra_tags="amount")
                url = reverse('projectPage', kwargs={'pk': pk})
                return HttpResponseRedirect(url)
        else:
            url = reverse('projectPage', kwargs={'pk': pk})
            return HttpResponseRedirect(url)
    else:
        amount = request.session['amount']
        request.session.clear()
        print amount
        return render(request, 'checkOut.html',
                      {'amount': amount, 'project': project, 'ngo': ngo, 'title': name, 'form': form, 'pk': pk},
                      context)





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

def payment_redirect(request):
    api = Instamojo(api_key='27fb8178a52dc8e02866df53267d016d',
                    auth_token='4c5d72dcdaa1e81b2ec37525609dd6b5', endpoint='https://test.instamojo.com/api/1.1/')

    # Create a new Payment Request
    # firstname = request.POST["first_name"]
    amount = request.POST["amount"]
    email = request.POST["email"]
    # phone = request.POST["mobile"]
    # project = request.POST["project"]
    # print project
    response = api.payment_request_create(
        amount=amount,
        purpose='FIFA 16',
        send_email=True,
        email=email
    )
    # print the long URL of the payment request.
    response1 = response['payment_request']['longurl']
    print response1
    # print the unique ID(or payment request ID)
    print response['payment_request']['id']
    return redirect(response1)






@csrf_protect
@csrf_exempt
def success(request):
    api = Instamojo(api_key='27fb8178a52dc8e02866df53267d016d',
                    auth_token='4c5d72dcdaa1e81b2ec37525609dd6b5', endpoint='https://test.instamojo.com/api/1.1/')

    # Create a new Payment Request
    payment_request_id = request.GET["payment_request_id"]
    txnid = request.GET["payment_id"]
    response = api.payment_request_status(payment_request_id)

    print response['payment_request']['shorturl']  # Get the short URL
    print response['payment_request']['status']  # Get the current status
    print response['payment_request']['payments']  # List of payments
    print response['payment_request']['amount']

    status = response['payment_request']['status']
    amount = response['payment_request']['amount']

    return render(request, 'sucess.html', {"status": status,"amount": amount,"txnid":txnid})


@csrf_protect
@csrf_exempt
def failure(request):
    c = {}
    c.update(csrf(request))
    status = request.POST["status"]
    firstname = request.POST["firstname"]
    amount = request.POST["amount"]
    txnid = request.POST["txnid"]
    posted_hash = request.POST["hash"]
    key = request.POST["key"]
    productinfo = request.POST["productinfo"]
    email = request.POST["email"]
    salt = "GQs7yium"
    try:
        additionalCharges = request.POST["additionalCharges"]
        retHashSeq = additionalCharges + '|' + salt + '|' + status + '|||||||||||' + email + '|' + firstname + '|' + productinfo + '|' + amount + '|' + txnid + '|' + key
    except Exception:
        retHashSeq = salt + '|' + status + '|||||||||||' + email + '|' + firstname + '|' + productinfo + '|' + amount + '|' + txnid + '|' + key
    hashh = hashlib.sha512(retHashSeq).hexdigest().lower()
    if (hashh != posted_hash):
        print "Invalid Transaction. Please try again"
    else:
        print "Thank You. Your order status is ", status
        print "Your Transaction ID for this transaction is ", txnid
        print "We have received a payment of Rs. ", amount, ". Your order will soon be shipped."
    return render_to_response("Failure.html", RequestContext(request, c))

#
# from django.contrib.auth.models import User
# from django.http import JsonResponse
#
# def validate_username(request):
#     username = request.GET.get('username', None)
#     data = {
#         'is_taken': User.objects.filter(username__iexact=username).exists()
#     }
#     if data['is_taken']:
#         data['error_message'] = 'A user with this username already exists.'
#     return JsonResponse(data)



