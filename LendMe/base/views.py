from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required 
from .forms import FinanceInfo
# Create your views here.

def home(request):

    return render(request, 'home.html')

@login_required 
def login(request):
    return render(request, 'login.html')

@login_required
def profile(request):
    return HttpResponse('You are logged in!')


@login_required 
def get_finance_info(request):
    context = {}
    context['form'] = FinanceInfo()
    return render(request, 'finance_info.html', context)



