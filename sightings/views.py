from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404

from map.models import Squirrel
from .forms import SquirrelForm


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

def edit(request, unique_squirrel_id):
    squirrel = get_object_or_404(Squirrel,pk = unique_squirrel_id)
    if request.method == 'POST':
        form = form_sightings(request.POST, instance=squirrel)
        context = {
                'form': form
                }
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{squirrel_id}')
    else:
        form = form_sightings(instance=squirrel)
    return render(request, "sightings/edit.html",context)


def stats(request):

    total = Squirrel.objects.count()
    ages = Squirrel.objects.values('age').annotate(c=Count('age'))
    fur_colors = Squirrel.objects.values(
            'primary_fur_color').annotate(c=Count('primary_fur_color'))
    shifts = Squirrel.objects.values('shift').annotate(c=Count('shift'))
    locations= Squirrel.objects.values('location').annotate(c=Count('location'))
    context= {
            'total':total,
            'ages':ages,
            'fur_colors':fur_colors,
            'shifts':shifts,
            'locations':locations,
        }
    return render(request,'sightings/stats.html',context)




# Create your views here.
