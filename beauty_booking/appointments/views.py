from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Specialist
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def homepage(request):
    specialists = Specialist.objects.all()
    return render(request, 'appointments/homepage.html', {'specialists': specialists})

def specialist_profile(request, specialist_id):
    specialist = get_object_or_404(Specialist, id=specialist_id)
    return render(request, 'appointments/specialist_profile.html', {'specialist': specialist})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = UserCreationForm()
    return render(request, 'appointments/register.html', {'form': form})

def about(request):
    return render(request, 'appointments/about.html')

def privacy_policy(request):
    return render(request, 'appointments/privacy_policy.html')

def terms_of_service(request):
    return render(request, 'appointments/terms_of_service.html')

def contact_support(request):
    return render(request, 'appointments/contact_support.html')
