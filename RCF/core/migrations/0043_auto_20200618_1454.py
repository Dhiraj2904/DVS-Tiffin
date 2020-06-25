# Generated by Django 3.0.4 on 2020-06-18 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0042_auto_20200531_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='alacartaorder',
            fields=[
                ('aid', models.IntegerField(primary_key=True, serialize=False)),
                ('amenu', models.CharField(max_length=100)),
                ('aamount', models.IntegerField()),
            ],
            options={
                'db_table': 'alacarta',
            },
        ),
        migrations.RemoveField(
            model_name='carorder',
            name='author_id',
        ),
        migrations.AddField(
            model_name='carorder',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dtdisplay',
            name='Mixed',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
