# Generated by Django 2.1 on 2018-08-11 10:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20180808_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('e1ee1b4e-55ad-463f-9a3e-33f9632a4a90')),
        ),
    ]
