# Generated by Django 3.0.4 on 2020-05-16 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_remove_news_short_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='trending',
            field=models.BooleanField(default=False),
        ),
    ]
