# Generated by Django 3.0.6 on 2021-01-17 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210117_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='passwors',
            new_name='password',
        ),
    ]
