# Generated by Django 3.0.4 on 2020-05-29 04:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0039_auto_20200529_0903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carta',
            old_name='aamount',
            new_name='camount',
        ),
        migrations.RenameField(
            model_name='carta',
            old_name='aid',
            new_name='cid',
        ),
        migrations.RenameField(
            model_name='carta',
            old_name='amenu',
            new_name='cmenu',
        ),
        migrations.AddField(
            model_name='carta',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carta',
            name='ramt',
            field=models.IntegerField(default=1),
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
            name='samt',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carta',
            name='swamt',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carta',
            name='sweets',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='alacartaorder',
            table='alacarta',
        ),
        migrations.AlterModelTable(
            name='carta',
            table='menualcarta',
        ),
    ]