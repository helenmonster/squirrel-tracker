# Generated by Django 2.2.7 on 2019-12-01 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sightings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=20, max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=20, max_digits=20)),
            ],
        ),
    ]
