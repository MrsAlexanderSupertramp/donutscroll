# Generated by Django 3.0.4 on 2020-07-02 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0009_comments_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.CharField(default='-', max_length=40),
        ),
        migrations.AddField(
            model_name='comments_reply',
            name='date',
            field=models.CharField(default='-', max_length=40),
        ),
    ]
