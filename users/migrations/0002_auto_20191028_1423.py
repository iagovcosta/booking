# Generated by Django 2.2.6 on 2019-10-28 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='produtorBanda',
            new_name='tipo',
        ),
    ]
