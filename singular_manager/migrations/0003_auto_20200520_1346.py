# Generated by Django 3.0.4 on 2020-05-20 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('singular_manager', '0002_auto_20200520_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='singular_manager',
            old_name='identifier_list',
            new_name='identifier',
        ),
    ]