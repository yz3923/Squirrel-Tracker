# Generated by Django 3.2 on 2021-04-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20210415_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='date',
            field=models.DateField(blank=True, default='Unknown', help_text='sighting date'),
        ),
    ]
