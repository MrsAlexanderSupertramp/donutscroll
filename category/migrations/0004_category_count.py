# Generated by Django 3.0.4 on 2020-04-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_auto_20200415_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='count',
            field=models.IntegerField(default='0'),
        ),
    ]
