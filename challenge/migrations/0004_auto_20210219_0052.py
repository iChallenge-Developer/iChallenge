# Generated by Django 3.1.6 on 2021-02-18 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0003_auto_20210219_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='cur_pp',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
