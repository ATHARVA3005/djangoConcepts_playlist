# Generated by Django 4.0.5 on 2022-07-30 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Student',
        ),
    ]