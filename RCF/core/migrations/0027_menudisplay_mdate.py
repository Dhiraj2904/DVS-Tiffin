# Generated by Django 3.0.4 on 2020-05-16 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20200514_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='menudisplay',
            name='mdate',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
