# Generated by Django 3.0.4 on 2020-07-08 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_mostpopular_position'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MostPopular',
            new_name='FeaturedHome',
        ),
    ]
