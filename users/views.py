from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import login, logout, get_user_model
# from django.contrib.auth.models import User
# from django.template import RequestContext, loader, Context
# from django.views import generic
# from django.views.generic import View
from .forms import *
from .models import *
from data.models import NGOtemp, Project
from django.contrib.auth import authenticate as auth
from django.contrib.auth.decorators import login_required
import datetime
from django.db.models import F, Q
from django.contrib import messages

def comingSoon(request):
    if request.method == "POST":
        myform = email_form(request.POST)
        print(request.POST)
        email = request.POST['email']

        def validateEmail(email):
            from django.core.validators import validate_email
            from django.core.exceptions import ValidationError
            try:
                validate_email(email)
                return True
            except ValidationError:
                return False

        if validateEmail(email):
            if not Email.objects.filter(email=email).exists():
            # creating an user object containing all the data
                email_obj = Email(email= email)
            # saving all the data in the current object into the database
                email_obj.save()
                context_dict = {'message': 'Thank You!'}
            else:
                context_dict = {'message': 'You have already registered with us', 'form': myform}
        else:
            context_dict = {'value':email,'message': 'Enter a valid e-mail address', 'form': myform}
    else:
        myform = email_form()
        context_dict = {'form': myform}

    return render(request, 'comingSoon.html', context_dict)

#you have to comulsorily use '_view' because Django already has a login(), logout() method


def login_view(request):
    if request.method == "POST": #if the form has been submitted
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        u = User.objects.filter(username=username)
        print("sadfh",u)
        user = auth(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print("True")
            message = "Welcome"
            project_list = Project.objects.all()  ###view all project... no logic used...
            context_dict = {'message': message, 'projects': project_list}
            page = 'index.html'
        else:
            # Return an 'invalid login' error message.
            project_list = Project.objects.all()  ###view all project... no logic used...
            context_dict = {'message': 'Incorrect Credentials', 'form': form, 'projects': project_list}
            page = 'index.html'

    else:#if the form has not been submitted
        form = UserLoginForm(request.POST or None)
        project_list = Project.objects.all()  ###view all project... no logic used...
        context_dict = {'form':form, 'projects': project_list}
        page = 'index.html'
    #
    # if request.user.is_authenticated():
    return render(request, page, context_dict)


def register_view(request):
    if request.method == "POST":  # if the form has been submitted
        form = UserRegistrationForm(request.POST or None)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        import re

        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?))$", request.POST['username'] )!= None:
            # check if the passwords match
            if password == password2:
                user = User(username=username, email=username, password=password, first_name=first_name,
                            last_name=last_name)
                # user = user.save(commit=False)
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                user.set_password(password)
                user.save()
                user_details = User_Details(username=user)
                user_details.save()
                notifications = Notification(username=user)
                notifications.save()
                login(request, user)
                context_dict = {
                    "message": "Welcome",
                }
            else:
                context_dict = {'form': form, 'message': "Passwords did not match!"}
        else:
            context_dict = {'form': form, 'message': "Enter a valid Email address!"}



    else:
        form = UserRegistrationForm(request.POST or None)
        context_dict = {'form': form}
    return render(request, 'index.html', context_dict)


def validate_username(request):
    print ('pass1')
    from django.http import JsonResponse
    username = request.GET.get('username', None)
    print (username)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)


def validate_password(request):
    print ('pass2')
    from django.http import JsonResponse
    password = request.GET.get('password', None)
    password2 = request.GET.get('password2', None)
    def passcheck():
        if password == password2:
            print ('True')
            return True
        else:
            print ('False')
            return False
    data = {
        'is_not_equal': not passcheck()
    }
    if data['is_not_equal']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')
    # return render(request, 'index.html', {})


