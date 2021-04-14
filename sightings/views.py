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
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/sightings/')
    else:
        form = SquirrelForm()
        context = {'form':form}
        return render(request, 'sightings/add.html', context)

def edit(request, unique_squirrel_id):
    squirrel = get_object_or_404(Squirrel,pk = unique_squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{unique_squirrel_id}')
    else:
        form = SquirrelForm(instance=squirrel)
    context = { 'form': form }
    return render(request, "sightings/edit.html",context)


def stats(request):

    total = Squirrel.objects.count()
    juvenile_age = Squirrel.objects.filter(age='Juvenile').count()
    adult_age = Squirrel.objects.filter(age='Adult').count()
    fur_black = Squirrel.objects.filter(primary_fur_color='Black').count()
    fur_cinnamon = Squirrel.objects.filter(primary_fur_color='Cinnamon').count()
    fur_gray = Squirrel.objects.filter(primary_fur_color='Gray').count()
    shifts = Squirrel.objects.values('shift').annotate(c=Count('shift'))
    location_above = Squirrel.objects.filter(location='Above Ground').count()
    location_ground = Squirrel.objects.filter(location='Ground Plane').count()
    context= {
            'total':total,
            'juvenile_age':juvenile_age,
            'adult_age':adult_age,
            'fur_black':fur_black,
            'fur_cinnamon':fur_cinnamon,
            'fur_gray':fur_gray,
            'shifts':shifts,
            'location_above':location_above,
            'location_ground':location_ground,
        }
    return render(request,'sightings/stats.html',context)




# Create your views here.
