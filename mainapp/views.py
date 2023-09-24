from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def mainindex(request):
    return render(request,
                  'mainapp/index.html',
                  {})