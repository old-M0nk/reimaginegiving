from django.shortcuts import render
from .forms import email_form
from .models import Email


# def comingSoon(request):
#     if request.method == "POST":
#         form = Email(request.POST)
#         if form.is_valid():
#                 form.save()
#                 # post.save()
#                 form = Email()
#                 context_dict = {'message': 'We will remember you :)', 'form': form}
#                 return render(request, 'comingSoon.html', context_dict)
#         else:
#             # email = HttpResponse.POST["email"]
#             # if Email.objects.filter(email=email).exists():
#             context_dict = {'message': 'We already remember you ;)', 'form': form}
#             return render(request, 'comingSoon.html', context_dict)
#     else:
#         form = Email()
#         return render(request, 'comingSoon.html', {'form': form})


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

