# Generated by Django 3.0.4 on 2020-05-10 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_carta'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderdisplay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiffin_type', models.CharField(max_length=100)),
                ('subtiffin_type', models.CharField(max_length=100)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('total_amount', models.IntegerField(max_length=100)),
            ],
        ),
    ]
