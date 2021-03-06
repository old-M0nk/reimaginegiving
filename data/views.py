from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from datetime import datetime
from django.template import RequestContext
from data.models import Project, GiveOnce, GiveMonthly, TimelineEvent, Report, GalleryPic
from users.models import ContactUs, Donation
from users.forms import contact_us_form
from django.db.models import F
from forms import *
from django.contrib import messages
from django.shortcuts import redirect
import re






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
    def filter():
        if request.POST.get('funding_level', False) != False:
            print ('pass1')
            if request.POST['funding_level'] == "nearly_funded":
                project_list = Project.objects.annotate(x=F('raised_amount') / F('total_amount')).filter(x__gte=0.8)
                print ('pass2')
            elif request.POST['funding_level'] == "just_started":
                project_list = Project.objects.annotate(x=F('raised_amount') / F('total_amount')).filter(x__lte=0.2)
                print ('pass3')
            elif request.POST['funding_level'] == "ongoing":
                print ('pass4')
                project_list = Project.objects.annotate(x=F('raised_amount') / F('total_amount')).filter(x__lte=1,end_date__gte=datetime.date.today())
        else:
            project_list = Project.objects.all()
        # if request.POST.get('all_causes', False) == 'True':
        #     pass
        if request.POST.get('education', False) != 'True' and request.POST.get('poverty', False) != 'True' and request.POST.get('sanitation', False) != 'True' and request.POST.get('child_welfare', False) != 'True' and request.POST.get('skill_development', False) != 'True' and request.POST.get('disaster_recovery', False) != 'True' and request.POST.get('lgbtq', False) != 'True' and request.POST.get('technology', False) != 'True' and request.POST.get('arts_and_culture', False) != 'True' and request.POST.get('environment', False) != 'True':
            pass
        else:
            if request.POST.get('education', False) != 'True':
                print ('pass1')
                project_list = project_list.exclude(cause__name='Education')
            if request.POST.get('poverty', False) != 'True':
                print ('pass2')
                project_list = project_list.exclude(cause__name='Poverty')
            if request.POST.get('sanitation', False) != 'True':
                print ('pass3')
                project_list = project_list.exclude(cause__name='Sanitation')
            if request.POST.get('child_welfare', False) != 'True':
                print ('pass4')
                project_list = project_list.exclude(cause__name='Child Welfare')
            if request.POST.get('skill_development', False) != 'True':
                print ('pass5')
                project_list = project_list.exclude(cause__name='Skill Development')
            if request.POST.get('disaster_recovery', False) != 'True':
                print ('pass6')
                project_list = project_list.exclude(cause__name='Disaster Recovery')
            if request.POST.get('lgbtq', False) != 'True':
                print ('pass7')
                project_list = project_list.exclude(cause__name='LGBTQ')
            if request.POST.get('technology', False) != 'True':
                print ('pass8')
                project_list = project_list.exclude(cause__name='Technology')
            if request.POST.get('arts_and_culture', False) != 'True':
                print ('pass9')
                project_list = project_list.exclude(cause__name='Arts & Culture')
            if request.POST.get('environment', False) != 'True':
                print ('pass10')
                project_list = project_list.exclude(cause__name='Environment')

        return project_list




    if cause == 'all' and funding == 'all':
        if request.method == 'POST' and request.POST['submit'] == 'filter':
            print ('pass')
            project_list = filter()
            project_count = project_list.count()
        else:
            project_list = Project.objects.all()  ###view all project... no logic used...
            project_count = project_list.count()
    elif cause != 'all':
        if request.method == 'POST' and request.POST['submit'] == 'filters':
            project_list = filter()
            project_count = project_list.count()
        else:
            project_list = Project.objects.filter(cause__name=cause)
            project_count = project_list.count()
    elif funding != 'all':
        if request.method == 'POST' and request.POST['submit'] == 'filters':
            project_list = filter()
            project_count = project_list.count()
        else:
            if funding == 'nearly_funded':
                project_list = Project.objects.annotate(x=F('raised_amount')/F('total_amount')).filter(x__gte=0.8)
                project_count = project_list.count()
            elif funding == 'just_started':
                project_list = Project.objects.annotate(x=F('raised_amount') / F('total_amount')).filter(x__lte=0.2)
                project_count = project_list.count()
            elif funding == 'ongoing':
                project_list = Project.objects.annotate(x=F('raised_amount') / F('total_amount')).filter(x__lte=1,
                                                                                                         end_date__gte=datetime.date.today())
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
            import re
            if re.match("^[0-9]*$", request.POST['amount']):
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


