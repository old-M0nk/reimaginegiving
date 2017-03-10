from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic import View
from .forms import email_form, UserLoginForm, UserRegistrationForm
from .models import Email, User_Details
from django.contrib.auth import authenticate as auth
from django.contrib.auth.decorators import login_required

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
            context_dict = {'message': message}
            page = 'index.html'
        else:
            # Return an 'invalid login' error message.
            context_dict = {'message': 'Incorrect Credentials', 'form': form}
            page = 'registration/login.html'

    else:#if the form has not been submitted
        form = UserLoginForm(request.POST or None)
        context_dict = {'form':form, 'message': "Login blah"}
        page = 'registration/login.html'

    if request.user.is_authenticated():
        return render(request, page, context_dict)


def register_view(request):
    if request.method == "POST":  # if the form has been submitted
        form = UserRegistrationForm(request.POST or None)
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        #check if the passwords match
        if password == password2:
            user = User(username=username, email=username, password=password)
            # user = user.save(commit=False)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.set_password(password)
            user.save()
            login(request, user)
            context_dict = {
                "message": "Welcome",
            }
        else:
            context_dict = {'form': form, 'message': "Passwords did not match!"}
    else:
        form = UserRegistrationForm(request.POST or None)
        context_dict = {'form': form}
    return render(request, 'index.html', context_dict)



@login_required
def logout_view(request):
    logout(request)
    return render(request, 'index.html', {})


@login_required
def userPage (request):
    user_details = User_Details.objects.get(username=request.user.id)
    return render(request, 'userPage.html', {'user_details': user_details})











