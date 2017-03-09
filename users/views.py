from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic import View
from .forms import email_form, UserLoginForm, UserRegistrationForm
from .models import Email
from django.contrib.auth import authenticate as auth

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
        else:
            # Return an 'invalid login' error message.
            context_dict = {'message': 'Incorrect Credentials', 'form': form}

    else:#if the form has not been submitted
        form = UserLoginForm(request.POST or None)
        context_dict = {'form':form, 'message': "Login blah"}
    return render(request, 'registration/login.html', context_dict)


def register_view(request):
    title = "Register"
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        user.set_password(password)
        user.save()
        login(request, user)

    context = {
        "form": form,
        "title": title
    }
    return render(request, 'registration/register.html', context)


def logout_view(request):
    logout(request)
    return render(request, 'index.html', {})

# def validateEmail(username):#function for checking if the username is in the correct email format
#     from django.core.validators import validate_email
#     from django.core.exceptions import ValidationError
#     try:
#         validate_email(username)
#         return True
#     except ValidationError:
#         return False
#
# if validateEmail(username):#if the username is in the correct email format
#     user = authenticate(username=username, password=password)#try authenticating user
#     if user is not None:
#         login(request, user)
#         print("True")
#         message = "You're already logged in!"
#         context_dict = {'message': message}
#     else:
#         context_dict = {'message': 'Incorrect Credentials', 'form': form}
# else:
#     context_dict = {'message': 'Incorrect Credentials', 'form': form}










