# Generated by Django 3.0.8 on 2020-07-07 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newscontent', '0002_newscontent_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newscontent',
            name='published_date',
            field=models.DateField(blank=True),
        ),
    ]
