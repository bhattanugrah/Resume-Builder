# Generated by Django 2.2.2 on 2019-07-30 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='user_data',
            name='zipcode',
        ),
    ]
