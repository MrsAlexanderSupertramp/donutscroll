# Generated by Django 3.0.4 on 2020-04-16 07:30

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200415_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='short_text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]