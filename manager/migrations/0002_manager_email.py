# Generated by Django 3.0.4 on 2020-06-27 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='email',
            field=models.CharField(default='', max_length=30),
        ),
    ]
