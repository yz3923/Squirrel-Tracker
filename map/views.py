from django.shortcuts import render

from django.http import HttpResponse

from .models import Squirrel

def index(request):
    context = {
        'mapping_squirrels' : Squirrel.objects.all()[:90]
    }
    return render(request, 'map/index.html', context)
# Create your views here.
