# Generated by Django 3.0.4 on 2020-05-21 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_alacartaorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alacartaorder',
            name='author',
        ),
    ]
