# Generated by Django 2.2.4 on 2019-08-17 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cgi_backend', '0002_auto_20190817_1210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='games',
            old_name='ge',
            new_name='title',
        ),
    ]
