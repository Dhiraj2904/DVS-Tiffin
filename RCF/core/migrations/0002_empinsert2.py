# Generated by Django 3.0.4 on 2020-05-03 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpInsert2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttype', models.CharField(max_length=100)),
            ],
        ),
    ]
