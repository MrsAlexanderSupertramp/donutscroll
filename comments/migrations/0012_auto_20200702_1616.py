# Generated by Django 3.0.4 on 2020-07-02 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0011_auto_20200702_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments_reply',
            name='body',
            field=models.TextField(blank=True, default='-', null=True),
        ),
        migrations.AlterField(
            model_name='comments_reply',
            name='email',
            field=models.CharField(blank=True, default='-', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='comments_reply',
            name='name',
            field=models.CharField(blank=True, default='-', max_length=50, null=True),
        ),
    ]
