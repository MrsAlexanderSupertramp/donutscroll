# Generated by Django 3.0.4 on 2020-07-08 09:12

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0031_auto_20200707_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='newsbody'),
        ),
    ]
