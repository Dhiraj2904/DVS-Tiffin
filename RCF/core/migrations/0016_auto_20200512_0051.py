# Generated by Django 3.0.4 on 2020-05-11 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0015_auto_20200512_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empinsert',
            name='author',
        ),
        migrations.RemoveField(
            model_name='empinsert',
            name='id',
        ),
        migrations.AddField(
            model_name='empinsert',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='empinsert',
            name='ordernow_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
