# Generated by Django 3.0.4 on 2020-05-03 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_auto_20200426_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='short_text',
        ),
    ]