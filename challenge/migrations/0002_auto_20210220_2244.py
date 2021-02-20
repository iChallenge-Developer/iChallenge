# Generated by Django 3.1.6 on 2021-02-20 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('challenge', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chEnrollment_set', to=settings.AUTH_USER_MODEL, verbose_name='유저'),
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together={('challenge', 'player')},
        ),
    ]
