from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):
    latitude = models.CharField(max_length = 255,)
    
    longitude = models.CharField(max_length = 255,)

    unique_squirrel_id = models.CharField(
        max_length = 255,
        primary_key = True,
    )

    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = [
        (AM, _('AM')),
        (PM, _('PM')),
    ]

    shift = models.CharField(
        help_text = _('shift in the day'),
        max_length = 15,
        choices = SHIFT_CHOICES,
        blank = True,
    )

    date = models.DateField(
        help_text = _('sighting date'),
        blank = True,
    )

    Adult = 'Adult'
    Juvenile = 'Juvenile'

    AGE_CHOICES = [
        (Adult, _('Adult')),
        (Juvenile, _('Juvenile')),
    ]

    age = models.CharField(
        help_text = _('age of squirrel'),
        max_length = 30,
        choices = AGE_CHOICES,
        default='Unknown',
        blank = True,
    )

    Gray = 'Gray'
    Cinnamon ='Cinnamon'
    Black = 'Black'

    COLOR_CHOICES = [
        (Gray, _('Gray')),
        (Cinnamon, _('Cinnamon')),
        (Black, _('Black')),
    ]

    primary_fur_color = models.CharField(
        help_text = _('primary_fur_color of squirrel'),
        max_length = 30,
        choices = COLOR_CHOICES,
        blank = True,
    )

    Above = 'Above Ground'
    Ground = 'Ground Plane'

    LOCATION_CHOICES = [
        (Above, _('Above Ground')),
        (Ground, _('Ground Plane')),
    ]

    location = models.CharField(
        help_text = _('location of squirrel'),
        max_length = 30,
        choices = LOCATION_CHOICES,
        blank = True,
    )

    specific_location = models.CharField(
        help_text = _('specific location of squirrel'),
        max_length = 255,
        blank = True,
    )

    running = models.BooleanField(
        help_text = _('true if squirrel was running'),
        default = False,
        blank = True,
    )

    chasing = models.BooleanField(
        help_text = _('true if squirrel was chasing'),
        default = False,
        blank = True,
    )

    climbing = models.BooleanField(
        help_text = _('true if squirrel was climbing'),
        default = False,
        blank = True,
    )

    eating = models.BooleanField(
        help_text = _('true if squirrel was eating'),
        default = False,
        blank = True,
    )

    foraging = models.BooleanField(
        help_text = _('true if squirrel was foraging'),
        default = False,
        blank = True,
    )

    other_activities = models.CharField(
        help_text = _('other activities'),
        max_length = 255,
        blank = True,
    )

    kuks = models.BooleanField(
        help_text = _('true if squirrel was kuking'),
        default = False,
        blank = True,
    )

    quaas = models.BooleanField(
        help_text = _('true if squirrel was quaaing'),
        default = False,
        blank = True,
    )

    moans = models.BooleanField(
        help_text = _('true if squirrel was moaning'),
        default = False,
        blank = True,
    )

    tail_flags = models.BooleanField(
        help_text = _('true if squirrel was flagging tail'),
        default = False,
        blank = True,
    )

    tail_twitches = models.BooleanField(
        help_text = _('true if squirrel was twitching tail'),
        default = False,
        blank = True,
    )

    approaches = models.BooleanField(
        help_text = _('true if squirrel was approaching'),
        default = False,
        blank = True,
    )

    indifferent = models.BooleanField(
        help_text = _('true if squirrel was indifferent to human'),
        default = False,
        blank = True,
    )

    runs_from = models.BooleanField(
        help_text = _('true if squirrel was running from human'),
        default = False,
        blank = True,
    )

    def __str__(self):
        return self.unique_squirrel_id


# Create your models here.
