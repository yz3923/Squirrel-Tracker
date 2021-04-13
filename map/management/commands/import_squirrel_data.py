from django.core.management import BaseCommand

from map.models import Squirrel

import csv
import datetime

class Command(BaseCommand):
    help = 'import squirrel data as csv. file'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):

        with open(kwargs['path'], encoding='utf-8') as abc:
            read_in = csv.DictReader(abc)
            data_frame = list(read_in)

        for i in data_frame:
            individual = Squirrel(
                longitude = i['X'],
                latitude = i['Y'],
                unique_squirrel_id = i['Unique Squirrel ID'],
                shift = i['Shift'],
                date=datetime.date(int(i['Date'][4:8]),int(i['Date'][:2]),int(i['Date'][2:4])),
                age = i['Age'],
                primary_fur_color = i['Primary Fur Color'],
                location = i['Location'],
                specific_location = i['Specific Location'],
                running = True if i['Running'].lower() == 'true' else False ,
                chasing = True if i['Chasing'].lower() == 'true' else False,
                climbing = True if i['Climbing'].lower() == 'true' else False,
                eating = True if i['Eating'].lower() == 'true' else False,
                foraging = True if i['Foraging'].lower() == 'true' else False,
                other_activities = i['Other Activities'],
                kuks = True if i['Kuks'].lower() == 'true' else False,
                quaas = True if i['Quaas'].lower() == 'true' else False,
                moans = True if i['Moans'].lower() == 'true' else False,
                tail_flags = True if i['Tail flags'].lower() == 'true' else False,
                tail_twitches = True if i['Tail twitches'].lower() == 'true' else False,
                approaches = True if i['Approaches'].lower() == 'true' else False,
                indifferent = True if i['Indifferent'].lower() == 'true' else False,
                runs_from = True if i['Runs from'].lower() == 'true' else False,
            )

            individual.save()

