from django.forms import ModelForm 
from map.models import Squirrel

class form_sightings(ModelForm):
    class = Meta:
        model = map.models
        fields = ['latitude', 'longitude', 'unique_squirrel_id', 'shift', 'date', 'age']