@login_required
def userPage(request):

    user_details = User_Details.objects.get(username=request.user)
    if not Notification.objects.filter(username=request.user).exists():
        print('pass1')
        notifications = Notification(username=request.user)
        notifications.save()
    if not User_Details.objects.filter(username=request.user).exists():
            print('pass1')
            user_details = User_Details(username=request.user)
            user_details.save()
    notification = Notification.objects.get(username=request.user)

    if request.method == "POST" and request.POST['submit'] == "basic":
        request.user.first_name = request.POST['first_name']
        request.user.last_name = request.POST['last_name']
        request.user.save()
        user_details.mobile_number = request.POST['mobile']
        user_details.pan_number = request.POST['pan']
        user_details.occupation = request.POST['occupation']
        user_details.save()

    if request.method == "POST" and request.POST['submit'] == "mailing":
        user_details.address_line_1 = request.POST['address_line_1']
        user_details.address_line_2 = request.POST['address_line_2']
        user_details.city = request.POST['city']
        user_details.pincode = request.POST['pincode']
        user_details.pan_number = request.POST['pan']
        user_details.occupation = request.POST['occupation']
        user_details.save()

    if request.method == "POST" and request.POST['submit'] == "notifications":
        form = NotificationForm(request.POST or None)
        supp_mob = request.POST.get('supp_mob', False)
        supp_mail = request.POST.get('sup_mail', False)
        gen_mob = request.POST.get('gen_mob', False)
        gen_mail = request.POST.get('gen_mail', False)
        exc_mob = request.POST.get('exc_mob', False)
        exc_mail = request.POST.get('exc_mail', False)

        notification = Notification.objects.get(username=request.user)
        notification.supported_projects_mobile = supp_mob
        notification.supported_projects_email = supp_mail
        notification.general_mobile = gen_mob
        notification.general_email = gen_mail
        notification.exciting_projects_mobile = exc_mob
        notification.exciting_projects_email = exc_mail
        notification.save()
    else:
        form = NotificationForm(request.POST or None)

    # if Card_Details.objects.filter(username=request.user).count():
    #     card_details = Card_Details.objects.get(username=request.user)
    # else:
    #     card_details = False
    if request.method == "POST" and request.POST['submit'] == "card":
        card_form = CardDetailsForm(request.POST or None)
        card_number = request.POST['num1']+request.POST['num2']+request.POST['num3']+request.POST['num4']
        date = request.POST['month']+'/'+request.POST['year']
        card = Card_Details(username=request.user,
                            card_number=card_number,
                            card_holder=request.POST['name'],
                            expiration_date=date,
                            cvv=request.POST['cvv'])
        card.save()
    else:
        card_form = CardDetailsForm(request.POST or None)
    cards = Card_Details.objects.filter(username=request.user)

    if request.method == "POST" and request.POST['submit'] == "change_password":
        cp_form = ChangePasswordForm(request.POST or None)
        user = request.user
        if auth(username=request.user.username, password=request.POST['userOldPassword']):
            if request.POST['userNewPassword'] == request.POST['userReNewPassword']:
                user.set_password(request.POST['userNewPassword'])
                user.save()
                user = auth(username=request.user.username, password=request.POST['userNewPassword'])
                login(request, user)
            else:
                cp_form = ChangePasswordForm(request.POST or None)
        else:
            cp_form = ChangePasswordForm(request.POST or None)
    else:
        cp_form = ChangePasswordForm(request.POST or None)

    if request.method == "POST" and request.POST['submit'] == "change_email":
        import re
        email_form = ChangeEmailForm(request.POST or None)
        user = request.user
        if auth(username=request.user.username, password=request.POST['password']):
            if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?))$", request.POST['new_email']) != None:
                user.username = request.POST['new_email']
                user.email = request.POST['new_email']
                user.save()
                user = auth(username=request.POST['new_email'], password=request.POST['password'])
                login(request, user)
            else:
                messages.add_message(request, messages.ERROR, 'Enter a valid e-mail address.')
        else:
            email_form = ChangeEmailForm(request.POST or None)
    else:
        email_form = ChangeEmailForm(request.POST or None)

    if request.method == 'POST' and request.POST['submit'] == "causes_i_care_about":
        cause_form = NewCausesForm(request.POST or None)
        for i in request.POST:
            print (request.POST[i])
            if i != 'submit' and i != 'csrfmiddlewaretoken':
                cause = Causes_I_Care_About(username=request.user, cause_id=request.POST[i])
                cause.save()
            else:
                cause_form = NewCausesForm(request.POST or None)
    else:
        cause_form = NewCausesForm(request.POST or None)




    user_details = User_Details.objects.get(username=request.user.id)
    project = Project.objects.annotate(x=F('raised_amount') / F('total_amount')).order_by('-x')
    project = project[0]
    chosen_causes = Causes_I_Care_About.objects.filter(username=request.user)
    print chosen_causes
    exclude_cause_id = [cause.cause_id for cause in chosen_causes]
    not_chosen_causes = Cause.objects.exclude(cause_id__in=exclude_cause_id)
    ongoing_project_donations = Donation.objects.filter(donor_id=request.user.id, project_id__end_date__gte=datetime.date.today())
    completed_project_donations = Donation.objects.filter(donor_id=request.user.id, project_id__end_date__lte=datetime.date.today())
    project_list = Project.objects.all()

    return render(request, 'userPage.html', {'user_details': user_details,
                                             'ongoing_project_donations': ongoing_project_donations,
                                             'completed_project_donations': completed_project_donations,
                                             'form': form,
                                             'card_form': card_form,
                                             'cp_form':cp_form,
                                             'email_form': email_form,
                                             'cards': cards,
                                             'projects': project_list,
                                             'chosen_causes': chosen_causes,
                                             'not_chosen_causes': not_chosen_causes,
                                             'max_project': project,
                                             'cause_form': cause_form})


def NGOformPage (request):
    if request.method == "POST":  # if the form has been submitted
        form = NGORegistrationForm(request.POST or None)
        name = request.POST['name']
        sector = request.POST['sector']
        since = request.POST['since']
        location = request.POST['location']
        legal_id = request.POST['legal_id']
        affiliation = request.POST['affiliation']
        board_no = request.POST['board_no']
        employee_no = request.POST['employee_no']
        min_pay = request.POST['min_pay']
        avg_pay = request.POST['avg_pay']
        offices_no = request.POST['offices_no']
        office_loc = request.POST['office_loc']

        ngo = NGOtemp(name=name,
                      sector=sector,
                      since=since,
                      location=location,
                      legal_id=legal_id,
                      affiliation=affiliation,
                      board_no=board_no,
                      employee_no=employee_no,
                      min_pay=min_pay,
                      avg_pay=avg_pay,
                      offices_no=offices_no,
                      office_loc=office_loc)
        ngo.save()
        context_dict = {'form': form}
    else:
        form = NGORegistrationForm(request.POST or None)
        context_dict = {'form': form}
    return render(request, 'NGOForm.html', context_dict)











