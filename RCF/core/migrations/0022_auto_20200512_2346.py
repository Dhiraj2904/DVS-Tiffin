# Generated by Django 3.0.4 on 2020-05-12 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20200512_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carta',
            name='id',
        ),
        migrations.AddField(
            model_name='carta',
            name='camount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carta',
            name='cid',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]