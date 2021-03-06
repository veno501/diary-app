# Generated by Django 3.1.7 on 2021-09-10 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaryEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default=uuid.uuid4, max_length=36)),
                ('title', models.CharField(max_length=50)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(blank=True, default='', max_length=200)),
                ('mood', models.IntegerField(choices=[(1, '🙂'), (2, '😶'), (3, '🙁')], default=2)),
                ('content', models.CharField(blank=True, default='', max_length=8000)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
