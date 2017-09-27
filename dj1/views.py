from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
from django.forms import ModelForm
from .indexForm import IndexForm


def indexView(request):
    if request.method ==  'POST':
        form = IndexForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            return HttpResponse(firstName + '  ' + lastName)
    else:
        form = IndexForm()

    return render(request,'index.html',{'welcome':'Hi , Welcom new world .','form':form})