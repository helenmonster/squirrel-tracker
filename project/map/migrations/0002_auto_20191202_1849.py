# Generated by Django 2.2.7 on 2019-12-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sightings',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
