from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render, redirect

from django.core.paginator import Paginator

from map.models import Squirrel

from .forms import form_sightings

def show_all(request):
    squirrels = Squirrel.objects.all()
    context = {'squirrels' : squirrels}
    return render (request, 'sightings/show_all.html', context)

def add(request):
    if request.method == 'POST':
        form = form_sightings(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
        else:
            form = form_sightings()
        return render(request, 'sightings/add.html', {'form':form})





# Create your views here.
