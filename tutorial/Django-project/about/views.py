from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'about.html')

def news(request):
    return HttpResponse('<h1>This is news</h1>')