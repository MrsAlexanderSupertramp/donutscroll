# Generated by Django 3.0.4 on 2020-07-06 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_mostviewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='mostviewed',
            name='date',
            field=models.CharField(default='-', max_length=50),
        ),
    ]