from django.template.loader import get_template
from django.template import Context, Template, RequestContext
import datetime
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf
from instamojo_wrapper import Instamojo

def payment_redirect(request):
    api = Instamojo(api_key='27fb8178a52dc8e02866df53267d016d',
                    auth_token='4c5d72dcdaa1e81b2ec37525609dd6b5', endpoint='https://test.instamojo.com/api/1.1/')

    # Create a new Payment Request
    firstname = request.POST["first_name"]
    amount = request.POST["amount"]
    email = request.POST["email"]
    phone = request.POST["mobile"]
    project = request.POST["project"]
    print project
    response = api.payment_request_create(
        amount=amount,
        purpose = project,
        send_email=True,
        email=email,
        phone=phone,
        buyer_name =  firstname,
        redirect_url="http://www.reimaginegiving.org/Success/"
    )
    # print the long URL of the payment request.
    print response
    response1 = response['payment_request']['longurl']
    print response1
    # print the unique ID(or payment request ID)
    # print response['payment_request']['id']
    return redirect(response1)

@csrf_protect
@csrf_exempt
def success(request):
    from django.contrib.auth.models import User
    api = Instamojo(api_key='27fb8178a52dc8e02866df53267d016d',
                    auth_token='4c5d72dcdaa1e81b2ec37525609dd6b5', endpoint='https://test.instamojo.com/api/1.1/')
    # Create a new Payment Request
    payment_request_id = request.GET["payment_request_id"]
    txnid = request.GET["payment_id"]
    response = api.payment_request_status(payment_request_id)

    print response['payment_request']['shorturl']  # Get the    short URL
    print response['payment_request']['status']  # Get the current status
    print response['payment_request']['payments']  # List of payments
    print response['payment_request']['amount']

    status = response['payment_request']['status']
    amount = response['payment_request']['amount']
    print("\n\n ", request.user)
    if request.user.is_authenticated():
        print "true"
        donation = Donation(name=response['payment_request']['buyer_name'],
                            transaction_id=txnid,
                            donor_id=request.user,
                            project_id_id=response['payment_request']['purpose'],
                            amount= amount)
    else:
        print "false"
        donation = Donation(name=response['payment_request']['buyer_name'],
                            transaction_id=txnid,
                            donor_id=User.objects.get(username="reimagine"),
                            project_id_id=response['payment_request']['purpose'],
                            amount=amount)
    donation.save()
    def raised_amount(project_id):
        donations = Donation.objects.filter(project_id=response['payment_request']['purpose'])
        print donations
        r_amt = 0
        for donation in donations:
            print donation
            r_amt = r_amt + donation.amount
            print r_amt
        return r_amt
    project = Project.objects.get(project_id=response['payment_request']['purpose'])
    project.raised_amount = raised_amount(response['payment_request']['purpose'])
    project.save()

    return render(request, 'sucess.html', {"status": status,
                                           "amount": amount,
                                           "txnid":txnid,
                                           'name':response['payment_request']['buyer_name'],
                                           'project_id':response['payment_request']['purpose'],
                                           'amount': amount})


def test(request):
    from django.contrib.auth.models import User
    if request.method == "POST":

        if request.user.is_authenticated():
            print "true"
            donation = Donation(name=request.POST['name'],
                                transaction_id=request.POST['transaction_id'],
                                donor_id=request.user,
                                project_id_id=request.POST['project_id'],
                                amount= request.POST['amount'])
        else:
            print "false"
            donation = Donation(name=request.POST['name'],
                                transaction_id=request.POST['transaction_id'],
                                donor_id=User.objects.get(username="reimagine"),
                                project_id_id=request.POST['project_id'],
                                amount=request.POST['amount'])
        donation.save()
    return render(request, 'soon.html')