from django.core.management import BaseCommand

from map.models import Squirrel

import sys

import csv

class Command(BaseCommand):
    help = 'export squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, path, **kwargs):
        with open(path, 'w', newline='') as f:
            field = [f.name for f in Squirrel._meta.fields]
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(field)
            for i in Squirrel.objects.all():
                writer.writerow([getattr(i, j) for j in field])

