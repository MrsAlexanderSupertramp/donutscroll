# Generated by Django 3.0.4 on 2020-07-02 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0010_auto_20200702_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='picurl',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='comments_reply',
            name='picurl',
            field=models.CharField(default='-', max_length=100),
        ),
    ]
