from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render

from django.core.paginator import Paginator

from .models import Squirrels

def show_all(request):
    squirrels = Squirrel.objects.all()
    context = {'squirrels' : squirrels}
    return render (request, 'sightings/show_all.html', context)

def create(request):
    if request.method == 'POST':
        form = form_sightings(request.POST)
        if form.is_valid():
            form.save()
            return render('/sightings')



# Create your views here.
