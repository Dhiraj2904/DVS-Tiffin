# Generated by Django 3.0.4 on 2020-05-10 17:13

import RCF.core.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_orderdisplay_oid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empinsert',
            name='id',
        ),
        migrations.RemoveField(
            model_name='orderdisplay',
            name='id',
        ),
        migrations.AddField(
            model_name='empinsert',
            name='ordernow_id',
            field=models.CharField(default=1, max_length=100, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empinsert',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(RCF.core.models.get_sentinel_user), to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='empinsert',
            name='total_amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orderdisplay',
            name='oid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
