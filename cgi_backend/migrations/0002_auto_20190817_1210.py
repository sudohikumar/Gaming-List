# Generated by Django 2.2.4 on 2019-08-17 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cgi_backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='games',
            old_name='title',
            new_name='ge',
        ),
    ]
