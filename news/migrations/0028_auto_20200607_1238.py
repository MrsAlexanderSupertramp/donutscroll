# Generated by Django 3.0.4 on 2020-06-07 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0027_auto_20200606_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body_text',
            field=models.TextField(),
        ),
    ]
