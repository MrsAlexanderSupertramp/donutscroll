# Generated by Django 3.0.4 on 2020-04-15 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20200415_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
    ]
