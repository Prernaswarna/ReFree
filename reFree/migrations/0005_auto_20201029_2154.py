# Generated by Django 3.1.2 on 2020-10-29 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reFree', '0004_auto_20201029_2139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phonenumber',
            new_name='phone_number',
        ),
    ]
