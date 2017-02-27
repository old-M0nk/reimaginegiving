from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Email

#
# def index(request):
#     return HttpResponse("Users Application")
from .forms import Email


def comingSoon(request):
    if request.method == "POST":
        form = Email(request.POST)
        if form.is_valid():
                form.save()
                # post.save()
                form = Email()
                context_dict = {'message': 'We will remember you :)', 'form': form}
                return render(request, 'comingSoon.html', context_dict)
        else:
            # email = HttpResponse.POST["email"]
            # if Email.objects.filter(email=email).exists():
            context_dict = {'message': 'We already remember you ;)', 'form': form}
            return render(request, 'comingSoon.html', context_dict)
    else:
        form = Email()
        return render(request, 'comingSoon.html', {'form': form})
