# Generated by Django 3.0.4 on 2020-04-26 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_auto_20200421_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='picname',
            field=models.TextField(default='-'),
        ),
    ]
