# Generated by Django 3.0.4 on 2020-04-16 15:55

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20200416_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='-'),
        ),
        migrations.AlterField(
            model_name='news',
            name='short_text',
            field=ckeditor.fields.RichTextField(default='-'),
        ),
    ]
