# Generated by Django 3.0.4 on 2020-07-06 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_headingdropdown'),
    ]

    operations = [
        migrations.CreateModel(
            name='MostViewed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(default='-', max_length=50)),
                ('name', models.CharField(default='-', max_length=100)),
                ('picurl', models.TextField(default='-')),
            ],
        ),
    ]
