# Generated by Django 3.0.4 on 2020-05-16 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_dtdisplay_ltdisplay'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dtdisplay',
            old_name='Mixed1',
            new_name='Mixed',
        ),
        migrations.AddField(
            model_name='carta',
            name='camount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]