# Generated by Django 5.0.4 on 2024-04-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='trending',
            field=models.BooleanField(default=False, help_text='0-default,1-Trending'),
        ),
    ]
