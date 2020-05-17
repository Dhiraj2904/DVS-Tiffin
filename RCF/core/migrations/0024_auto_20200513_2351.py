# Generated by Django 3.0.4 on 2020-05-13 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20200513_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carta',
            name='id',
        ),
        migrations.AddField(
            model_name='carta',
            name='cid',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carta',
            name='sabji',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carta',
            name='sweets',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
