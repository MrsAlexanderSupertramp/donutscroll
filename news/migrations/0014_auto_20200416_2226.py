# Generated by Django 3.0.4 on 2020-04-16 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20200416_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='picname',
            field=models.TextField(default='-'),
        ),
    ]