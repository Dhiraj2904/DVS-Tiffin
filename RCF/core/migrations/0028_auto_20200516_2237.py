# Generated by Django 3.0.4 on 2020-05-16 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_menudisplay_mdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menudisplay',
            old_name='mname',
            new_name='Mixed',
        ),
        migrations.AddField(
            model_name='menudisplay',
            name='Premium_Mixed',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menudisplay',
            name='Premium_Veg',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menudisplay',
            name='Vegetarian',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]