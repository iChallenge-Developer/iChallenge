# Generated by Django 3.1.6 on 2021-02-19 19:49

from django.db import migrations, models
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_ToS',
            field=models.BooleanField(default=False, validators=[login.models.is_ToS]),
        ),
    ]
