# Generated by Django 3.0.4 on 2020-07-06 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_mostpopular'),
    ]

    operations = [
        migrations.AddField(
            model_name='mostpopular',
            name='position',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
