# Generated by Django 3.0.4 on 2020-05-11 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200512_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empinsert',
            name='ordernow_id',
        ),
        migrations.AddField(
            model_name='empinsert',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]