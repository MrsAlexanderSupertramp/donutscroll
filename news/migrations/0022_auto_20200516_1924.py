# Generated by Django 3.0.4 on 2020-05-16 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0021_auto_20200516_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='trending',
            field=models.BooleanField(default=False),
        ),
    ]