# Generated by Django 3.1.6 on 2021-02-14 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendship',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friendship',
            name='me',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='self_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together={('me', 'friend')},
        ),
    ]
