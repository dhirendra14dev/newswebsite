# Generated by Django 3.0.8 on 2020-07-21 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newscontent', '0005_auto_20200718_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='newscontent',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
