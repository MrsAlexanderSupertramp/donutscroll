# Generated by Django 3.0.4 on 2020-06-06 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0024_news_identifier_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='intro_text',
            field=models.CharField(default='-', max_length=1000),
        ),
    ]