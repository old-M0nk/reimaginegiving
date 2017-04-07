from django.shortcuts import render, render_to_response
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
                    return render(request, 'checkOut.html', {'amount': amount, 'project':project, 'ngo':ngo, 'title':name, 'form': form, 'pk': pk}, context)
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
    from instamojo_wrapper import Instamojo
    api = Instamojo(api_key='4ede38968eb0f1e6ce1f236338b767d3',
                    auth_token='d44d2e46a7b39f6dfc86d2d144a432fd')

    # Create a new Payment Request
    response1 = api.payment_request_create(
        amount=request.POST['amount'],
        purpose=request.POST['project'],
        send_email=True,
        email=request.POST['email']
    )
    print response1
    return render_to_response(response1)
    # # print the long URL of the payment request.
    # print response['payment_request']['longurl']
    # # print the unique ID(or payment request ID)
    # print response['payment_request']['id']



from django.template.loader import get_template
from django.template import Context, Template, RequestContext
import datetime
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf


# def payment_redirect(request):
#     previous_page = request.META['HTTP_REFERER']
#     MERCHANT_KEY = "5771062"
#     key = "oplRyvbH"
#     SALT = "pxlrngrbm4"
#     PAYU_BASE_URL = "https://secure.payu.in/_payment"
#     action = ''
#     posted = {}
#     for i in request.POST:
#         posted[i] = request.POST[i]
#     hash_object = hashlib.sha256(b'randint(0,20)')
#     txnid = hash_object.hexdigest()[0:20]
#     hashh = ''
#     posted['txnid'] = txnid
#     hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
#     posted['key'] = key
#     posted['amount'] = request.POST['amount']
#     posted['productinfo'] = request.POST['project']
#     print posted['productinfo']
#     posted['firstname'] = request.POST['first_name']
#     posted['email'] = request.POST['email']
#     posted['mobile'] = request.POST['mobile']
#     hash_string = ''
#     hashVarsSeq = hashSequence.split('|')
#     for i in hashVarsSeq:
#         try:
#             hash_string += str(posted[i])
#         except Exception:
#             hash_string += ''
#         hash_string += '|'
#     hash_string += SALT
#     hashh = hashlib.sha512(hash_string).hexdigest().lower()
#     action = PAYU_BASE_URL
#     if (posted.get("key") != None and posted.get("txnid") != None and posted.get("productinfo") != None and posted.get("firstname") != None and posted.get("email") != None):
#         if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?))$", request.POST['email']) != None:
#             if re.match("^[0-9]*$", request.POST['mobile']) and len(str(request.POST['mobile'])) == 10:
#                 return render_to_response('payment_redirect.html', RequestContext(request, {"posted": posted, "hashh": hashh,
#                                                                                             "MERCHANT_KEY": MERCHANT_KEY,
#                                                                                             "txnid": txnid,
#                                                                                             "hash_string": hash_string,
#                                                                                             'amount': posted['amount'],
#                                                                                             'project': posted['productinfo'],
#                                                                                             'firstname': posted['firstname'],
#                                                                                             'email': posted['email'],
#                                                                                             'mobile': posted['mobile'],
#                                                                                             'key': posted['key'],
#                                                                                             "action": "https://secure.payu.in/_payment"}))
#             else:
#                 messages.add_message(request, messages.ERROR, 'Enter a valid mobile number.', extra_tags="mobile")
#                 previous_page = request.META['HTTP_REFERER']
#                 request.session['amount'] = request.POST['amount']
#                 return render(request, 'payment_redirect.html', {'previous_page': previous_page})
#
#         else:
#             messages.add_message(request, messages.ERROR, 'Enter a valid e-mail address.', extra_tags="email")
#             previous_page = request.META['HTTP_REFERER']
#             request.session['amount'] = request.POST['amount']
#             return render(request, 'payment_redirect.html', {'previous_page':previous_page})
#
#     else:
#         return render_to_response('payment_redirect.html', RequestContext(request, {"posted": posted, "hashh": hashh,
#                                                                                     "MERCHANT_KEY": MERCHANT_KEY,
#                                                                                     "txnid": txnid,
#                                                                                     "hash_string": hash_string,
#                                                                                     "action": "."}))
#
#
@csrf_protect
@csrf_exempt
def success(request):
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
    return render_to_response('sucess.html',
                              RequestContext(request, {"txnid": txnid, "status": status, "amount": amount}))


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



