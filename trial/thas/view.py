from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Customers, CustomerForm
from django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')


class CustomForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


def register(request):
    forms = CustomForm()
    if request.method == 'POST':
        forms = CustomForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('loginpage')
        # else:
        # messages.error(request, 'registration failed')
    context = {'forms': forms}
    return render(request, 'register.html', context)


def loginpage(request):
    return render(request, 'login.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def contactus(request):
    return render(request, 'contactus.html')


def dashboard(request):
    data = Customers.objects.all()
    form = CustomerForm()
    if request.method == 'POST':
        form_data = CustomerForm(request.POST)
        if form_data.is_valid():
            form_data.save()
    context = {'data': data, 'form': form}
    return render(request, 'dashboard.html', context)
