# Generated by Django 2.1 on 2018-08-06 09:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('21bbe117-aea2-4e68-80cf-f1036b946032'), unique=True),
        ),
    ]
