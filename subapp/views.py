from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def subindex(request):
    return render(request,
                  'subapp/index.html',
                  {})