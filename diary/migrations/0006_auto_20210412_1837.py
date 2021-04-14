# Generated by Django 3.1.7 on 2021-04-12 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diary', '0005_auto_20210408_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='entry',
            name='parentDiary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diary.diary'),
        ),
    ]