# Generated by Django 3.1.7 on 2021-09-06 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='is_admin',
        ),
    ]
