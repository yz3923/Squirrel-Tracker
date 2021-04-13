from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render

from django.core.paginator import Paginator

from .models import Squirrels

def show_all(request):


# Create your views here.
