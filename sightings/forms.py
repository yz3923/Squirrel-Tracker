from django.forms import ModelForm

from map.models import Squirrel


class SquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__'
        labels = {
                "unique_squirrel_id": "unique_squirrel_id should not be blank"
            }


