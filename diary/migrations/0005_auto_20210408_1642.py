# Generated by Django 3.1.7 on 2021-04-08 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_auto_20210408_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='uuid',
            field=models.CharField(max_length=36),
        ),
        migrations.AlterField(
            model_name='entry',
            name='uuid',
            field=models.CharField(max_length=36),
        ),
    ]
